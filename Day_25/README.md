
# ⏳ Time Series Forecasting: Daily Minimum Temperatures

This project demonstrates time series analysis and forecasting using Python. It uses a real-world dataset of daily minimum temperatures recorded in Melbourne, Australia, and applies statistical models like **ARIMA** and **Facebook Prophet** to predict future values.

---

## 📌 Project Objective

- Analyze temperature trends over time
- Test for stationarity using the ADF test
- Build forecasting models using ARIMA and Prophet
- Compare and visualize the results
- Evaluate model performance using RMSE

---

## 📂 Dataset

- **Source**: [Kaggle - Daily Minimum Temperatures](https://www.kaggle.com/datasets/shenba/time-series-datasets)
- **Format**: CSV
- **Columns**:
  - `Date`: Date of observation
  - `Temp`: Minimum temperature (°C)

---

## 🛠️ Technologies Used

- **Python**
- **Pandas** – data manipulation
- **Matplotlib & Seaborn** – visualization
- **Statsmodels** – ARIMA modeling
- **Prophet** – time series forecasting
- **Scikit-learn** – evaluation (RMSE)

---

## 🔍 Key Steps

1. **Data Preprocessing**  
   - Convert date column to datetime format  
   - Handle missing and invalid values (e.g., '?0.2')  
   - Set proper frequency and interpolate missing data

2. **Visualization**  
   - Plot temperature trends over time using Seaborn

3. **Stationarity Check**  
   - Used the **Augmented Dickey-Fuller (ADF)** test

4. **ARIMA Modeling**  
   - Fit ARIMA(5,1,0) model  
   - Forecast the next 30 days  
   - Visualize the predictions

5. **Prophet Modeling**  
   - Fit Prophet model with automatic trend/seasonality detection  
   - Forecast and plot future values

6. **Model Evaluation**  
   - Compute RMSE on test data (year 1990)  
   - RMSE achieved: **~3.98**

---

## 📈 Results

- Both models produced accurate short-term forecasts
- Prophet auto-handled seasonality better but ARIMA gave similar performance
- Visualizations helped interpret trends and model quality

---

## 📄 Outputs

- Forecast plots from both models
- RMSE printed in console
- [Optional] PDF export with code + output

---

## 🚀 How to Run

1. Upload the notebook to **Google Colab**
2. Install required packages:

```python
   !pip install pandas matplotlib seaborn statsmodels prophet

```

3. Run all cells in order
4. Modify `forecast steps`, model parameters, or data as needed

---

## 📌 Author

**👩‍💻 A. Hemalatha**
*#100DaysOfLearning | Day 25 – Time Series Analysis*
💡 Actively exploring AI/ML, Data Science, and Forecasting

---
