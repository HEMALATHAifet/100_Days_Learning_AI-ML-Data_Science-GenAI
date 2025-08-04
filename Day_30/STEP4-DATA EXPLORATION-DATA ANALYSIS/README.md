## 🧾 Full Code Breakdown + Explanation:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
```

### ✅ **This block imports the core libraries:**

* `pandas` → for handling and analyzing the dataset (`df`)
* `matplotlib.pyplot` → for creating visualizations (histograms)
* `seaborn` → for better-looking plots (you haven't used it yet here, but it's ready)
* `numpy` → for numeric operations (like skewness)

---

```python
df = pd.read_csv('preprocessed_maternal_health_data.csv')
```

### 📥 **Loads your preprocessed CSV dataset** into a DataFrame (`df`)

---

```python
print("🔹 Summary Statistics:\n")
print(df.describe())
```

### 📊 **Displays basic summary statistics for each numeric column:**

* **Count**, **mean**, **std**, **min**, **25%**, **50%**, **75%**, **max**
* Helps you quickly understand:

  * What is the average BMI?
  * What is the range of Systolic/Diastolic BP?
  * Are there extreme values (outliers)?

---

```python
print("🔹 Missing Values:\n")
print(df.isnull().sum())
```

### 🩹 **Checks for missing values in each column**

* Ensures your **cleaned data is truly clean**
* Important before modeling — missing data can crash ML models

---

```python
df.hist(figsize=(14, 10), bins=20, edgecolor='black')
plt.suptitle("📊 Distribution of Numerical Features", fontsize=16)
plt.tight_layout()
plt.subplots_adjust(top=0.93)
plt.show()
```

### 📈 **Creates histograms for all numeric features:**

* Shows **how each variable is distributed**
* Helps you spot:

  * Skewed data (e.g., BMI concentrated in one range)
  * Outliers (e.g., a few high BS or BP values)
  * Uniform vs. normal vs. right/left-skewed distributions

📌 `bins=20` → breaks data into 20 groups
📌 `edgecolor='black'` → adds borders to bars for clarity

---

```python
print("🔹 Skewness of Numerical Features:\n")
skew_values = df.select_dtypes(include='number').skew()
print(skew_values)
```

### ➿ **Checks Skewness of each numeric column:**

* Skewness tells you if the data is:

  * **0** → Symmetrical (normal distribution)
  * **> 0** → Right-skewed (tail on the right)
  * **< 0** → Left-skewed (tail on the left)

🎯 Why it matters:
Skewed data often needs **transformation** (e.g., log or sqrt) before modeling.

---

## ✅ Summary of What You Achieved:

| Step                | Insight You Get                |
| ------------------- | ------------------------------ |
| `df.describe()`     | Data range, central tendency   |
| `df.isnull().sum()` | Confirms clean data            |
| `df.hist()`         | Variable distributions         |
| `df.skew()`         | Normality or skewness patterns |

---
