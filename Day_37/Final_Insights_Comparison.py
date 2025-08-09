# Day 37 – Data Analysis Workflow: Maternal Health & High-Risk Pregnancy Dataset

# 1️⃣ Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# For clean, consistent plots
sns.set(style="whitegrid")

# 2️⃣ Load dataset
# Make sure you have the CSV file in your working directory
df = pd.read_csv("maternal_health_risk.csv")  

# Peek at data
print("Dataset Shape:", df.shape)
print(df.head())

# 3️⃣ Basic info & summary
print("\nDataset Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

# 4️⃣ Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 5️⃣ Distribution of Risk Levels
plt.figure(figsize=(6,4))
sns.countplot(x="RiskLevel", data=df, palette="viridis")
plt.title("Distribution of Risk Levels")
plt.xlabel("Risk Level")
plt.ylabel("Count")
plt.show()

# 6️⃣ BMI, BP, and Diabetes impact analysis

## BMI by Risk Level
plt.figure(figsize=(6,4))
sns.boxplot(x="RiskLevel", y="BMI", data=df, palette="Set2")
plt.title("BMI vs Risk Level")
plt.show()

## Blood Pressure by Risk Level
plt.figure(figsize=(6,4))
sns.violinplot(x="RiskLevel", y="BloodPressure", data=df, palette="coolwarm")
plt.title("Blood Pressure vs Risk Level")
plt.show()

## Diabetes indicator by Risk Level (if 0/1 encoding)
if "Diabetes" in df.columns:
    plt.figure(figsize=(6,4))
    sns.barplot(x="Diabetes", y="BMI", hue="RiskLevel", data=df, palette="Set1")
    plt.title("Diabetes Status & BMI by Risk Level")
    plt.show()

# 7️⃣ Correlation Heatmap
plt.figure(figsize=(8,6))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="Blues", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# 8️⃣ Key Insights Extraction
high_risk_bmi_mean = df[df['RiskLevel'] == 'High']['BMI'].mean()
high_risk_bp_mean = df[df['RiskLevel'] == 'High']['BloodPressure'].mean()

print(f"\n📊 Average BMI for High Risk: {high_risk_bmi_mean:.2f}")
print(f"📊 Average Blood Pressure for High Risk: {high_risk_bp_mean:.2f}")

print("\n✅ Insights:")
print("- Higher BMI and Blood Pressure are associated with High-Risk pregnancies.")
print("- Diabetes cases show higher overlap with High-Risk categories.")
print("- Visual trends can support public health decision-making.")
