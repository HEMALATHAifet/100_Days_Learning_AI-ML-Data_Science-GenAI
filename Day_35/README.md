# 🩺 Maternal Health Risk Prediction – Day 35 (Outlier Treatment & Hyperparameter Tuning)

Welcome to Day 35 of my [#100DaysOfLearning](https://www.linkedin.com/feed/hashtag/?keywords=100daysoflearning) challenge!  
This repository focuses on the **Maternal Health and High-Risk Pregnancy Dataset** and covers:

- 📊 **Outlier Detection & Treatment** (Data Analysis)
- 🤖 **Hyperparameter Tuning** of a Random Forest Classifier (Data Science)

---

## 📂 Dataset

The dataset used is the **Maternal Health Risk Data Set** from Kaggle/UCI, which includes the following features:

- Age
- Systolic BP
- Diastolic BP
- Blood Sugar (BS)
- Body Mass Index (BMI)
- Heart Rate
- Risk Level (Target) – `Low`, `Mid`, or `High`

---

## ✅ Data Analysis: Step 9 – Outlier Treatment

Outliers were detected and treated using:

- **Boxplots**
- **Z-score Method** (removal of extreme values)
- **IQR Rule** (winsorization for mild outliers)

### Sample Code:
```python
from scipy.stats import zscore
df['Systolic_BP_z'] = zscore(df['Systolic BP'])
df_clean = df[(df['Systolic_BP_z'].abs() < 3)]
````

Outliers were handled gently since in **healthcare data**, high/low values might be valid indicators.

---

## 🤖 Data Science: Step 9 – Hyperparameter Tuning

A **Random Forest Classifier** was tuned using `GridSearchCV`.

### Parameters Tuned:

* `n_estimators`: \[50, 100, 150]
* `max_depth`: \[None, 5, 10]
* `min_samples_split`: \[2, 5]

### Sample Code:

```python
from sklearn.model_selection import GridSearchCV

params = {
    'n_estimators': [100, 150],
    'max_depth': [5, 10],
    'min_samples_split': [2, 5]
}
grid = GridSearchCV(RandomForestClassifier(), params, cv=5)
grid.fit(X_train, y_train)
print(grid.best_params_)
```

### 🧠 Results:

* **Accuracy improved from \~71% to \~78%**
* **Recall for 'Mid Risk' improved** (critical in maternal health)

---

## 📊 Classification Report

```text
              precision    recall  f1-score   support

        High       0.80      0.89      0.84        35
         Low       0.85      0.80      0.82        30
         Mid       0.00      0.00      0.00         5

    accuracy                           0.78        70
   macro avg       0.55      0.56      0.55        70
weighted avg       0.73      0.78      0.75        70
```

> ⚠️ Note: `Mid` risk class was underrepresented and not predicted in this model. Will address class imbalance in future steps.

---

## 📈 Visuals

* Boxplots and Histograms (Before vs After Winsorization)
* Confusion Matrix
* Accuracy before vs after tuning (Coming Soon)

---

## 🚀 How to Run

```bash
# Install dependencies
pip install pandas scikit-learn seaborn matplotlib

# Run the notebook or script
python maternal_health_model.py
```

---

## 📌 Coming Up (Day 36)

* 📘 **Insight Storytelling** (Data Analysis)
* ⚙️ **Final Model Training** with tuned hyperparameters (Data Science)

---

## 🔗 Connect

* 💼 [LinkedIn](https://www.linkedin.com/in/hemalatha-a-developer/)
* 📌 Hashtags: #OutlierTreatment #HyperparameterTuning #RandomForest #DataScience #MaternalHealth #100DaysOfLearning #Python #WomenInTech

---
