# Step 1: Import libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# Step 2: Load dataset
df = pd.read_csv('Maternal_Health_and_high_risk_pregnancy_dataset.csv')

# Drop missing rows
df = df.dropna()

# Encode target
df['RiskLevelEncoded'] = df['Risk Level'].map({'Low': 0, 'Mid': 1, 'High': 2})

# Feature selection
X = df[['Age', 'Systolic BP', 'Diastolic', 'BS', 'Body Temp', 'Heart Rate']]
y = df['RiskLevelEncoded']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic Regression
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=['Low', 'High']))
