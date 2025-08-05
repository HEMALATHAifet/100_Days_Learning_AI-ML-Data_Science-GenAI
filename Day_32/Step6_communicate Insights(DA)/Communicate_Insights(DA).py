import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("preprocessed_maternal_health_data.csv")

# Set style
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

# 🔸 1. Heatmap for correlations
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("🔍 Correlation Heatmap of Features")
plt.tight_layout()
plt.show()

# 🔸 2. Pie Chart for Risk Level Distribution
plt.figure(figsize=(6, 6))
df['RiskLevel'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, shadow=True)
plt.title("⚠️ Risk Level Distribution")
plt.ylabel("")  # Hide y-label
plt.show()

# 🔸 3. Boxplots for Numerical Features vs Risk Level
num_cols = ['Age', 'Systolic BP', 'Diastolic', 'BS', 'BodyTemp', 'HeartRate']

for col in num_cols:
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x='RiskLevel', y=col, palette='Set2')
    plt.title(f"{col} vs Risk Level")
    plt.show()

# 🔸 4. Barplot: Percentage of High BP/Diabetes in High Risk Group
high_risk_df = df[df['RiskLevel'] == 'high risk']
high_bp_diabetes = high_risk_df[(high_risk_df['Systolic BP'] > 140) | (high_risk_df['BS'] > 120)]
percent = (len(high_bp_diabetes) / len(high_risk_df)) * 100
print(f"✅ Percentage of high-risk pregnancies with high BP or diabetes: {percent:.2f}%")

# 🔸 5. BMI > 35 filter and count in High Risk Group
# If BMI is not in dataset, you might need to calculate it or skip this step.
if 'BMI' in df.columns:
    high_bmi = df[df['BMI'] > 35]
    print(f"💡 Number of records with BMI > 35: {len(high_bmi)}")

# 🔸 6. Mental Health Variance Check
if 'MentalHealth' in df.columns:
    print("📊 Mental Health Variance by Risk Level:")
    print(df.groupby('RiskLevel')['MentalHealth'].describe())

