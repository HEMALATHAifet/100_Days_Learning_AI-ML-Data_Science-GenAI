# Day 33/100 – Advanced Visualization (DA) vs Baseline Model Building (DS)

Welcome to Day 33 of my **#100DaysOfLearning** challenge!

In this notebook, I explored both **Data Analysis** and **Data Science** perspectives using the **Maternal Health and High-Risk Pregnancy Dataset**.

---

## 🔹 Data Analysis Step 7: Advanced Visualization

To go beyond summary statistics and uncover deeper insights, I used advanced visualizations to understand the relationship between features and the target (`RiskLevel`).

### 📊 Visuals Created:

- **Pairplots**: To observe pairwise feature interactions
- **Violin Plots**: To understand distribution differences across risk levels
- **Swarm Plots**: For tightly packed individual data points
- **Annotated Heatmaps**: To visually represent correlations among features

### 🔍 Key Observations:

- **Blood Sugar (BS)** and **BMI** together show good separation between **Low** and **High Risk** levels
- **Preexisting conditions** tend to cluster around **High Risk**
- **Mental Health** shows a wide variance across all levels

### 📌 Tools Used:

```python
sns.pairplot(df, hue='RiskLevel')
sns.violinplot(x='RiskLevel', y='BS', data=df)
sns.heatmap(df.corr(), annot=True)
````

These plots help build human understanding before building any machine learning model.

---

## 🔸 Data Science Step 7: Baseline Model Building

In this step, I built my **first machine learning model** to classify pregnancy risk.

### 🤖 Model: Logistic Regression (Multiclass)

I used **Logistic Regression** as a simple baseline classifier.

### 🔧 Preprocessing Steps:

* Handled missing values using **mean imputation**
* **Standardized** features using `StandardScaler`
* Encoded `RiskLevel` using `LabelEncoder`

### 🧪 Code Snippet:

```python
model = LogisticRegression(multi_class='multinomial', max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

### ⚠️ Evaluation metrics such as confusion matrix and accuracy will be explored in **Day 34**.

---

## 🔍 Key Takeaway

| Aspect       | Data Analysis (DA)           | Data Science (DS)       |
| ------------ | ---------------------------- | ----------------------- |
| Purpose      | Understand the data visually | Build predictive models |
| Step 7 Focus | Advanced visual storytelling | Baseline model building |
| Outcome      | Human insight                | Automated understanding |

---

## 📅 Next Step: Day 34

* 🔹 Correlation Deep Dive (DA)
* 🔸 Model Evaluation & Comparison (DS)

---

## 🚀 Follow the Journey

* LinkedIn: https://www.linkedin.com/in/hemalatha-a-developer/
* Hashtag: `#100DaysOfLearning`
* Daily Updates: `Day 1 → Day 100`

---
