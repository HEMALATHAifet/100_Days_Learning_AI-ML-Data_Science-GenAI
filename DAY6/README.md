## 📌 Day 6/100 - Web Scraping using BeautifulSoup

Welcome to **Day 6** of my **100 Days, 100 Skills** learning challenge!  
In this project, I practiced **web scraping** using **Python**, `requests`, and `BeautifulSoup` by extracting quotes and authors from a sample website.

---

### 🧠 Skill of the Day: Web Scraping with BeautifulSoup

This project demonstrates how to:

- Send HTTP requests using `requests`
- Parse and navigate HTML using `BeautifulSoup`
- Extract text data from tags
- Print quotes and their authors from a webpage

---

### 🌐 Website Scraped

- **URL**: [http://quotes.toscrape.com](http://quotes.toscrape.com)  
- A beginner-friendly site created for practicing web scraping (no legal or ethical issues)

---

### 🧾 Sample Output

```txt
“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.” - Albert Einstein
“It is our choices, Harry, that show what we truly are, far more than our abilities.” - J.K. Rowling
...
````

---

### 🚀 Code

📝 Python script: [`Web_Scraping_Using_BeautifulSoup.py`](./Web_Scraping_Using_BeautifulSoup.py)

---

### 📦 Requirements

Install the required Python packages:

```bash
pip install requests
pip install beautifulsoup4
```

---

### 🔍 Why BeautifulSoup & Requests?

* **`requests`** is used to send HTTP requests and get the HTML content of a webpage.
* **`BeautifulSoup`** helps parse the HTML and extract useful data like tags, text, and attributes.

Together, they allow you to fetch and analyze web data in Python easily.

---

### ❓ Need for Web Scraping

In AI/ML/Data Science/GenAI, **real-world data** is key. Web scraping helps when:

* There’s **no official API** provided by the data source
* You want to build **custom datasets** (e.g., for sentiment analysis, product reviews, news classification)
* You're developing **generative models** that require knowledge of trending or current data
* You need to **automate data collection** for research, model training, or dashboards

---

### 📚 What I Learned

* How to inspect and understand HTML structure
* The difference between `.find()` and `.find_all()`
* How to safely scrape websites using Python
* Importance of using `.text` to extract clean content
* The ethical considerations when scraping sites

---

### 📌 About the Challenge

This is part of my **#100DaysOfLearning** journey where I’m learning **1 AI/ML/Data Science/GenAI skill per day** to get my **first job** in the AI/ML industry.

* 🔗 [Follow my journey on LinkedIn](https://www.linkedin.com/in/hemalatha-a-developer)
* 🔗 [Check out the full challenge repo on GitHub](https://github.com/HEMALATHAifet/100_Days_Learning_AI-ML-Data_Science-GenAI/tree/main)

---

### ⚠️ Disclaimer

This project is for educational purposes only. Always check a website’s `robots.txt` and terms before scraping.

---

