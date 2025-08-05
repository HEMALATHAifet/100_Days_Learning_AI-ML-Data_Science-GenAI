import pandas as pd
from sklearn.model_selection import train_test_split

# Check target column
print("Columns:", df.columns)

# If the target is named differently, update this accordingly
target_column = 'Risk Level'

# Encode target column if it's categorical
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df[target_column] = le.fit_transform(df[target_column])  # e.g., low=1, mid=2, high=0 (may vary)

# Split features and target
X = df.drop(target_column, axis=1)
y = df[target_column]

# Split the dataset into train and test sets (80/20) with stratification
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2, 
    stratify=y, 
    random_state=42
)

# Display shapes
print("✅ Train set shape:", X_train.shape)
print("✅ Test set shape:", X_test.shape)

# Check class distribution in both sets
print("\n🎯 Class distribution in Train set:")
print(y_train.value_counts(normalize=True))

print("\n🎯 Class distribution in Test set:")
print(y_test.value_counts(normalize=True))
