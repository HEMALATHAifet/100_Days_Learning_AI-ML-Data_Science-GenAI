## ✅ What Are Missing Values?

Missing values are data points that are **not stored** (i.e., blank, null, NaN) in your dataset. These can occur due to:

* **Human errors** in data entry
* **Data corruption**
* **System issues**
* **Non-response** in surveys

---

## 🔍 How to Know If Data Is Missing

In Python using `pandas`:

```python
import pandas as pd

# Load your data
df = pd.read_csv("your_data.csv")

# Summary of missing values
print(df.isnull().sum())

# Total number of missing values
print(df.isnull().sum().sum())

# Percentage of missing values
missing_percentage = df.isnull().mean() * 100
print(missing_percentage)
```

You can also **visualize** missing data using:

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.show()
```

---

## 🧠 Why Handling Missing Values Is Important

1. **Algorithms can't handle NaNs** – Most ML models will throw errors.
2. **Biased results** – Missing data can distort your conclusions.
3. **Loss of information** – Ignoring missing values may reduce data size unnecessarily.
4. **Impacts model accuracy** – Poor handling leads to underperforming models.

---

## 🛠️ How to Handle Missing Values

### 1. **Remove Missing Data**

* **Remove rows**

  ```python
  df.dropna(inplace=True)
  ```
* **Remove columns**

  ```python
  df.dropna(axis=1, inplace=True)
  ```

📝 Use this only when the amount of missing data is **very small**.

---

### 2. **Impute Missing Data**

#### a. **Fill with Mean / Median / Mode (for numerical data)**

```python
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].median(), inplace=True)
```

#### b. **Fill with Mode (for categorical data)**

```python
df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)
```

#### c. **Forward or Backward Fill (Time Series Data)**

```python
df.fillna(method='ffill', inplace=True)  # forward fill
df.fillna(method='bfill', inplace=True)  # backward fill
```

#### d. **Custom Imputation**

```python
df['Column'].fillna(0, inplace=True)  # replace with constant
```

---

### 3. **Advanced Techniques (Machine Learning Based)**

* Use **KNN Imputer**, **Iterative Imputer**, or regression models.

```python
from sklearn.impute import KNNImputer

imputer = KNNImputer(n_neighbors=3)
df_imputed = imputer.fit_transform(df)
```

---

## 📋 Best Practices

| Situation     | Recommended Action                              |
| ------------- | ----------------------------------------------- |
| <5% missing   | Drop rows                                       |
| 5-30% missing | Impute (mean/median/mode)                       |
| >30% missing  | Consider dropping column or advanced imputation |

---

## 📌 Summary Steps for Handling Missing Values

1. **Identify missing values** using `.isnull()` or `.info()`
2. **Understand** the nature and cause of the missing data
3. **Visualize** missing patterns (optional but helpful)
4. **Decide**: Drop or Impute?
5. **Apply** the chosen method
6. **Verify** that missing values are handled properly

---
