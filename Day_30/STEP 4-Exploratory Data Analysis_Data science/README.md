### ✅ Full Explanation: Line-by-Line

---

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

### 🔧 You’re importing 3 key libraries:

* `pandas` (`pd`) – for loading and handling your data
* `matplotlib.pyplot` (`plt`) – for plotting and layout control
* `seaborn` (`sns`) – for beautiful statistical plots

---

```python
df = pd.read_csv("preprocessed_maternal_health_data.csv")
```

### 📥 Load Dataset:

Loads your **cleaned/preprocessed CSV file** into a DataFrame `df`.

Now `df` contains all your pregnancy-related features like:

* Age, BP, BS, BMI, Mental Health, Heart Rate, and Risk Level, etc.

---

```python
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("🔍 Correlation Heatmap of Features")
plt.tight_layout()
plt.show()
```

### 📊 Correlation Heatmap:

* Shows how **strongly variables are related** to each other.
* For example, if **BMI** and **BS** have a high correlation, it may help your model.
* `annot=True` shows correlation values inside boxes.
* `cmap="coolwarm"` sets color scale: red (positive), blue (negative).

✅ Useful for **feature selection** in data science.

---

```python
df.hist(figsize=(14, 10), bins=20, edgecolor='black')
plt.suptitle("📊 Distribution of Numerical Features", fontsize=16)
plt.tight_layout()
plt.subplots_adjust(top=0.93)
plt.show()
```

### 📈 Histograms of All Numeric Features:

* One plot per numeric column (Age, BS, BMI, etc.)
* Helps see how values are distributed (normal, skewed, outliers).
* `bins=20` groups values into 20 bars.
* `edgecolor='black'` makes the bars easy to see.

✅ Used in **data exploration** to understand data quality.

---

```python
sns.violinplot(x='BS', data=df, inner='quartile', color='violet')
plt.title("BS Distribution (Violin Plot)")
plt.show()
```

### 🎻 Violin Plot of Blood Sugar (BS):

* Combines **boxplot** and **KDE (density)** curve.
* Shows data **spread and central tendency**.
* `inner='quartile'` draws the median and interquartile range.

✅ Used to **understand shape of a feature** and spot clusters/outliers.

---

```python
plt.figure(figsize=(8, 4))
sns.histplot(df['BMI'], kde=True, color='orange', bins=20)
plt.title("BMI Distribution with KDE")
plt.xlabel("BMI")
plt.ylabel("Density")
plt.show()
```

### 📊 Histogram + KDE for BMI:

* `histplot()` makes a histogram.
* `kde=True` adds a smooth curve to show **probability density**.
* Great for understanding how BMI is distributed.

✅ Helps decide whether **scaling or transformation** is needed for ML models.

---

```python
print(df.columns)
```

### 🔍 Prints All Column Names in the DataFrame:

For example, output might be:

```
Index(['Age', 'Systolic BP', 'Diastolic', 'BS', 'Body Temp', 'BMI',
       'Previous Complications', 'Preexisting Diabetes',
       'Gestational Diabetes', 'Mental Health', 'Heart Rate', 'Risk Level'],
      dtype='object')
```

✅ Helps confirm your feature names before selecting, grouping, or plotting.

---

### 🧠 Summary of What This Code Achieves:

| Task                | Purpose                                   |
| ------------------- | ----------------------------------------- |
| Load Data           | Reads the cleaned dataset                 |
| Correlation Heatmap | Identify linear relationships             |
| Histograms          | Explore distributions and outliers        |
| Violin Plot         | Visualize BS spread and density           |
| Histogram + KDE     | Understand BMI's probability distribution |
| Print Columns       | Confirm feature names for further steps   |

---

