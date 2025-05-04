# 🌱 Smart Agriculture: Crop Recommendation & Yield Prediction using Machine Learning

> Empowering farmers with AI to make data-driven crop choices and estimate yields efficiently.

This machine learning project aims to empower farmers by providing intelligent crop recommendations and predicting expected crop yields based on soil and climate data. The system leverages classification and regression algorithms to enhance decision-making and support sustainable agricultural practices.

## 📌 Overview

This project is a dual-model machine learning solution to support **smart farming** by:

- 🔍 **Recommending the most suitable crop** based on environmental conditions.
- 📈 **Predicting expected crop yield** using factors such as crop year, season, crop type, and area cultivated.
- Support sustainable agriculture aligned with SDGs (Zero Hunger, Responsible Production, Life on Land).


## 📊 Datasets

### 🌾 Crop Recommendation

- 📁 **Features**: `N`, `P`, `K`, `temperature`, `humidity`, `pH`, `rainfall`
- 🎯 **Target**: `crop type`
- 📊 **Samples**: 2200 entries

### 🌱 Yield Prediction

- 📁 **Features**: `Crop Year`, `Season`, `Crop Type`, `Area (hectares)`
- 🎯 **Target**: `Production (metric tons)`


## 🧠 Machine Learning Models

### 🔍 Crop Recommendation (Classification)

| Algorithm               | Accuracy     |
|------------------------|--------------|
| ✅ Random Forest        | **99.39%**   |
| Naïve Bayes            | 98.94%       |
| Support Vector Machine | 98.33%       |
| Decision Tree          | 98.33%       |
| K-Nearest Neighbors    | 97.72%       |
| Logistic Regression    | 94.24%       |

### 📈 Yield Prediction (Regression)

| Algorithm               | R² Score | MAE        | RMSE       |
|------------------------|----------|------------|------------|
| ✅ Random Forest        | **0.8474** | 16,330.54 | 50,668.44  |
| Decision Tree          | 0.6983   | 21,289.12 | 63,245.99  |


## 🛠️ Tech Stack

- **Python 3.x**
- **scikit-learn** for ML models
- **Pandas, NumPy** for data handling
- **Matplotlib, Seaborn** for visualization

