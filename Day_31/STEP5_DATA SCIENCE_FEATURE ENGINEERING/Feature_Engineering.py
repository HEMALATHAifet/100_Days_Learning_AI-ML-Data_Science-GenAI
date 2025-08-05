import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load preprocessed dataset
df = pd.read_csv("preprocessed_maternal_health_data.csv")
print(df.columns)
# Feature 1: Blood Pressure Ratio
df['BP Ratio'] = df['Systolic BP'] / df['Diastolic']
# Feature 2: Complication Score (sum of 3 binary indicators)
df['Complication Score'] = df[['Previous Complications', 'Preexisting Diabetes', 'Gestational Diabetes']].sum(axis=1)
# Feature 3: High Blood Pressure Flag
df['High BP Flag'] = ((df['Systolic BP'] > 140) | (df['Diastolic'] > 90)).astype(int)
# Preview the new features
print(df[['Systolic BP', 'Diastolic', 'BP Ratio', 'Complication Score', 'High BP Flag']].head())
import numpy as np
np.random.seed(42)
df['Risk Level'] = np.random.choice(['Low', 'Mid', 'High'], size=len(df))
# 1. Average BP Ratio by Risk Level
plt.figure(figsize=(8, 5))
sns.barplot(x='Risk Level', y='BP Ratio', data=df, ci='sd')
plt.title("Average BP Ratio across Risk Levels")
plt.tight_layout()
plt.savefig("barplot_bp_ratio.png")
plt.show()
# 2. Complication Score distribution by Risk Level
plt.figure(figsize=(8, 5))
sns.boxplot(x='Risk Level', y='Complication Score', data=df)
plt.title("Complication Score by Risk Level")
plt.tight_layout()
plt.savefig("boxplot_complication_score.png")
plt.show()
# 3. High BP Flag distribution
plt.figure(figsize=(8, 5))
sns.countplot(x='Risk Level', hue='High BP Flag', data=df)
plt.title("High BP Flag Count across Risk Levels")
plt.tight_layout()
plt.savefig("countplot_high_bp_flag.png")
plt.show() 
