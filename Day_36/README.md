## ✅ **DATA ANALYSIS -Storytelling from Your Visuals**

### 🎯 Goal:

To identify how key features like **BMI**, **Blood Sugar (BS)**, and **Systolic BP** vary across **Risk Levels** and what patterns help indicate **high-risk pregnancies**.

---

### 📊 1. **BMI Distribution by Risk Level**

* You plotted **BMI** by `'Risk Level'` and added a red line at **BMI = 35**.
* ✅ **Insight:**
  From the boxplot, it's likely that:

  * Women classified as **High Risk** tend to have a **higher median BMI** than those in the Low Risk group.
  * A good number of **High Risk cases** fall **above the 35 BMI threshold**, which is considered **obese** and clinically significant.
  * The **spread** (IQR) may also be wider in the High group, indicating **greater variability**.

🟢 **Interpretation for Non-technical audience:**

> Pregnant women with a BMI above 35 are **much more likely to fall into the High-Risk category**, suggesting weight management could be important for prevention.

---

### 📊 2. **Blood Sugar (BS) by Risk Level**

* You used a purple line to mark **BS = 140**.
* ✅ **Insight:**

  * The **High Risk group** shows more values above the 140 line.
  * The **median BS** might be closer to or above 140 for High Risk women, while **Low Risk** women tend to stay well below it.
  * This suggests a **strong correlation** between high blood sugar and pregnancy risk.

🟢 **Interpretation:**

> Elevated blood sugar levels are a **clear red flag** — women with BS over 140 are more likely to be classified as high-risk.

---

### 📊 3. **Systolic BP by Risk Level**

* A green line at **140 Systolic BP** indicates a threshold for hypertension.
* ✅ **Insight:**

  * Like BMI and BS, **Systolic BP is higher in the High Risk group**.
  * You may see **outliers** or a longer upper whisker in the High group, pointing to **cases of severe hypertension**.
  * Low Risk cases generally stay under the 140 mark.

🟢 **Interpretation:**

> High systolic blood pressure (above 140) is **commonly associated with pregnancy risk**, aligning with medical guidelines on preeclampsia and hypertension.

---

## 🧠 Final Summary for Storytelling

> By visualizing BMI, Blood Sugar, and Systolic BP against Risk Level, we see a **consistent pattern**:
> **Higher values in these features are associated with High Risk pregnancies.**
> These insights are essential for **early screening**, **clinical awareness**, and building **predictive models**.

---
## **DATA SCIENCE - FINAL MODEL TRAINING**
---

Think of the model like a **very experienced doctor**.
You gave this doctor a **set of health details** about a pregnant woman:

* **Age** → 28 years
* **Systolic BP** → 150 (this is high)
* **Diastolic BP** → 95 (also high)
* **Blood Sugar (BS)** → 145 (above normal)
* **Body Temperature** → 98.6°F (normal)
* **BMI** → 36.5 (obese range)
* **Previous Complications** → Yes (1 means yes)
* **Preexisting Diabetes** → No
* **Gestational Diabetes** → Yes (1 means yes)
* **Mental Health Issues** → Yes
* **Heart Rate** → 80 (normal)

---

Here’s what happened behind the scenes:

1. **The model remembered patterns** from many real examples in its training data — it saw thousands of cases where certain combinations of blood pressure, sugar, BMI, and other factors led to either a "Low Risk" or a "High Risk" pregnancy.
2. When you entered your details, the model compared them with all the cases it knows.
3. In this example:

   * High **Blood Pressure** (both numbers)
   * High **BMI**
   * High **Blood Sugar**
   * Previous complications
   * Gestational diabetes

   These are all red flags in the medical world.
4. Based on those warning signs, the model concluded: **"This pregnancy is high risk."**

---

💡 **Simple analogy:**
It’s like a weather app predicting rain.

* If the sky is dark, humidity is high, and there’s a history of rain with such conditions → it says *“Rain likely.”*
* Here, instead of clouds and humidity, we have BMI, BP, sugar, and history.
* The “rain” here is *“High risk”*.

---
