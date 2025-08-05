### 📦 **1. Import Required Libraries**

```python
import pandas as pd
from sklearn.model_selection import train_test_split
```

* `pandas` is used for data manipulation and handling dataframes.
* `train_test_split` from `sklearn` is used to split your data into training and testing sets.

---

### 🔍 **2. Print All Column Names**

```python
print("Columns:", df.columns)
```

* This prints all the column names in your dataset (`df`) to ensure that the target column (`'Risk Level'`) exists.

---

### 🎯 **3. Define Target Column**

```python
target_column = 'Risk Level'
```

* You define the target (output) column for classification as `'Risk Level'`.

---

### 🧠 **4. Encode Categorical Target Values**

```python
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df[target_column] = le.fit_transform(df[target_column])
```

* `LabelEncoder` converts categorical labels (like `'low risk'`, `'mid risk'`, `'high risk'`) into numerical form.

  * For example:

    * `'high risk'` → 0
    * `'low risk'` → 1
    * `'mid risk'` → 2
      *(Note: the exact mapping depends on the alphabetical order of labels unless you customize it.)*

---

### 🧮 **5. Split Into Features (X) and Target (y)**

```python
X = df.drop(target_column, axis=1)
y = df[target_column]
```

* `X`: All input features (everything except `'Risk Level'`).
* `y`: Target variable (`'Risk Level'`).

---

### ✂️ **6. Split Data Into Train and Test Sets**

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2, 
    stratify=y, 
    random_state=42
)
```

* Splits the data into **80% train** and **20% test**.
* `stratify=y` ensures that all classes in `y` are **proportionally represented** in both train and test sets.
* `random_state=42` makes the split **reproducible**.

---

### 📐 **7. Print Shapes of Train and Test Sets**

```python
print("✅ Train set shape:", X_train.shape)
print("✅ Test set shape:", X_test.shape)
```

* Shows how many samples and features are in your training and testing datasets.

---

### 📊 **8. Display Class Distribution**

```python
print("\n🎯 Class distribution in Train set:")
print(y_train.value_counts(normalize=True))

print("\n🎯 Class distribution in Test set:")
print(y_test.value_counts(normalize=True))
```

* `value_counts(normalize=True)` gives the **proportion (percentage)** of each class in the train and test targets.

  * For example:

    ```
    0    0.33
    1    0.33
    2    0.34
    ```

    means classes 0, 1, 2 are approximately equally distributed.

---

### ✅ Summary:

This code:

* Checks your data columns.
* Encodes the target labels.
* Splits the dataset into training and testing while keeping the class balance.
* Prints the size and class distribution in both sets.

---
