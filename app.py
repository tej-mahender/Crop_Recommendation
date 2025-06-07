from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
# import warnings
# warnings.filterwarnings("ignore", message="Trying to unpickle estimator .* from version .*")


app = Flask(__name__)

# ========== 🔹 Load Models & Scalers ==========
# Crop Recommendation
with open('models/crop_recommendation_model.pkl', 'rb') as f:
    crop_model = pickle.load(f)
with open('models/scaler_crop_recommendation.pkl', 'rb') as f:
    crop_scaler = pickle.load(f)
with open('models/label_encoder_crop.pkl', 'rb') as f:
    crop_label_encoder = pickle.load(f)

# Companion Crop Recommendation (Clustering)
with open('models/companion_crop_kmeans.pkl', 'rb') as f:
    kmeans_model = pickle.load(f)
with open('models/companion_crop_scaler.pkl', 'rb') as f:
    companion_scaler = pickle.load(f)
with open('models/companion_data.pkl', 'rb') as f:
    companion_data = pickle.load(f)  # Should contain the original DataFrame with 'crop' and 'cluster'

# Yield Prediction
with open('models/yield_prediction_model.pkl', 'rb') as f:
    yield_model = pickle.load(f)
with open('models/yield_prediction_scaler.pkl', 'rb') as f:
    yield_scaler = pickle.load(f)
with open('models/label_encoders_yield.pkl', 'rb') as f:
    label_encoders = pickle.load(f)  # Should be a dict with keys 'Season', 'Crop'


# ========== 🌾 ROUTES ==========

# ---- [1] Crop Recommendation ----
@app.route('/recommend-crop', methods=['POST'])
def recommend_crop():
    try:
        features = request.json  # Expected keys: N, P, K, temperature, humidity, ph, rainfall

         # Validate keys exist
        required_keys = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
        if not all(k in features for k in required_keys):
            return jsonify({"error": f"Missing features. Required keys: {required_keys}"}), 400

        input_data = np.array([[features[k] for k in required_keys]])
        input_scaled = crop_scaler.transform(input_data)
        prediction = crop_model.predict(input_scaled)
        crop_name = crop_label_encoder.inverse_transform(prediction)[0]
        return jsonify({"recommended_crop": crop_name})

    except Exception as e:
        return jsonify({"error": str(e)}), 400


# ---- [2] Companion Crop Grouping ----
@app.route('/recommend-companions', methods=['POST'])
def recommend_companion_crops():
    try:
        crop_name = request.json.get('crop', '').strip().lower()
        if crop_name == '':
            return jsonify({"error": "Please provide a crop name."}), 400

        if crop_name not in companion_data['crop'].values:
            return jsonify({"error": f"Crop '{crop_name}' not found in dataset."}), 400

        cluster_id = companion_data[companion_data['crop'] == crop_name]['cluster'].values[0]
        companions = companion_data[companion_data['cluster'] == cluster_id]['crop'].unique().tolist()
        companions = [c for c in companions if c != crop_name]

        return jsonify({"companions": companions})

    except Exception as e:
        return jsonify({"error": str(e)}), 400


# ---- [3] Yield Prediction ----
@app.route('/predict-yield', methods=['POST'])
def predict_yield():
    try:
        data = request.json  # Expected keys: crop_year, season, crop, area

         # Validate keys exist
        required_keys = ['crop_year', 'season', 'crop', 'area']
        if not all(k in data for k in required_keys):
            return jsonify({"error": f"Missing data. Required keys: {required_keys}"}), 400

        # Validate season and crop
        season = data['season'].strip()
        crop = data['crop'].strip().lower()
        
        if season not in label_encoders['Season'].classes_:
            return jsonify({"error": f"Invalid season. Available: {list(label_encoders['Season'].classes_)}"}), 400
        if crop not in label_encoders['Crop'].classes_:
            return jsonify({"error": f"Invalid crop. Available: {list(label_encoders['Crop'].classes_)}"}), 400

        season_encoded = label_encoders['Season'].transform([season])[0]
        crop_encoded = label_encoders['Crop'].transform([crop])[0]

        input_data = np.array([[data['crop_year'], season_encoded, crop_encoded, data['area']]])
        input_scaled = yield_scaler.transform(input_data)
        predicted_yield = yield_model.predict(input_scaled)[0]
        return jsonify({"predicted_yield": round(predicted_yield, 2)})

    except Exception as e:
        return jsonify({"error": str(e)}), 400


# ---- Root Route ----
@app.route('/')
def home():
    return jsonify({
        "message": "🌱 Welcome to the Smart Agriculture API!",
        "routes": {
            "POST /recommend-crop": "Send N, P, K, temperature, humidity, ph, rainfall",
            "POST /recommend-companions": "Send crop name",
            "POST /predict-yield": "Send crop_year, season, crop, area"
        }
    })


# ========== ✅ MAIN ==========
if __name__ == '__main__':
    app.run(debug=True)
