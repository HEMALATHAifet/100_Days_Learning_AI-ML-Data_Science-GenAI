# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load the dataset
df = pd.read_csv('Maternal_Health_and_high_risk_pregnancy_dataset.csv')  # Ensure correct file path or upload via Colab

# Step 3: Check the first few rows (optional)
print(df.head())

# Step 4: Compute correlation matrix
correlation_matrix = df.corr()

# Step 5: Plot the heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, fmt='.2f')
plt.title('Correlation Matrix - Maternal Health Dataset')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()
