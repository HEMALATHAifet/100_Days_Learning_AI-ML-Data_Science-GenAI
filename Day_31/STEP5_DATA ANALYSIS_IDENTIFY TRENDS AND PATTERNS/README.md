## ✅ Libraries Used

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
```

**Explanation:**

* `pandas` is used to load and handle tabular data (`.csv` files).
* `seaborn` is used for easy and attractive statistical plots.
* `matplotlib.pyplot` is used to display and save plots.
* `numpy` is used for numerical operations, here to generate fake labels.

---

## ✅ Load the Dataset

```python
df = pd.read_csv("preprocessed_maternal_health_data.csv")
```

**Explanation:**
Loads your preprocessed CSV dataset into a DataFrame named `df`. This dataset contains standardized or scaled health data of pregnant women.

---

## ✅ Step 1: Assign Risk Levels (for visualization only)

```python
np.random.seed(42)
df['Risk Level'] = np.random.choice(['Low', 'Mid', 'High'], size=len(df))
```

**Explanation:**
Since your dataset has no `Risk Level` labels (all are missing), this code assigns random labels: `Low`, `Mid`, or `High`, just for visualization purposes.

* `np.random.seed(42)` ensures the results are repeatable.
* `np.random.choice(..., size=len(df))` generates one risk level per row.

---

## ✅ Step 2: Boxplot – BMI vs Risk Level

```python
plt.figure(figsize=(8, 5))
sns.boxplot(x='Risk Level', y='BMI', data=df)
plt.title("BMI Distribution by Risk Level")
plt.tight_layout()
plt.show()
```

**Explanation:**

* Draws a **boxplot** of BMI for each `Risk Level`.
* A boxplot shows:

  * Median (middle line),
  * Quartiles (box edges),
  * Outliers (dots).
* Helps you see if **BMI increases with risk level**.

---

## ✅ Step 2 (continued): Boxplot – Systolic BP vs Risk Level

```python
plt.figure(figsize=(8, 5))
sns.boxplot(x='Risk Level', y='Systolic BP', data=df)
plt.title("Systolic BP Distribution by Risk Level")
plt.tight_layout()
plt.show()
```

**Explanation:**

* Similar to BMI, this boxplot shows **Systolic Blood Pressure** distributions across risk groups.
* High systolic BP may indicate pregnancy complications.

---

## ✅ Step 3: Countplot – Preexisting Diabetes per Risk Level

```python
plt.figure(figsize=(8, 5))
sns.countplot(x='Risk Level', hue='Preexisting Diabetes', data=df)
plt.title("Preexisting Diabetes across Risk Levels")
plt.tight_layout()
plt.show()
```

**Explanation:**

* This countplot shows **number of patients with and without diabetes** (`0` or `1`) for each risk level.
* `hue='Preexisting Diabetes'` splits the bars by diabetes status.
* Reveals whether high-risk groups have more diabetic patients.

---

## ✅ Step 4: Proportion Plot – Mental Health Distribution

### First, calculate proportions:

```python
prop_df = pd.crosstab(df['Risk Level'], df['Mental Health'], normalize='index')
```

**Explanation:**

* `pd.crosstab()` creates a frequency table of `Mental Health` values (`0` or `1`) grouped by `Risk Level`.
* `normalize='index'` converts counts to **percentages** within each risk group.

---

### Then, plot stacked bar chart:

```python
prop_df.plot(kind='bar', stacked=True, colormap='coolwarm')
plt.title("Proportion of Mental Health Scores by Risk Level")
plt.ylabel("Proportion")
plt.xlabel("Risk Level")
plt.legend(title="Mental Health", labels=["Low (0)", "High (1)"])
plt.tight_layout()
plt.show()
```

**Explanation:**

* `stacked=True` stacks bars for `Mental Health = 0` and `1`.
* Shows what percentage of people in each risk level had low or high mental health.
* Uses a **colorful stacked bar chart** for clear visual comparison.

---

### 🔚 Summary

| Step | Task                           | Purpose                                                  |
| ---- | ------------------------------ | -------------------------------------------------------- |
| 1    | Assign random Risk Levels      | Enable plotting (original data had missing `Risk Level`) |
| 2    | Plot BMI & BP distributions    | Find trends in physical health indicators by risk        |
| 3    | Plot diabetes distribution     | Understand how diabetes correlates with pregnancy risk   |
| 4    | Plot mental health proportions | Show how psychological health varies by risk level       |

---
