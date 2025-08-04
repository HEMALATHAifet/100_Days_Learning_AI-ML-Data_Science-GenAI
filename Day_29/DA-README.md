# 🧹 Data Cleaning – Maternal Health and High-Risk Pregnancy Dataset

This repository contains the data cleaning process applied to the **Maternal Health and High-Risk Pregnancy Dataset** as part of the **#100DaysOfLearning** challenge.

---

## 📁 Dataset

- **Name**: Maternal_Health_and_high_risk_pregnancy_dataset.csv
- **Source**: https://www.kaggle.com/datasets/vmohammedraiyyan/maternal-health-and-high-risk-pregnancy-dataset/data

---

## 🔍 Objective

Clean the dataset by:
- Handling missing values
- Identifying and flagging outliers
- Preparing the dataset for further analysis and machine learning

---

#### ✅ **Step-by-step Explanation of Python Code**

#### 1. **Loading the Dataset**

```python
df = pd.read_csv('Maternal_Health_and_high_risk_pregnancy_dataset.csv')
```

You are loading a CSV file into a pandas DataFrame named `df`.

---

#### 2. **Checking for Missing Values**

```python
print("Missing Values:\n", df.isnull().sum())
```

This prints the **count of missing values** for each column. You’re auditing the dataset before cleaning.

---

#### 3. **Imputing Missing Numerical Values**

```python
num_cols = ['Systolic BP', 'Diastolic', 'BS', 'BMI', 'Heart Rate']
for col in num_cols:
    df[col].fillna(df[col].mean(), inplace=True)
```

This replaces missing values in numeric columns with their **column-wise mean** (average). This is a common strategy to avoid data loss.

---

#### 4. **Imputing Missing Categorical/Boolean Values**

```python
cat_cols = ['Previous Complications', 'Preexisting Diabetes']
for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)
```

This replaces missing values in categorical columns with the **most frequent value** (mode) of each column.

---

#### 5. **Dropping Rows with Missing Target Values**

```python
df.dropna(subset=['Risk Level'], inplace=True)
```

Since `Risk Level` is your **target label** for machine learning, rows with missing values in this column are **removed entirely**, as you cannot train a model without a target label.

---

#### 6. **Checking Missing Values Again**

```python
print("Missing Values After Cleaning:\n", df.isnull().sum())
```

This confirms that all missing values have been handled.

---

#### 7. **Outlier Detection using Histogram**
📊 Visualizing BMI Distribution using histogram to see how BMI values are spread across the dataset. It shows how many people fall in each BMI range, helping to spot unusually high or low BMI values i.e., extreme values visually

(e.g., very high BMI > 50).

---

#### 8. **Flagging Unusual BMI Values**

```python
outliers_bmi = df[df['BMI'] > 50]
print("\nUnusual BMI Values:\n", outliers_bmi)
```

This step filters and displays any rows where the `BMI` is unusually high (>50), which might indicate data entry errors or actual high-risk conditions.

---

### 🎯 **What is Your Endpoint?**

Your **endpoint** (final result) is a **cleaned and preprocessed dataset** that:

* ✅ Has **no missing values**
* ✅ Has **imputed values** for numeric and categorical features
* ✅ Has **no missing target labels** (`Risk Level`)
* ✅ Is **visually examined** for outliers
* ✅ **Flags outliers** in BMI (if any)

You are now ready to:

* Perform **data exploration (DA)**
* Or begin **preprocessing for machine learning (DS)** such as encoding and scaling
---

## 📂 Output File

* `cleaned_maternal_health_data.csv`
  → Contains fully cleaned data ready for exploration and modeling.

---

## 📌 Tools Used

* Python
* pandas
* matplotlib
* seaborn
* Google Colab

---

## ✅ Next Steps

➡️ Move on to:

* **Day 30: Data Exploration & EDA**
* **Data Science: Label Encoding & Feature Scaling**

---

## 💡 Author

**A. Hemalatha**
#100DaysOfLearning | Data Science | AI/ML Enthusiast

---

## 📌 Tags

`#DataCleaning` `#MaternalHealth` `#PregnancyRisk` `#100DaysChallenge` `#DataScience` `#DataAnalysis`
---
