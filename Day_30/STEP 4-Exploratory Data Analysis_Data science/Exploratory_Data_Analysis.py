import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load preprocessed dataset
df = pd.read_csv("preprocessed_maternal_health_data.csv")

plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("🔍 Correlation Heatmap of Features")
plt.tight_layout()
plt.show()

df.hist(figsize=(14, 10), bins=20, edgecolor='black')
plt.suptitle("📊 Distribution of Numerical Features", fontsize=16)
plt.tight_layout()
plt.subplots_adjust(top=0.93)
plt.show()

sns.violinplot(x='BS', data=df, inner='quartile', color='violet')
plt.title("BS Distribution (Violin Plot)")
plt.show()

plt.figure(figsize=(8, 4))
sns.histplot(df['BMI'], kde=True, color='orange', bins=20)
plt.title("BMI Distribution with KDE")
plt.xlabel("BMI")
plt.ylabel("Density")
plt.show()

print(df.columns)
