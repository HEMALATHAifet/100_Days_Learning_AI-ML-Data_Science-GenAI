# 🩺 Maternal Health & High-Risk Pregnancy – DA vs DS

**Day 37/100 – #100DaysOfLearning Challenge**  
Wrapping up **Data Analysis** and **Data Science** workflows on the same healthcare dataset to compare **Insights vs Deployment Plan**.

---

## 📌 Project Overview

This project demonstrates the **key differences** between:
- **Data Analysis (DA)** – extracting insights, trends, and storytelling with data
- **Data Science (DS)** – training and deploying predictive models

The dataset used is the **Maternal Health and High-Risk Pregnancy Dataset**, focusing on features like:
- **BMI**
- **Blood Pressure**
- **Diabetes**
- **Age**
- **Risk Level**

---

## 🧪 Data Analysis (DA) Pipeline

### **Goal**
Identify patterns, trends, and key risk factors influencing high-risk pregnancies.

### **Key Steps**
1. Load and explore the dataset
2. Handle missing values and data types
3. Visualize relationships:
   - BMI vs Risk Level
   - Blood Pressure vs Risk Level
   - Diabetes & BMI by Risk Level
4. Generate summary statistics
5. Derive actionable healthcare insights

### **Tools Used**
- Python (`pandas`, `matplotlib`, `seaborn`)

---

## 🤖 Data Science (DS) Pipeline

### **Goal**
Build and save a **Random Forest Classifier** to predict pregnancy risk levels based on patient health data.

### **Key Steps**
1. Encode categorical variables (Risk Level)
2. Split into training & test sets
3. Train Random Forest Classifier
4. Evaluate performance (accuracy, classification report, confusion matrix)
5. Save model & label encoder with `joblib`
6. Prepare for deployment in **Gradio**, **Streamlit**, or **Flask**

### **Tools Used**
- Python (`pandas`, `scikit-learn`, `matplotlib`, `seaborn`, `joblib`)

---

## 📊 Comparison Table

| Aspect   | Data Analysis         | Data Science             |
| -------- | --------------------- | ------------------------ |
| Output   | Key insights, trends  | Trained predictive model |
| Purpose  | Human understanding   | Machine prediction       |
| End User | Non-tech stakeholders | Technical systems/teams  |
| Tools    | Charts, summaries     | ML models, APIs          |

---

## 📂 Repository Structure

```

maternal-health-risk/
│
├── data\_analysis.py             # DA code for insights & visuals
├── data\_science.py              # DS code for model training
├── maternal\_health\_risk.csv     # Dataset (if allowed to share)
├── maternal\_health\_rf\_model.joblib    # Saved RF model
├── risk\_level\_label\_encoder.joblib    # Saved label encoder
└── README.md                    # Project documentation

````

---

## 🚀 How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YourUsername/maternal-health-risk.git
cd maternal-health-risk
````

### 2️⃣ Install dependencies

```bash
pip install pandas matplotlib seaborn scikit-learn joblib
```

### 3️⃣ Run Data Analysis

```bash
python data_analysis.py
```

### 4️⃣ Run Data Science Model Training

```bash
python data_science.py
```

---

## 📅 Next Step (Day 38)

* Build a **Gradio web app** to let users enter patient details and get **risk predictions instantly**.

---

## 📜 License

This project is licensed under the MIT License – feel free to use and adapt.

---

## ❤️ Acknowledgements

* Dataset source: [Maternal Health and High-Risk Pregnancy Dataset](https://www.kaggle.com/)
* Part of my **#100DaysOfLearning** journey

---

