### 📦 **1. Importing Required Libraries**

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

* `pandas`: used for data manipulation and analysis (like loading the dataset, filtering).
* `matplotlib.pyplot`: used for creating plots.
* `seaborn`: built on top of matplotlib, used for more attractive and informative statistical plots.

---

### 📥 **2. Load Dataset**

```python
df = pd.read_csv("preprocessed_maternal_health_data.csv")
```

* Loads your preprocessed maternal health dataset into a DataFrame called `df`.

---

### 🎨 **3. Set Plot Style**

```python
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
```

* Sets the visual style to `whitegrid`, which gives a clean background with gridlines.
* Sets the default figure size (width=10 inches, height=6 inches) for the plots.

---

### 🔶 **4. Correlation Heatmap**

```python
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("🔍 Correlation Heatmap of Features")
plt.tight_layout()
plt.show()
```

* `df.corr()`: calculates correlation between numeric features.
* `sns.heatmap(...)`: creates a heatmap showing how strongly features are related (from -1 to 1).
* `annot=True`: displays the correlation value in each cell.
* `cmap="coolwarm"`: uses a color range from blue to red for low to high correlation.
* `plt.tight_layout()`: adjusts spacing so labels don't get cut off.
* `plt.show()`: displays the plot.

---

### 🥧 **5. Pie Chart for Risk Levels**

```python
plt.figure(figsize=(6, 6))
df['RiskLevel'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, shadow=True)
plt.title("⚠️ Risk Level Distribution")
plt.ylabel("")  # Hide y-label
plt.show()
```

* `df['RiskLevel'].value_counts()`: counts how many records fall under each risk level (e.g., low, mid, high).
* `.plot.pie(...)`: makes a pie chart from those counts.
* `autopct='%1.1f%%'`: shows percentage on each slice.
* `startangle=90`: rotates the pie for better layout.
* `shadow=True`: adds a shadow effect.
* `plt.ylabel("")`: removes the y-axis label.

---

### 📊 **6. Boxplots: Feature vs Risk Level**

```python
num_cols = ['Age', 'Systolic BP', 'Diastolic', 'BS', 'BodyTemp', 'HeartRate']
```

* This line lists the numerical features to be compared with `RiskLevel`.

```python
for col in num_cols:
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x='RiskLevel', y=col, palette='Set2')
    plt.title(f"{col} vs Risk Level")
    plt.show()
```

* Loops through each numerical feature and:

  * Creates a boxplot comparing distribution across risk levels.
  * `palette='Set2'`: chooses a specific color scheme.
  * `x='RiskLevel'`: risk categories on x-axis.
  * `y=col`: current feature on y-axis.

---

### 📉 **7. High Risk + High BP/BS % Calculation**

```python
high_risk_df = df[df['RiskLevel'] == 'high risk']
```

* Filters only the rows where RiskLevel is "high risk".

```python
high_bp_diabetes = high_risk_df[(high_risk_df['Systolic BP'] > 140) | (high_risk_df['BS'] > 120)]
```

* From high-risk data, filters further where:

  * `Systolic BP` > 140 **or**
  * `Blood Sugar (BS)` > 120

```python
percent = (len(high_bp_diabetes) / len(high_risk_df)) * 100
print(f"✅ Percentage of high-risk pregnancies with high BP or diabetes: {percent:.2f}%")
```

* Calculates the **percentage** of such patients and prints it with 2 decimal points.

---

### ⚖️ **8. BMI > 35 in High Risk Group**

```python
if 'BMI' in df.columns:
    high_bmi = df[df['BMI'] > 35]
    print(f"💡 Number of records with BMI > 35: {len(high_bmi)}")
```

* Checks if the `BMI` column exists.
* Filters rows where BMI > 35.
* Prints the **number** of such records.

---

### 🧠 **9. Mental Health Variance by Risk Level**

```python
if 'MentalHealth' in df.columns:
    print("📊 Mental Health Variance by Risk Level:")
    print(df.groupby('RiskLevel')['MentalHealth'].describe())
```

* If the `MentalHealth` column exists:

  * Groups data by `RiskLevel`.
  * Shows **summary statistics** (count, mean, std, min, max, etc.) for Mental Health score within each group.

---
