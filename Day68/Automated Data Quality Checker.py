import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (update file name if needed)
file_path = "salesforcourse-4fe2kehu.csv"   # or .xlsx

if file_path.endswith(".csv"):
    df = pd.read_csv(file_path)
else:
    df = pd.read_excel(file_path)

# -------------------------------
# Data Quality Checks
# -------------------------------

# Missing values
missing = df.isnull().sum()

# Duplicates
duplicates = df.duplicated().sum()

# Data types
dtypes = df.dtypes

# Outlier detection (IQR method)
outliers = {}

for col in df.select_dtypes(include='number').columns:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1

    outliers[col] = df[
        (df[col] < q1 - 1.5 * iqr) |
        (df[col] > q3 + 1.5 * iqr)
    ].shape[0]

# -------------------------------
# Print Results
# -------------------------------
print("\nMissing Values:\n", missing)
print("\nTotal Duplicates:", duplicates)
print("\nData Types:\n", dtypes)
print("\nOutliers:\n", outliers)

# -------------------------------
# Visualization
# -------------------------------
missing.plot(kind='bar', title="Missing Values by Column")
plt.tight_layout()
plt.show()

# -------------------------------
# Export Reports
# -------------------------------
with pd.ExcelWriter("data_quality_report.xlsx") as writer:
    missing.to_excel(writer, sheet_name="Missing Values")
    dtypes.to_excel(writer, sheet_name="Data Types")

pd.DataFrame.from_dict(outliers, orient='index', columns=['Outliers']) \
    .to_excel("outliers_report.xlsx")

print("\nReports generated successfully!")
