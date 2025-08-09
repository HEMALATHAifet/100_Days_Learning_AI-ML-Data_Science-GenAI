# Day 37 – Data Science Workflow: Maternal Health & High-Risk Pregnancy Dataset

# 1️⃣ Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# 2️⃣ Load dataset
df = pd.read_csv("maternal_health_risk.csv")

print("Dataset Shape:", df.shape)
print(df.head())

# 3️⃣ Encode categorical target variable
label_encoder = LabelEncoder()
df['RiskLevel'] = label_encoder.fit_transform(df['RiskLevel'])
# Low=1, Medium=2, High=0 (example — will depend on encoding order)

# 4️⃣ Split features & target
X = df.drop(columns=['RiskLevel'])
y = df['RiskLevel']

# 5️⃣ Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6️⃣ Train model
rf_model = RandomForestClassifier(
    n_estimators=100, random_state=42
)
rf_model.fit(X_train, y_train)

# 7️⃣ Predictions & evaluation
y_pred = rf_model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {acc*100:.2f}%")
print("\n📊 Classification Report:")
print(classification_report(y_test, y_pred))

# 8️⃣ Confusion Matrix
plt.figure(figsize=(5,4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# 9️⃣ Save the trained model
joblib.dump(rf_model, "maternal_health_rf_model.joblib")
print("💾 Model saved as maternal_health_rf_model.joblib")

# 🔟 Save the Label Encoder too (important for decoding predictions later)
joblib.dump(label_encoder, "risk_level_label_encoder.joblib")

print("\n📌 Deployment Ready!")
print("- Model and label encoder saved")
print("- Can be loaded in Gradio/Streamlit/Flask for risk assessment app")
