# 📊 Automated Data Quality Checker (Python)

A simple yet powerful Python script to **automatically analyze data quality issues** in any dataset (CSV/Excel).
This project helps data analysts save time by identifying common problems before analysis.

---

## 🚀 Why This Project?

In real-world data analysis, data is rarely clean.

Before doing any analysis, we must check:

* Missing values
* Duplicate records
* Incorrect data types
* Outliers

Doing this manually is time-consuming.
This project **automates the entire process**.

---

## 🛠️ Tools Used

* Python
* Pandas
* Matplotlib

---

## 📂 How It Works

### 🔹 1. Import Libraries

```python
import pandas as pd
import matplotlib.pyplot as plt
```

### ✅ Why?

* `pandas` → used for data manipulation and analysis
* `matplotlib` → used for visualization

### 📌 When to use?

Whenever you are working with structured data (Excel, CSV, databases)

---

### 🔹 2. Load Dataset

```python
file_path = "salesforcourse-4fe2kehu.csv"

if file_path.endswith(".csv"):
    df = pd.read_csv(file_path)
else:
    df = pd.read_excel(file_path)
```

### ✅ Why?

* Automatically detects file type (CSV or Excel)
* Makes the script reusable for different datasets

### 📌 Practical Example:

You receive:

* Sales data in CSV
* Finance data in Excel

Same script works for both ✔

---

### 🔹 3. Check Missing Values

```python
missing = df.isnull().sum()
```

### ✅ Why?

Missing values can break analysis or give wrong insights.

### 📌 Practical Example:

* Customer age is missing → affects segmentation
* Revenue column has nulls → wrong total revenue

---

### 🔹 4. Check Duplicates

```python
duplicates = df.duplicated().sum()
```

### ✅ Why?

Duplicate data leads to **double counting**

### 📌 Practical Example:

* Same order recorded twice → inflated revenue
* Duplicate customers → wrong customer count

---

### 🔹 5. Check Data Types

```python
dtypes = df.dtypes
```

### ✅ Why?

Wrong data types cause errors in calculations.

### 📌 Practical Example:

* Date stored as text → cannot filter by date
* Price stored as string → cannot sum values

---

### 🔹 6. Outlier Detection (IQR Method)

```python
outliers = {}

for col in df.select_dtypes(include='number').columns:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1

    outliers[col] = df[
        (df[col] < q1 - 1.5 * iqr) |
        (df[col] > q3 + 1.5 * iqr)
    ].shape[0]
```

### ✅ Why?

Outliers can distort analysis and models.

### 📌 Practical Example:

* Salary = 1,00,000 vs one entry = 10,00,000 → skewed average
* Sales suddenly 0 or extremely high → possible data error

---

## 📐 Outlier Formula Used

\text{Outlier if } x < Q_1 - 1.5\cdot IQR ; \text{or} ; x > Q_3 + 1.5\cdot IQR

---

### 🔹 7. Print Results

```python
print("\nMissing Values:\n", missing)
print("\nTotal Duplicates:", duplicates)
print("\nData Types:\n", dtypes)
print("\nOutliers:\n", outliers)
```

### ✅ Why?

Gives quick insights directly in console

---

### 🔹 8. Visualization

```python
missing.plot(kind='bar', title="Missing Values by Column")
plt.tight_layout()
plt.show()
```

### ✅ Why?

Visuals help quickly identify problem areas

### 📌 Practical Example:

Instead of reading numbers → instantly see which column has highest missing data

---

### 🔹 9. Export Reports

```python
with pd.ExcelWriter("data_quality_report.xlsx") as writer:
    missing.to_excel(writer, sheet_name="Missing Values")
    dtypes.to_excel(writer, sheet_name="Data Types")

pd.DataFrame.from_dict(outliers, orient='index', columns=['Outliers']) \
    .to_excel("outliers_report.xlsx")
```

### ✅ Why?

* Saves results for sharing
* Useful in business reporting

### 📌 Practical Example:

Send report to manager/stakeholders without running code again

---

## 📈 Output

The script generates:

* Console summary
* Bar chart (missing values)
* Excel reports:

  * `data_quality_report.xlsx`
  * `outliers_report.xlsx`

---

## 💡 Real-World Use Cases

* Data cleaning before Power BI dashboards
* Preparing datasets for machine learning
* Validating data received from clients
* Automating repetitive analyst tasks

---

## 🔥 Future Improvements

* Auto data cleaning (fill/remove nulls)
* SQL database integration
* Scheduled automation (daily checks)
* Dashboard integration

---

## 🙌 Conclusion

This project demonstrates how Python can:

* Save time
* Improve data accuracy
* Automate repetitive tasks

A must-have tool for every data analyst 🚀

---
