# Import required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Optional: Set style
sns.set(style="whitegrid")

# Pairplot to analyze interactions between features colored by RiskLevel
sns.pairplot(df, hue="RiskLevel", palette="Set2", diag_kind="kde")
plt.suptitle("Pairplot of Features by Risk Level", y=1.02)
plt.show()

# Violin plot: Distribution of Blood Sugar (BS) by Risk Level
plt.figure(figsize=(8, 5))
sns.violinplot(x='RiskLevel', y='BS', data=df, palette='muted')
plt.title('Distribution of Blood Sugar by Risk Level')
plt.show()

# Swarm plot: BMI vs Risk Level
plt.figure(figsize=(8, 5))
sns.swarmplot(x='RiskLevel', y='BMI', data=df, palette='dark')
plt.title('BMI Distribution by Risk Level (Swarm Plot)')
plt.show()

# Annotated heatmap of feature correlations
plt.figure(figsize=(10, 6))
corr_matrix = df.drop(columns=['RiskLevel']).corr()
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()
