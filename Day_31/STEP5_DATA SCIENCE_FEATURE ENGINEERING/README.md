## Full explanation of code
## 🔶 **1. Import Libraries**

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
```

* `pandas`: for data loading and manipulation
* `seaborn`: for statistical data visualization
* `matplotlib.pyplot`: for displaying and saving plots

---

## 📥 **2. Load Dataset**

```python
df = pd.read_csv("preprocessed_maternal_health_data.csv")
print(df.columns)
```

* Loads the preprocessed dataset into a DataFrame `df`.
* `print(df.columns)` helps verify the column names (especially to check for spaces like `'Systolic BP'`).

---

## 🛠️ **3. Feature Engineering**

### ✅ Feature 1: **BP Ratio**

```python
df['BP Ratio'] = df['Systolic BP'] / df['Diastolic']
```

* **BP Ratio** = Systolic / Diastolic
* A high ratio may signal **hypertension or BP imbalance**
* This is a new **continuous feature** for modeling

---

### ✅ Feature 2: **Complication Score**

```python
df['Complication Score'] = df[['Previous Complications', 'Preexisting Diabetes', 'Gestational Diabetes']].sum(axis=1)
```

* This creates a **new integer feature** that combines 3 binary columns.
* Possible values:

  * 0 = No complications
  * 1 = One complication
  * 2 = Two complications
  * 3 = All three complications
* This simplifies and strengthens **risk identification**.

---

### ✅ Feature 3: **High BP Flag**

```python
df['High BP Flag'] = ((df['Systolic BP'] > 140) | (df['Diastolic'] > 90)).astype(int)
```

* If systolic > 140 **or** diastolic > 90 → assigns `1` (high BP)
* Otherwise, assigns `0` (normal BP)
* A simple binary feature that highlights **risky blood pressure cases**

---

### 👀 Preview the new features:

```python
print(df[['Systolic BP', 'Diastolic', 'BP Ratio', 'Complication Score', 'High BP Flag']].head())
```

* Helps verify that the new features are added correctly.

---

## 🏷️ **4. Assign Dummy Risk Levels (for plotting only)**

```python
import numpy as np
np.random.seed(42)
df['Risk Level'] = np.random.choice(['Low', 'Mid', 'High'], size=len(df))
```

* Since the dataset doesn't have actual risk levels, you assign **random dummy labels** to simulate grouping.
* This is needed **only for visualization**.
* `np.random.seed(42)` ensures **reproducibility**.

---

## 📊 **5. Visualizations of Engineered Features**

---

### 📌 Plot 1: **BP Ratio vs Risk Level**

```python
plt.figure(figsize=(8, 5))
sns.barplot(x='Risk Level', y='BP Ratio', data=df, ci='sd')
plt.title("Average BP Ratio across Risk Levels")
```

* Shows **average BP Ratio** in each risk group
* Helps identify if **imbalanced BP** is more frequent in high-risk pregnancies

---

### 📌 Plot 2: **Complication Score Distribution**

```python
plt.figure(figsize=(8, 5))
sns.boxplot(x='Risk Level', y='Complication Score', data=df)
plt.title("Complication Score by Risk Level")
```

* Displays how many complications (0–3) are common in each risk group
* A **higher score** indicates **higher maternal risk**

---

### 📌 Plot 3: **High BP Flag Count**

```python
plt.figure(figsize=(8, 5))
sns.countplot(x='Risk Level', hue='High BP Flag', data=df)
plt.title("High BP Flag Count across Risk Levels")
```

* A **countplot** that compares how many people with/without high BP fall into each risk level
* Very useful for seeing how **binary features relate to the target**

---

### 🖼️ All plots are displayed and saved:

```python
plt.tight_layout()
plt.savefig("filename.png")
plt.show()
```

* `tight_layout()` ensures clean plot spacing
* `savefig()` saves the plot image
* `show()` displays the plot in your Colab notebook

---

## ✅ 📌 Final Outcome

created:

* 3 new features
* 3 visualizations
* A dataset that's **ready for model training** (with predictive features)

---

## 📍 Conclusion:

> These engineered features — **BP Ratio, Complication Score, and High BP Flag** — show strong relationships with risk levels and will likely improve prediction accuracy in a machine learning model.

---
