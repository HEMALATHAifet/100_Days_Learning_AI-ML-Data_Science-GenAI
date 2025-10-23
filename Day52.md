

## 🧠 **Day 52 of My SQL Learning Journey – Views, Procedures & Functions!**

Today’s focus was on **code reusability and abstraction** in SQL 💡
Instead of repeating long queries, I learned how to **encapsulate logic** inside *views, procedures, and user-defined functions*.

---

### 🪟 **1️⃣ Views**

A **view** acts like a *virtual table* that stores a query result for reuse.

**Create a View:**

```sql
CREATE VIEW emp_dept_view AS
SELECT e.ename, e.job, d.dname
FROM employee e
JOIN department d ON e.deptno = d.deptno;
```

**Use the View:**

```sql
SELECT * FROM emp_dept_view;
```

**Alter a View:**

```sql
CREATE OR REPLACE VIEW emp_dept_view AS
SELECT e.ename, e.sal, d.dname
FROM employee e
JOIN department d ON e.deptno = d.deptno;
```

💬 *Why useful?* – Simplifies complex queries and adds security (you can hide sensitive columns).

---

### ⚙️ **2️⃣ Stored Procedures**

A **Stored Procedure** is a saved block of SQL logic that can take input, perform tasks, and even return output.

**Example:**

```sql
CREATE PROCEDURE get_high_salary_emps (IN min_sal DECIMAL)
BEGIN
  SELECT ename, sal
  FROM employee
  WHERE sal > min_sal;
END;
```

**Execute it:**

```sql
CALL get_high_salary_emps(3000);
```

💬 *Why useful?* – Avoids rewriting logic and improves performance.

---

### 🔁 **3️⃣ User-Defined Functions (UDFs)**

A **Function** returns a value — perfect for calculations or repeated logic.

**Example:**

```sql
CREATE FUNCTION annual_salary (sal DECIMAL)
RETURNS DECIMAL
DETERMINISTIC
RETURN sal * 12;
```

**Use it in a query:**

```sql
SELECT ename, annual_salary(sal) AS yearly_salary
FROM employee;
```

💬 *Why useful?* – Makes repetitive logic reusable in multiple queries.

---

### ✨ **Key Takeaway**

➡️ *Views* simplify reading data.
➡️ *Stored Procedures* automate actions.
➡️ *Functions* make code modular.

Each helps make SQL projects cleaner, faster, and easier to maintain.


#SQL #100DaysOfSQL #LearningJourney #Database #Views #StoredProcedures #Functions #Day52 #DataEngineering
