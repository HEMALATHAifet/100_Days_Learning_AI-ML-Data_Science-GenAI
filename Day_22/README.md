
# 📊 Chat with Excel Data using SQL and Gradio

This project is a simple chatbot built with **Gradio** that allows users to ask **natural language questions** about a **sales dataset stored in Excel**. The questions are converted into SQL queries, and answers are returned from an in-memory **SQLite** database.

---

## ✅ Features

- 📥 Load and parse Excel file using `pandas`
- 🧠 Map user questions to SQL queries
- 🗃️ Query SQLite database in-memory
- 💬 Simple Gradio chatbot interface
- 📌 Predefined queries for common sales analytics

---

## 🔧 Installation (Google Colab / Local)

```bash
pip install gradio pandas openpyxl
````

---

## 📁 Sample Data (Auto-generated)

The app uses a sample dataset like this:

| OrderID | CustomerName | Product  | Category    | Quantity | Price | OrderDate  |
| ------- | ------------ | -------- | ----------- | -------- | ----- | ---------- |
| 101     | Ravi         | Keyboard | Electronics | 2        | 800   | 2024-10-01 |
| 102     | Priya        | T-Shirt  | Apparel     | 3        | 500   | 2024-10-02 |
| ...     | ...          | ...      | ...         | ...      | ...   | ...        |

---

## 🚀 How to Use

1. Run the Python script in Google Colab or locally.
2. A Gradio chat interface will appear.
3. Ask questions like:

```
What is the total sales?
Show sales by category
Sales by date
Which is the top category?
```

---

## 🤖 How It Works

* **Excel ➝ pandas ➝ SQLite:**
  The sample Excel file is loaded into a pandas DataFrame and then written to a SQLite in-memory database.

* **User Question ➝ SQL Mapping:**
  A Python function matches keywords in the user question to predefined SQL queries.

* **Gradio Interface:**
  The `ChatInterface` runs a function that takes the user message, converts it to SQL, executes the query, and returns the result.

---

## 🧠 Supported Questions

| Example Question           | SQL Logic                                                               |
| -------------------------- | ----------------------------------------------------------------------- |
| What is the total sales?   | `SELECT SUM(Quantity * Price) AS TotalSales FROM sales`                 |
| Show sales by category     | `SELECT Category, SUM(Quantity * Price) FROM sales GROUP BY Category`   |
| Sales by date              | `SELECT OrderDate, SUM(Quantity * Price) FROM sales GROUP BY OrderDate` |
| Which is the top category? | `... ORDER BY Revenue DESC LIMIT 1`                                     |

---

## 📦 To Do

* [ ] Add support for uploading custom Excel files
* [ ] Use OpenAI or LLM for dynamic SQL generation
* [ ] Add visual charts for sales trends
* [ ] Expand question mapping logic

---

## 🙋‍♀️ Created By

**A. Hemalatha**
Data Science & AI Enthusiast

```
