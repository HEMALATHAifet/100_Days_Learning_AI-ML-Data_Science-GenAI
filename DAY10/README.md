# ☕ DAY10 – Cafe Sales Data Cleaning & Handling Missing Values

This project focuses on **handling missing values** and **cleaning a messy real-world dataset** using Python, Pandas, and NumPy. It includes explanations, visualizations, sample fixes, and a cleaned dataset.

---

## 📂 Folder Structure

| File Name                  | Description                                     |
|----------------------------|-------------------------------------------------|
| `Handling_Missing_Values.py` | Python script for cleaning the dataset         |
| `cleaned_cafe_sales.csv`     | Final cleaned dataset (ready for analysis)      |
| `README.md`                  | Complete documentation for the project          |

---

## 📌 Dataset Source

Dirty dataset from Kaggle:  
🔗 [Cafe Sales Dirty Data – Ahmed Mohamed (Kaggle)](https://www.kaggle.com/datasets/ahmedmohamed2003/cafe-sales-dirty-data-for-cleaning-training)

---

## ✅ Objective

To clean and preprocess the dataset so it is ready for:
- Data Analysis
- Dashboarding
- Machine Learning Models

---

## 🧠 What Are Missing Values?

Missing values are data points that are **not stored** (i.e., blank, null, NaN) in your dataset. These can occur due to:

- **Human errors** in data entry
- **Data corruption**
- **System issues**
- **Non-response** in surveys

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
````

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

### 1. Remove Missing Data

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

### 2. Impute Missing Data

#### a. Fill with Mean / Median / Mode (for numerical data)

```python
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].median(), inplace=True)
```

#### b. Fill with Mode (for categorical data)

```python
df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)
```

#### c. Forward or Backward Fill (Time Series Data)

```python
df.fillna(method='ffill', inplace=True)  # forward fill
df.fillna(method='bfill', inplace=True)  # backward fill
```

#### d. Custom Imputation

```python
df['Column'].fillna(0, inplace=True)  # replace with constant
```

---

### 3. Advanced Techniques (Machine Learning Based)

Use **KNN Imputer**, **Iterative Imputer**, or regression models.

```python
from sklearn.impute import KNNImputer

imputer = KNNImputer(n_neighbors=3)
df_imputed = imputer.fit_transform(df)
```

---

## 📋 Cleaning Plan

The dataset has **10,000 rows and 8 columns**, with several missing and inconsistent values.

| Column             | Issue Detected                      | Cleaning Applied                     |
| ------------------ | ----------------------------------- | ------------------------------------ |
| `Item`             | 333 missing values                  | Fill with `'Unknown'`                |
| `Quantity`         | 138 missing; stored as object       | Convert to numeric, fill with median |
| `Price Per Unit`   | 179 missing; stored as object       | Convert to float, fill with median   |
| `Total Spent`      | 173 missing; contains `'ERROR'`     | Replace "ERROR", recalculate         |
| `Payment Method`   | 2,579 missing; contains `'UNKNOWN'` | Replace missing/UNKNOWN with mode    |
| `Location`         | 3,265 missing; contains `'UNKNOWN'` | Fill with `'Unknown'`                |
| `Transaction Date` | 159 missing                         | Fill using forward fill (`ffill`)    |
| `Transaction ID`   | ✅ No issues                         | No action needed                     |

---

## 🔁 Sample Input vs Output

### 🔹 1. Missing Categorical Value – `Item`

**Before Cleaning**

| Transaction ID | Item  |
| -------------- | ----- |
| TXN\_000123    | *NaN* |

**After Cleaning**

| Transaction ID | Item    |
| -------------- | ------- |
| TXN\_000123    | Unknown |

---

### 🔹 2. Invalid `Quantity` Format

**Before Cleaning**

| Quantity |
| -------- |
| "4"      |
| *NaN*    |

**After Cleaning**

| Quantity                   |
| -------------------------- |
| 4.0                        |
| 2.0 *(filled with median)* |

---

### 🔹 3. `Total Spent` Has ERROR

**Before Cleaning**

| Quantity | Price Per Unit | Total Spent |
| -------- | -------------- | ----------- |
| 4        | 1.0            | ERROR       |

**After Cleaning**

| Quantity | Price Per Unit | Total Spent |
| -------- | -------------- | ----------- |
| 4        | 1.0            | 4.0         |

---

### 🔹 4. `Payment Method` Missing or UNKNOWN

**Before Cleaning**

| Payment Method |
| -------------- |
| UNKNOWN        |
| *NaN*          |

**After Cleaning**

| Payment Method       |
| -------------------- |
| Credit Card *(mode)* |

---

### 🔹 5. `Location` UNKNOWN/Missing

**Before Cleaning**

| Location |
| -------- |
| UNKNOWN  |
| *NaN*    |

**After Cleaning**

| Location |
| -------- |
| Unknown  |

---

### 🔹 6. Missing `Transaction Date`

**Before Cleaning**

| Transaction Date |
| ---------------- |
| *NaN*            |

**After Cleaning**

| Transaction Date     |
| -------------------- |
| 2023-05-11 *(ffill)* |

---

## 📊 Final Output Sample

| Transaction ID | Item   | Quantity | Price Per Unit | Total Spent | Payment Method | Location | Transaction Date |
| -------------- | ------ | -------- | -------------- | ----------- | -------------- | -------- | ---------------- |
| TXN\_1961373   | Coffee | 2.0      | 2.0            | 4.0         | Credit Card    | Takeaway | 2023-09-08       |

---

## ▶️ How to Run in Google Colab

1. Open the `.py` file or notebook in Google Colab
2. Upload `dirty_cafe_sales.csv` when prompted
3. Run all cells
4. Download the cleaned dataset (`cleaned_cafe_sales.csv`)

---
