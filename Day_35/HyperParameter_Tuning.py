import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Maternal_Health_and_high_risk_pregnancy_dataset.csv")  # Update path if needed

# ----------------------
# Step 1: Prepare Features and Target
# ----------------------

X = df.drop(columns=["Risk Level"])  # Assuming RiskLevel is the target column
y = df["Risk Level"]

# Optional: Encode categorical features if any (like RiskLevel if not numeric)
# If RiskLevel is categorical like 'low', 'mid', 'high'
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# ----------------------
# Step 2: Grid Search for Random Forest
# ----------------------

params = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 5, 10],
    'min_samples_split': [2, 5]
}

grid = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_grid=params,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

grid.fit(X_train, y_train)

print("✅ Best Parameters:", grid.best_params_)

# ----------------------
# Step 3: Evaluate Best Model
# ----------------------
from sklearn.metrics import classification_report

# Ensure all three labels are reported: 0 (High), 1 (Low), 2 (Mid)
# Check your label mapping:
print(le.classes_)  # Should be ['high', 'low', 'mid']

# Map correctly
label_order = [0, 1, 2]  # order matches encoded labels: ['high', 'low', 'mid']
class_names = ['High', 'Low', 'Mid']  # Display names in same order

# Avoid error if some labels are missing in predictions
print(classification_report(y_test, y_pred, labels=label_order, target_names=class_names, zero_division=0))


# ----------------------
# Step 4: Confusion Matrix
# ----------------------

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=le.classes_, yticklabels=le.classes_)
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
