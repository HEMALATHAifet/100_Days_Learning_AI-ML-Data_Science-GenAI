# 🤖 Day 34 – Correlation Analysis & Model Evaluation | #100DaysOfLearning

This repository contains the analysis and modeling for **Day 34** of my **#100DaysOfLearning challenge**. The focus is on:

- 📊 **Data Analysis Step 8:** Correlation Analysis  
- 📈 **Data Science Step 8:** Model Evaluation  

Dataset: [Maternal Health and High-Risk Pregnancy Dataset](https://www.kaggle.com/datasets/andrewmvd/maternal-health-risk-data)

---

## 📌 Project Overview

This project demonstrates how we can:
- Use **correlation matrices** to understand feature relationships in data
- Evaluate a **logistic regression model** using metrics like accuracy, precision, recall, and confusion matrix

---

## 🧪 Data Analysis – Step 8: Correlation Analysis

### 📈 Goal
To measure linear relationships between numeric features.

### 🧰 Tools
- `pandas`
- `matplotlib`
- `seaborn`

### 💡 Insights

* **Systolic BP vs Diastolic BP** – Strong positive correlation (as expected)
* **BMI / BS vs Risk Level** – Mild to moderate correlation
* **Mental Health** – Very low correlation with most features
* **Important** – Correlation helps understand feature redundancy & possible influence

---
### 🧠 **How to Read the Heatmap**

Each cell in the heatmap shows the **Pearson correlation coefficient (r)** between two variables:

* `+1`: perfect positive correlation
* `0`: no correlation
* `–1`: perfect negative correlation

---

### 🔍 **Typical Insights You Might Get**

#### 🔸 1. **Systolic BP vs Diastolic BP**

* Correlation: **Strong positive**
* ✅ This is expected because these are biologically related blood pressure measurements.

#### 🔸 2. **BMI vs RiskLevelEncoded**

* Correlation: **Mild to moderate positive**
* ✅ Higher BMI may be associated with higher pregnancy risk.

#### 🔸 3. **Blood Sugar (BS) vs RiskLevelEncoded**

* Correlation: **Slight positive**
* 🩸 Elevated BS might increase maternal risk but may not be a dominant factor alone.

#### 🔸 4. **Mental Health vs Other Features**

* Correlation: **Low or near 0**
* ⚠️ Suggests that **mental health is not linearly correlated** with other features or risk level. Still important clinically, but not captured well with simple correlation.

#### 🔸 5. **RiskLevelEncoded vs Others**

* Helps identify features that contribute more to the **target variable** (e.g., BMI, BS, BP values).

---

### 📌 Final Takeaway

The heatmap tells you:

* Which features are **redundant** (highly correlated with each other).
* Which features might be **good predictors** of `RiskLevel`.
* Which features are **independent**, potentially adding unique value to the model.
* Correlation is **not causation**, but it's a great first filter for feature selection or deeper analysis.



## 🤖 Data Science – Step 8: Model Evaluation

### 📈 Goal

Evaluate the performance of a logistic regression model trained to classify risk levels.

### 🧰 Tools

* `scikit-learn`
* `seaborn`
* `matplotlib`

### 💡 Evaluation Metrics

* **Accuracy:** \~87%
* **Recall (Mid Risk):** Low – a known challenge due to overlap in symptoms
* **Confusion Matrix:** Most confusion between *Mid & Low* or *Mid & High*

---

## 🔍 Key Difference

| Data Analysis                    | Data Science                       |
| -------------------------------- | ---------------------------------- |
| Understand feature relationships | Evaluate model performance         |
| Correlation ≠ Causation          | Accuracy, Recall, Confusion Matrix |
| Guides feature selection         | Tells where the model struggles    |

---

## 📌 Next Steps – Day 35

* 🧼 Data Analysis: **Outlier Treatment**
* 🔧 Data Science: **Hyperparameter Tuning**

---

## 🧵 Related Hashtags

`#100DaysOfLearning` `#DataScience` `#MachineLearning` `#Python` `#CorrelationAnalysis` `#ModelEvaluation` `#MaternalHealth` `#WomenInTech`

---



#ModelEvaluation #ConfusionMatrix #CorrelationAnalysis #MaternalHealth #PregnancyRisk #hiring #chennai #hireme #immediately #OpenToWork #DataScience #DataAnalysis #100DaysOfLearning #Python #Colab #MachineLearning #WomenInTech #Gradio
