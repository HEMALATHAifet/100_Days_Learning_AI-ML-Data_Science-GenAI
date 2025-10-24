````markdown
# 🧠 Day 54 – SQL Learning Journey  
### Topics Covered: Constraints | ACID Properties | SQL vs NoSQL  

---

## 🧩 1️⃣ Constraints – UNIQUE, NOT NULL, CHECK  

```sql
CREATE TABLE Employee (
  emp_id INT PRIMARY KEY,
  emp_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE,
  age INT CHECK (age >= 18)
);
````

🧠 **Explanation:**

* **NOT NULL:** Ensures column cannot have missing values
* **UNIQUE:** Prevents duplicate entries
* **CHECK:** Adds a condition that data must satisfy

📘 **Result:** Only valid and unique employee records are inserted.

---

## ⚙️ 2️⃣ ACID Properties in Databases

| Property        | Meaning                                 | Example                                            |
| --------------- | --------------------------------------- | -------------------------------------------------- |
| **Atomicity**   | All-or-nothing execution                | Bank transfer (both debit and credit must succeed) |
| **Consistency** | Data integrity is preserved             | Balance cannot go negative                         |
| **Isolation**   | Concurrent transactions don’t interfere | Multiple users updating without conflict           |
| **Durability**  | Committed data is safe permanently      | Power failure won’t lose committed data            |

💡 **Goal:** Reliable and trustworthy transactions in every situation.

---

## 🗃️ 3️⃣ SQL vs NoSQL – Overview

| Aspect           | SQL Databases       | NoSQL Databases                                              |
| ---------------- | ------------------- | ------------------------------------------------------------ |
| **Model**        | Relational (Tables) | Non-relational (Documents, Key-Value, Graphs)                |
| **Schema**       | Fixed               | Flexible                                                     |
| **Transactions** | ACID compliant      | BASE (Basically Available, Soft state, Eventual consistency) |
| **Scalability**  | Vertical            | Horizontal                                                   |
| **Examples**     | MySQL, PostgreSQL   | MongoDB, Cassandra                                           |
| **Best For**     | Structured data     | Unstructured/semi-structured data                            |

📘 **When to Use:**

* Use **SQL** for transactional systems (Banking, ERP)
* Use **NoSQL** for scalable, fast-changing apps (Chat, Analytics, IoT)

---

## ✅ Summary

| Concept             | Purpose                 |
| ------------------- | ----------------------- |
| **Constraints**     | Control data integrity  |
| **ACID Properties** | Guarantee reliability   |
| **SQL vs NoSQL**    | Choose right data model |

---

## 💻 Repository Info

Includes:

* SQL scripts for constraints
* Notes on ACID properties
* Comparison of SQL and NoSQL with examples

---

## 🏷️ Hashtags

#SQL #NoSQL #DatabaseDesign #ACID #SQLLearning #Constraints #SQLPractice #DataEngineering #MongoDB #PostgreSQL #LearningJourney #GitHubProjects

```
