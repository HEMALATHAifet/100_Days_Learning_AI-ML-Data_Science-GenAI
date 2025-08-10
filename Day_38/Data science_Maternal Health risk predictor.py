# Day 38 – Data Science Workflow: Maternal Health & High-Risk Pregnancy Dataset

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
df = pd.read_csv("Maternal_Health_and_high_risk_pregnancy_dataset.csv")

print("Dataset Shape:", df.shape)
print(df.head())

# 3️⃣ Encode categorical target variable
label_encoder = LabelEncoder()
df['Risk Level'] = label_encoder.fit_transform(df['Risk Level'])
# Low=1, Medium=2, High=0 (example — will depend on encoding order)

# 4️⃣ Split features & target
X = df.drop(columns=['Risk Level'])
y = df['Risk Level']

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




# Day 38 – Gradio Deployment of Maternal Health Risk Predictor

import gradio as gr
import pandas as pd
import joblib

# 1️⃣ Load model & label encoder
model = joblib.load("maternal_health_rf_model.joblib")
label_encoder = joblib.load("risk_level_label_encoder.joblib")

# 2️⃣ Define prediction function
def predict_risk(age, systolic_bp, diastolic_bp, bs, body_temp, bmi, prev_comp, pre_diab, gest_diab, mental_health, heart_rate):
    # Arrange inputs into DataFrame (must match training order)
    input_df = pd.DataFrame([[age, systolic_bp, diastolic_bp, bs, body_temp, bmi,
                              prev_comp, pre_diab, gest_diab, mental_health, heart_rate]],
                            columns=[
                                "Age", "Systolic BP", "Diastolic", "BS", "Body Temp", "BMI",
                                "Previous Complications", "Preexisting Diabetes", "Gestational Diabetes",
                                "Mental Health", "Heart Rate"
                            ])

    # Predict encoded risk level
    prediction_encoded = model.predict(input_df)[0]

    # Decode back to original labels
    prediction_label = label_encoder.inverse_transform([prediction_encoded])[0]

    return f"Predicted Risk Level: {prediction_label}"

# 3️⃣ Define Gradio inputs
inputs = [
    gr.Number(label="Age"),
    gr.Number(label="Systolic BP"),
    gr.Number(label="Diastolic BP"),
    gr.Number(label="Blood Sugar"),
    gr.Number(label="Body Temperature"),
    gr.Number(label="BMI"),
    gr.Number(label="Previous Complications (0=No, 1=Yes)"),
    gr.Number(label="Preexisting Diabetes (0=No, 1=Yes)"),
    gr.Number(label="Gestational Diabetes (0=No, 1=Yes)"),
    gr.Number(label="Mental Health Score"),
    gr.Number(label="Heart Rate"),
]

# 4️⃣ Output
output = gr.Textbox(label="Risk Prediction")

# 5️⃣ Interface
app = gr.Interface(
    fn=predict_risk,
    inputs=inputs,
    outputs=output,
    title="Maternal Health Risk Predictor",
    description="Enter patient details to predict pregnancy risk level."
)

# 6️⃣ Launch
app.launch()
