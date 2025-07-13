# 📌 Step 1: Import Libraries
import pandas as pd
import numpy as np

# 📌 Step 2: Upload the file
from google.colab import files
uploaded = files.upload()  # upload your dirty_cafe_sales.csv here

# 📌 Step 3: Read the CSV file
df = pd.read_csv('dirty_cafe_sales.csv')  # update filename if needed

# 📌 Step 4: Create a copy to preserve original
clean_df = df.copy()

# 📌 Step 5: Replace 'ERROR' in 'Total Spent' with NaN
clean_df['Total Spent'] = clean_df['Total Spent'].replace("ERROR", np.nan)

# 📌 Step 6: Convert relevant columns to numeric
cols_to_convert = ['Quantity', 'Price Per Unit', 'Total Spent']
for col in cols_to_convert:
    clean_df[col] = pd.to_numeric(clean_df[col], errors='coerce')

# 📌 Step 7: Fill missing values
# Fill missing Item with 'Unknown'
clean_df['Item'].fillna('Unknown', inplace=True)

# Fill missing numerical columns with median
for col in ['Quantity', 'Price Per Unit', 'Total Spent']:
    clean_df[col].fillna(clean_df[col].median(), inplace=True)

# Replace 'UNKNOWN' in Payment Method and fill missing with mode
clean_df['Payment Method'].replace('UNKNOWN', np.nan, inplace=True)
clean_df['Payment Method'].fillna(clean_df['Payment Method'].mode()[0], inplace=True)

# Replace 'UNKNOWN' in Location and fill missing with 'Unknown'
clean_df['Location'].replace('UNKNOWN', np.nan, inplace=True)
clean_df['Location'].fillna('Unknown', inplace=True)

# Fill missing Transaction Date using forward fill
clean_df['Transaction Date'].fillna(method='ffill', inplace=True)

# 📌 Step 8: Recalculate 'Total Spent'
clean_df['Total Spent'] = clean_df['Quantity'] * clean_df['Price Per Unit']

# 📌 Step 9: Confirm cleaning is complete
print(clean_df.info())
print("\nMissing Values:\n", clean_df.isnull().sum())

# 📌 Step 10: Save cleaned dataset
clean_df.to_csv('cleaned_cafe_sales.csv', index=False)

# 📌 Step 11: Download the cleaned file
files.download('cleaned_cafe_sales.csv')
