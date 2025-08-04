import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Maternal_Health_and_high_risk_pregnancy_dataset.csv') 

# Check for missing values
print("Missing Values:\n", df.isnull().sum())

# Impute missing numerical values with mean
num_cols = ['Systolic BP', 'Diastolic', 'BS', 'BMI', 'Heart Rate']
for col in num_cols:
    df[col].fillna(df[col].mean(), inplace=True)

# Impute categorical/boolean with mode
cat_cols = ['Previous Complications', 'Preexisting Diabetes']
for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Drop rows where target variable is missing
df.dropna(subset=['Risk Level'], inplace=True)

# Check again
print("Missing Values After Cleaning:\n", df.isnull().sum())

# Outlier Detection – Box plots
plt.figure(figsize=(10, 5))
sns.boxplot(data=df[['BMI', 'Systolic BP', 'Diastolic']])
plt.title('Box Plot for Outlier Detection')
plt.show()

# Flag high BMI values for review
outliers_bmi = df[df['BMI'] > 50]
print("\nUnusual BMI Values:\n", outliers_bmi)

# Save cleaned dataset to a new CSV file
df.to_csv('cleaned_maternal_health_data.csv', index=False)

print("✅ Cleaned dataset saved successfully as 'cleaned_maternal_health_data.csv'")
