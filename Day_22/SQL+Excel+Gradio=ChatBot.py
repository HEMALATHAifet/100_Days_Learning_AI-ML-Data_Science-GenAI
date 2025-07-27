# ✅ Step 1: Install required packages
!pip install -q gradio pandas openpyxl

# ✅ Step 2: Create sample Excel file
import pandas as pd

data = {
    "OrderID": [101, 102, 103, 104, 105],
    "CustomerName": ["Ravi", "Priya", "Aman", "Sneha", "Vikram"],
    "Product": ["Keyboard", "T-Shirt", "Mouse", "Shoes", "Monitor"],
    "Category": ["Electronics", "Apparel", "Electronics", "Apparel", "Electronics"],
    "Quantity": [2, 3, 1, 2, 1],
    "Price": [800, 500, 400, 1200, 5500],
    "OrderDate": pd.to_datetime(["2024-10-01", "2024-10-02", "2024-10-03", "2024-10-04", "2024-10-05"])
}

df = pd.DataFrame(data)
df.to_excel("sales_data.xlsx", index=False)

# ✅ Step 3: Load Excel data into SQLite
import sqlite3
import gradio as gr

def setup_database():
    df = pd.read_excel("sales_data.xlsx")
    conn = sqlite3.connect(":memory:")
    df.to_sql("sales", conn, index=False, if_exists="replace")
    return conn

conn = setup_database()

# ✅ Step 4: Question to SQL mapping
def question_to_sql(question):
    q = question.lower()
    if "total sales" in q:
        return "SELECT SUM(Quantity * Price) AS TotalSales FROM sales"
    elif "sales by category" in q or "category wise" in q:
        return "SELECT Category, SUM(Quantity * Price) AS Revenue FROM sales GROUP BY Category"
    elif "sales by date" in q:
        return "SELECT OrderDate, SUM(Quantity * Price) AS DailySales FROM sales GROUP BY OrderDate"
    elif "top category" in q:
        return "SELECT Category, SUM(Quantity * Price) AS Revenue FROM sales GROUP BY Category ORDER BY Revenue DESC LIMIT 1"
    else:
        return None

# ✅ Step 5: Gradio chatbot function
def chat_fn(message, history=[]):
    sql = question_to_sql(message)
    if not sql:
        return "❗ Sorry, I didn't understand that. Try asking: 'total sales', 'sales by category', or 'sales by date'."
    try:
        result = pd.read_sql_query(sql, conn)
        return result.to_markdown()
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# ✅ Step 6: Launch Gradio app
gr.ChatInterface(fn=chat_fn, title="📊 Chat with Excel Data (SQL Powered)").launch()
