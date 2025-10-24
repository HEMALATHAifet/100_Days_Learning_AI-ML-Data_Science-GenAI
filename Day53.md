
````markdown
# 🧠 Day 53 – SQL Learning Journey  
### Topics Covered: Constraints | Normalization | Transactions  

---

## ⚙️ 1️⃣ Constraints – Primary Key & Foreign Key

Constraints help maintain **data accuracy and consistency** in relational databases.  

```sql
-- Create Department table
CREATE TABLE Department (
  dept_id INT PRIMARY KEY,
  dept_name VARCHAR(50)
);

-- Create Employee table with Foreign Key
CREATE TABLE Employee (
  emp_id INT PRIMARY KEY,
  emp_name VARCHAR(50),
  dept_id INT,
  FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);
````

🧩 **Explanation:**

* `PRIMARY KEY`: Ensures each record is unique and not NULL.
* `FOREIGN KEY`: Links data between tables and maintains referential integrity.

---

## 🧱 2️⃣ Normalization – 1NF, 2NF, 3NF

Normalization is the process of **structuring a database** to reduce redundancy and improve data integrity.

| Normal Form | Description                                         | Example                                                   |
| ----------- | --------------------------------------------------- | --------------------------------------------------------- |
| **1NF**     | Each cell contains only atomic (indivisible) values | No multiple phone numbers in one column                   |
| **2NF**     | 1NF + Remove partial dependency                     | Each non-key column depends on the whole primary key      |
| **3NF**     | 2NF + Remove transitive dependency                  | Non-key columns depend only on the key, not on each other |

📘 **Example Breakdown:**

Unnormalized Table

| StudentID | StudentName | Course1 | Course2 |
| --------- | ----------- | ------- | ------- |

➡️ **1NF:** Separate into individual rows
➡️ **2NF:** Separate Course details into a new table
➡️ **3NF:** Remove derived fields like "TotalMarks"

---

## 💾 3️⃣ Transactions – BEGIN, COMMIT, ROLLBACK

Transactions ensure **data reliability** when performing multiple SQL operations.

```sql
BEGIN;

UPDATE Accounts SET balance = balance - 1000 WHERE acc_no = 101;
UPDATE Accounts SET balance = balance + 1000 WHERE acc_no = 202;

COMMIT;
```

If something fails:

```sql
ROLLBACK;
```

⚡ **Key Concepts:**

* **BEGIN:** Start a transaction
* **COMMIT:** Save all changes
* **ROLLBACK:** Undo all uncommitted changes

---

## ✅ Summary

| Concept           | Purpose                 |
| ----------------- | ----------------------- |
| **Constraints**   | Maintain data integrity |
| **Normalization** | Eliminate redundancy    |
| **Transactions**  | Ensure reliability      |

---

## 💻 Repository Info

This repository contains:

* SQL scripts for **Constraints, Normalization, Transactions**
* Practice queries with results
* Concept notes for quick revision

---

## 📚 Learning Source

Part of my **100 Days of SQL Learning Journey** 🚀

---

## 🏷️ Hashtags

#SQL #DatabaseDesign #Constraints #Normalization #Transactions #SQLLearning #PrimaryKey #ForeignKey #Commit #Rollback #DataIntegrity #SQLPractice #LearningJourney #GitHubProjects

```
