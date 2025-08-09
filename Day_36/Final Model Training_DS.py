# 📦 Imports
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, f1_score
import joblib
# Load dataset
df = pd.read_csv("Maternal_Health_and_high_risk_pregnancy_dataset.csv")  # Update path if needed

# Encode target variable if not already numerical
df['Risk Level'] = df['Risk Level'].map({'Low': 0, 'High': 1})  # If needed

# Define feature set and target
X = df.drop(columns=['Risk Level'])  # Features
y = df['Risk Level']                 # Target
# Check if there are NaN values in target
print("NaN count in y:", y.isna().sum())

# Drop rows with NaN in y
df = df.dropna(subset=['Risk Level'])  # replace with your target column name

# Reset index after dropping
df = df.reset_index(drop=True)

# Define X and y again
X = df.drop(columns=['Risk Level'])  # replace with your target column name
y = df['Risk Level']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
# Train the final Random Forest model with optimal hyperparameters
final_model = RandomForestClassifier(
    n_estimators=150,
    max_depth=10,
    min_samples_split=2,
    random_state=42
)

final_model.fit(X_train, y_train)
y_pred = final_model.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Accuracy: {acc*100:.2f}%")
print(f"F1 Score: {f1*100:.2f}%")


print("\nClassification Report:")
print(classification_report(y_test, y_pred))
# Load the dataset
df = pd.read_csv("Maternal_Health_and_high_risk_pregnancy_dataset.csv")

# Show all column names
print(df.columns)
joblib.dump(final_model, "pregnancy_risk_model.pkl")
print("Model saved as pregnancy_risk_model.pkl")
new_data = pd.DataFrame([{
    'Age': 28,
    'Systolic BP': 150,
    'Diastolic': 95,
    'BS': 145,
    'Body Temp': 98.6,
    'BMI': 36.5,
    'Previous Complications': 1,
    'Preexisting Diabetes': 0,
    'Gestational Diabetes': 1,
    'Mental Health': 1,
    'Heart Rate': 80
}])
prediction = final_model.predict(new_data)
print("Predicted Risk Level:", "High" if prediction[0] == 1 else "Low")
