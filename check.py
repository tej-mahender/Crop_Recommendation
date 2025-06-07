import pandas as pd

try:
    companion_data = pd.read_pickle('models/companion_data.pkl')
    print(f"Type: {type(companion_data)}")
    print(companion_data.head())
    print(f"Columns: {companion_data.columns}")

    assert 'crop' in companion_data.columns, "'crop' column is missing!"
    assert 'cluster' in companion_data.columns, "'cluster' column is missing!"

    print("✅ companion_data.pkl is valid with 'crop' and 'cluster' columns.")

except FileNotFoundError:
    print("❌ File 'models/companion_data.pkl' not found. Please create it first.")

except AssertionError as ae:
    print(f"❌ Assertion error: {ae}")

except Exception as e:
    print(f"❌ An error occurred: {e}")
