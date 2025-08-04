import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the cleaned dataset
df = pd.read_csv('cleaned_maternal_health_data.csv')

# Step 1: Encode the target variable
risk_map = {'Low Risk': 0, 'Mid Risk': 1, 'High Risk': 2}
df['Risk Level'] = df['Risk Level'].map(risk_map)

# Step 2: Standardize numerical features
features = ['Age', 'Systolic BP', 'Diastolic', 'BS', 'Body Temp', 'BMI', 'Heart Rate']

scaler = StandardScaler()
df[features] = scaler.fit_transform(df[features])

# Step 3: Check class balance
print("Class Distribution (Normalized):")
print(df['Risk Level'].value_counts(normalize=True))

# Step 4 (Optional): Save the preprocessed dataset
df.to_csv('preprocessed_maternal_health_data.csv', index=False)
print("✅ Preprocessed data saved as 'preprocessed_maternal_health_data.csv'")
