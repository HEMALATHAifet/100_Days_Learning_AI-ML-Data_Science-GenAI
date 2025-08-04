# 🤖 Step 3 – Data Preprocessing (Data Science)

This step prepares the cleaned maternal health dataset for machine learning models by making the data machine-readable, scaled, and suitable for modeling.

---

## 📁 Input

- `cleaned_maternal_health_data.csv`  
  (Output from Step 2: Data Cleaning)

---

## ✅ Objectives

- Encode the categorical target (`Risk Level`)
- Standardize numerical features for uniform scale
- Check class balance before modeling
- Save the final preprocessed dataset

---

## ⚙️ Steps Performed

### 1. 🔠 Encode Target Variable

We mapped the `Risk Level` column as follows:

| Original Label | Encoded Value |
|----------------|----------------|
| Low Risk       | 0              |
| Mid Risk       | 1              |
| High Risk      | 2              |

```python
risk_map = {'Low Risk': 0, 'Mid Risk': 1, 'High Risk': 2}
df['Risk Level'] = df['Risk Level'].map(risk_map)
````

---

### 2. 📏 Feature Scaling using StandardScaler

All numeric columns were standardized to have **mean = 0** and **standard deviation = 1**, which helps machine learning models perform better.

```python
from sklearn.preprocessing import StandardScaler

features = ['Age', 'Systolic BP', 'Diastolic', 'BS', 'Body Temp', 'BMI', 'Heart Rate']
scaler = StandardScaler()
df[features] = scaler.fit_transform(df[features])
```

---

### 3. 📊 Class Distribution Check

We checked the balance of classes in the `Risk Level` column.

```python
print(df['Risk Level'].value_counts(normalize=True))
```

This helps us understand if the model needs balancing techniques (e.g., SMOTE, class weights) during training.

---

### 4. 💾 Save Preprocessed Dataset

We saved the final output as:

```python
df.to_csv('preprocessed_maternal_health_data.csv', index=False)
```

---

## 📦 Output

* `preprocessed_maternal_health_data.csv`
  → Scaled and encoded dataset ready for modeling

---

## 🛠️ Tools Used

* `pandas` → Data loading, mapping, saving
* `scikit-learn` (`StandardScaler`) → Feature scaling

---

## 🔜 Next Step

➡️ **Step 4: Data Exploration & EDA (Day 30)**
Understand relationships, patterns, and trends in the data visually.

---

## 💡 Author

**A. Hemalatha**

#100DaysOfLearning | Data Science | AI/ML Enthusiast

---

## 🔖 Tags

`#DataPreprocessing` `#StandardScaler` `#LabelEncoding` `#MaternalHealth` `#MachineLearning` `#DataScience` `#100DaysChallenge` `#Python`
---
