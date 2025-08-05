import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load preprocessed dataset
df = pd.read_csv("preprocessed_maternal_health_data.csv")

# Set plot style
sns.set(style="whitegrid")

import numpy as np
# Temporarily assign fake risk levels for demo purposes only
np.random.seed(42)  # for reproducibility
df['Risk Level'] = np.random.choice(['Low', 'Mid', 'High'], size=len(df))

# 1. Boxplot: BMI vs Risk_Level
plt.figure(figsize=(8, 5))
sns.boxplot(x='Risk Level', y='BMI', data=df)
plt.title("BMI Distribution by Risk Level")
plt.tight_layout()
plt.show()

# 2. Boxplot: Systolic BP vs Risk_Level
plt.figure(figsize=(8, 5))
sns.boxplot(x='Risk Level', y='Systolic BP', data=df)
plt.title("Systolic BP Distribution by Risk Level")
plt.tight_layout()
plt.show()


# 3. Countplot: Preexisting Diabetes across Risk Levels
plt.figure(figsize=(8, 5))
sns.countplot(x='Risk Level', hue='Preexisting Diabetes', data=df)
plt.title("Preexisting Diabetes across Risk Levels")
plt.tight_layout()
plt.show()

# Check distribution of Mental_Health across Risk Levels
df.groupby("Risk Level")["Mental Health"].value_counts(normalize=True)

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create a crosstab of proportions
prop_df = pd.crosstab(df['Risk Level'], df['Mental Health'], normalize='index')

# 4. Plot stacked bar chart
prop_df.plot(kind='bar', stacked=True, colormap='coolwarm')
plt.title("Proportion of Mental Health Scores by Risk Level")
plt.ylabel("Proportion")
plt.xlabel("Risk Level")
plt.legend(title="Mental Health", labels=["Low (0)", "High (1)"])
plt.tight_layout()
plt.show()
