import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
df = pd.read_csv("Maternal_Health_and_high_risk_pregnancy_dataset.csv")  # Update path if needed

plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Risk Level', y='BMI', palette='Set2')
plt.axhline(35, color='red', linestyle='--', label='BMI Threshold (35)')
plt.title("BMI Distribution by Risk Level")
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Risk Level', y='BS', palette='Set1')
plt.axhline(140, color='purple', linestyle='--', label='BS Threshold (140)')
plt.title("Blood Sugar Levels by Risk Level")
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Risk Level', y='Systolic BP', palette='Pastel1')
plt.axhline(140, color='green', linestyle='--', label='Systolic BP Threshold (>140)')
plt.title("Systolic BP by Risk Level")
plt.legend()
plt.tight_layout()
plt.show()
