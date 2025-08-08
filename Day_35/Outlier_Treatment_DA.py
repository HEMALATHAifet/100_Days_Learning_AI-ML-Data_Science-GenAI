import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# Load your dataset
df = pd.read_csv("Maternal_Health_and_high_risk_pregnancy_dataset.csv")  # Replace with your actual path

# ----------------------
# Step 1: Visual Inspection (Boxplots)
# ----------------------

plt.figure(figsize=(15, 5))
for i, col in enumerate(['BMI', 'BS', 'SystolicBP']):
    plt.subplot(1, 3, i+1)
    sns.boxplot(data=df, y=col)
    plt.title(f'Boxplot of {col}')
plt.tight_layout()
plt.show()

# ----------------------
# Step 2: Z-score Method
# ----------------------

# Add z-scores
df['BMI_z'] = zscore(df['BMI'])
df['BS_z'] = zscore(df['BS'])
df['SystolicBP_z'] = zscore(df['SystolicBP'])

# Filter rows with z < 3 (removes extreme outliers)
df_z_clean = df[(df['BMI_z'].abs() < 3) & 
                (df['BS_z'].abs() < 3) & 
                (df['SystolicBP_z'].abs() < 3)]

# ----------------------
# Step 3: IQR Method
# ----------------------

def iqr_bounds(column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return lower, upper

for col in ['BMI', 'BS', 'SystolicBP']:
    low, high = iqr_bounds(col)
    print(f"{col} bounds: {low:.2f} to {high:.2f}")

# Create a capped version using Winsorization
df_winsor = df.copy()
for col in ['BMI', 'BS', 'SystolicBP']:
    low, high = iqr_bounds(col)
    df_winsor[col] = df[col].clip(lower=low, upper=high)

# ----------------------
# Optional: Compare Distributions
# ----------------------

fig, axes = plt.subplots(3, 2, figsize=(12, 10))
features = ['BMI', 'BS', 'SystolicBP']
for i, col in enumerate(features):
    sns.histplot(df[col], kde=True, ax=axes[i, 0], color='red')
    axes[i, 0].set_title(f'Original {col}')
    
    sns.histplot(df_winsor[col], kde=True, ax=axes[i, 1], color='green')
    axes[i, 1].set_title(f'Winsorized {col}')
plt.tight_layout()
plt.show()
