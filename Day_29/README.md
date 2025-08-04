| Aspect                     | **Data Analysis (Data Cleaning)**                               | **Data Science (Data Preprocessing)**                                    |
| -------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **Goal**                   | Make the dataset readable and accurate for human interpretation | Prepare data in a machine-readable format for modeling                   |
| **Handles Missing Values** | Yes — Fill or drop missing data                                 | Yes — Fill missing values (if any) before feeding into models            |
| **Detects Outliers**       | Yes — Use visual tools (like histograms) to flag extreme values | Sometimes — Outliers may be scaled or removed based on model sensitivity |
| **Data Type Validation**   | Yes — Ensure correct types (int, float, object)                 | Yes — Must be numeric for most ML algorithms                             |
| **Encoding Categorical**   | Not always necessary                                            | Yes — Essential (e.g., Risk Level → 0, 1, 2)                             |
| **Feature Scaling**        | Not required                                                    | Required — to normalize features (StandardScaler)                        |
| **Output**                 | Cleaned data for exploration                                    | Preprocessed data ready for machine learning models                      |
| **Tools Used**             | `pandas`, `matplotlib`, `seaborn`                               | `pandas`, `scikit-learn`                                                 |
| **Example File Name**      | `cleaned_maternal_health_data.csv`                              | `preprocessed_maternal_health_data.csv`                                  |
