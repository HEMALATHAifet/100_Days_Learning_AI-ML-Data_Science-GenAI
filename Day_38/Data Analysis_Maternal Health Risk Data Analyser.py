# Day 38 - Data Analysis before Deployment

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset
df = pd.read_csv("maternal_health_risk.csv")

# 2. Quick overview
print("\nDataset Shape:", df.shape)
print("\nFirst 5 rows:\n", df.head())
print("\nMissing Values:\n", df.isnull().sum())

# 3. Summary statistics
print("\nSummary Statistics:\n", df.describe())

# 4. Distribution of Risk Levels
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Risk Level", palette="viridis")
plt.title("Distribution of Pregnancy Risk Levels")
plt.xlabel("Risk Level")
plt.ylabel("Count")
plt.show()

# 5. Correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of Features")
plt.show()

# 6. Boxplots for Outlier Detection
numeric_cols = ["Age", "Systolic BP", "Diastolic", "BS", "BMI", "Heart Rate"]
plt.figure(figsize=(12, 8))
for i, col in enumerate(numeric_cols, 1):
    plt.subplot(2, 3, i)
    sns.boxplot(y=df[col], palette="mako")
    plt.title(f"{col} - Outlier Check")
plt.tight_layout()
plt.show()

# 7. Pairplot for Feature Relationship
sns.pairplot(df, hue="Risk Level", diag_kind="kde", palette="husl")
plt.suptitle("Feature Relationships by Risk Level", y=1.02)
plt.show()
