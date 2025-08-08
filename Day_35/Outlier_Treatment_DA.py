import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# Load your dataset
df = pd.read_csv("Maternal_Health_and_high_risk_pregnancy_dataset.csv")  # Adjust path if needed

# ----------------------
# Step 1: Boxplots
# ----------------------

plt.figure(figsize=(15, 5))
for i, col in enumerate(['BMI', 'BS', 'Systolic BP']):
    plt.subplot(1, 3, i+1)
    sns.boxplot(data=df, y=col)
    plt.title(f'Boxplot of {col}')
plt.tight_layout()
plt.show()

# ----------------------
# Step 2: Z-score Method
# ----------------------

# Add z-score columns
df['BMI_z'] = zscore(df['BMI'])
df['BS_z'] = zscore(df['BS'])
df['Systolic_BP_z'] = zscore(df['Systolic BP'])

# Remove rows with extreme outliers (z-score > 3)
df_z_clean = df[(df['BMI_z'].abs() < 3) &
                (df['BS_z'].abs() < 3) &
                (df['Systolic_BP_z'].abs() < 3)]

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

# Display IQR bounds
for col in ['BMI', 'BS', 'Systolic BP']:
    low, high = iqr_bounds(col)
    print(f"{col} IQR bounds: {low:.2f} to {high:.2f}")

# ----------------------
# Step 4: Winsorization
# ----------------------

df_winsor = df.copy()
for col in ['BMI', 'BS', 'Systolic BP']:
    low, high = iqr_bounds(col)
    df_winsor[col] = df[col].clip(lower=low, upper=high)

# ----------------------
# Step 5: Plot Comparison
# ----------------------

fig, axes = plt.subplots(3, 2, figsize=(12, 10))
features = ['BMI', 'BS', 'Systolic BP']
for i, col in enumerate(features):
    sns.histplot(df[col], kde=True, ax=axes[i, 0], color='red')
    axes[i, 0].set_title(f'Original {col}')
    
    sns.histplot(df_winsor[col], kde=True, ax=axes[i, 1], color='green')
    axes[i, 1].set_title(f'Winsorized {col}')
plt.tight_layout()
plt.show()
