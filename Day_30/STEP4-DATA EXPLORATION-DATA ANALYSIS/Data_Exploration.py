import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# Load the cleaned dataset
df = pd.read_csv('preprocessed_maternal_health_data.csv')
print("🔹 Summary Statistics:\n")
print(df.describe())
print("🔹 Missing Values:\n")
print(df.isnull().sum())
df.hist(figsize=(14, 10), bins=20, edgecolor='black')
plt.suptitle("📊 Distribution of Numerical Features", fontsize=16)
plt.tight_layout()
plt.subplots_adjust(top=0.93)
plt.show()
print("🔹 Skewness of Numerical Features:\n")
skew_values = df.select_dtypes(include='number').skew()
print(skew_values)
