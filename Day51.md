### 🧩 **Tables Used**

**EMPLOYEE**

| EMPNO | ENAME  | JOB       | MGR  | HIREDATE   | SAL  | COMM | DEPTNO | PHONE      |
| ----- | ------ | --------- | ---- | ---------- | ---- | ---- | ------ | ---------- |
| 7369  | SMITH  | CLERK     | 7902 | 1980-12-17 | 800  | NULL | 20     | NULL       |
| 7499  | ALLEN  | SALESMAN  | 7698 | 1981-02-20 | 1600 | 300  | 30     | 9876543210 |
| 7521  | WARD   | SALESMAN  | 7698 | 1981-02-22 | 1250 | 500  | 30     | NULL       |
| 7566  | JONES  | MANAGER   | 7839 | 1981-04-02 | 2975 | NULL | 20     | 9876512345 |
| 7654  | MARTIN | SALESMAN  | 7698 | 1981-09-28 | 1250 | 1400 | 30     | NULL       |
| 7698  | BLAKE  | MANAGER   | 7839 | 1981-05-01 | 2850 | NULL | 30     | 9876509876 |
| 7782  | CLARK  | MANAGER   | 7839 | 1981-06-09 | 2450 | NULL | 10     | 9876598765 |
| 7788  | SCOTT  | ANALYST   | 7566 | 1982-12-09 | 3000 | NULL | 20     | NULL       |
| 7839  | KING   | PRESIDENT | NULL | 1981-11-17 | 5000 | NULL | 10     | 9876587654 |
| 7844  | TURNER | SALESMAN  | 7698 | 1981-09-08 | 1500 | 0    | 30     | NULL       |

**DEPARTMENT**

| DEPTNO | DNAME      | LOC      |
| ------ | ---------- | -------- |
| 10     | ACCOUNTING | NEW YORK |
| 20     | RESEARCH   | DALLAS   |
| 30     | SALES      | CHICAGO  |
| 40     | OPERATIONS | BOSTON   |

---

## 🧩 **1️⃣ NULL & COALESCE**

**Q1.** Show employee name and commission, replacing nulls with 0.

```sql
SELECT ENAME, COALESCE(COMM, 0) AS COMMISSION
FROM EMPLOYEE;
```

**Result (partial):**

| ENAME | COMMISSION |
| ----- | ---------- |
| SMITH | 0          |
| ALLEN | 300        |
| WARD  | 500        |

---

**Q2.** Display employee name and phone number, replace null phone with 'Not Available'.

```sql
SELECT ENAME, COALESCE(PHONE, 'Not Available') AS PHONE
FROM EMPLOYEE;
```

**Result (partial):**

| ENAME | PHONE         |
| ----- | ------------- |
| SMITH | Not Available |
| ALLEN | 9876543210    |

---

**Q3.** Calculate total earnings = SAL + COALESCE(COMM,0).

```sql
SELECT ENAME, SAL, COMM, SAL + COALESCE(COMM,0) AS TOTAL_EARNINGS
FROM EMPLOYEE;
```

**Result:** MARTIN → 2650, SMITH → 800

---

## 🔤 **2️⃣ String Functions**

**Q4.** Display employee names in uppercase.

```sql
SELECT UPPER(ENAME) AS UPPER_NAME FROM EMPLOYEE;
```

**Q5.** Display job titles in lowercase.

```sql
SELECT LOWER(JOB) AS JOB_IN_LOWER FROM EMPLOYEE;
```

**Q6.** Concatenate employee name and job as one string.

```sql
SELECT CONCAT(ENAME, ' - ', JOB) AS EMP_JOB
FROM EMPLOYEE;
```

**Result:** `KING - PRESIDENT`

---

**Q7.** Show first 3 letters of each employee’s name.

```sql
SELECT ENAME, SUBSTR(ENAME,1,3) AS SHORT_NAME
FROM EMPLOYEE;
```

**Result:** SMITH → SMI

---

**Q8.** Find position of letter ‘A’ in each name.

```sql
SELECT ENAME, INSTR(ENAME,'A') AS POS_OF_A
FROM EMPLOYEE;
```

**Result:** ALLEN → 1, SMITH → 0

---

**Q9.** Show name and length of each name.

```sql
SELECT ENAME, LENGTH(ENAME) AS NAME_LENGTH
FROM EMPLOYEE;
```

---

## ⏰ **3️⃣ Date and Time Functions**

**Q10.** Show current date and employee’s hire date.

```sql
SELECT ENAME, HIREDATE, SYSDATE AS TODAY
FROM EMPLOYEE;
```

---

**Q11.** Display number of months each employee has worked.

```sql
SELECT ENAME, MONTHS_BETWEEN(SYSDATE, HIREDATE) AS MONTHS_WORKED
FROM EMPLOYEE;
```

---

**Q12.** Add 6 months to each hire date.

```sql
SELECT ENAME, ADD_MONTHS(HIREDATE,6) AS CONFIRMATION_DATE
FROM EMPLOYEE;
```

---

**Q13.** Truncate hire date to month.

```sql
SELECT ENAME, TRUNC(HIREDATE,'MM') AS MONTH_START
FROM EMPLOYEE;
```

---

## 🔢 **4️⃣ Numeric Functions**

**Q14.** Round salaries to nearest hundred.

```sql
SELECT ENAME, ROUND(SAL,-2) AS ROUNDED_SAL
FROM EMPLOYEE;
```

---

**Q15.** Get next highest integer salary.

```sql
SELECT ENAME, CEIL(SAL/1000)*1000 AS CEIL_SAL
FROM EMPLOYEE;
```

---

**Q16.** Get next lowest integer salary.

```sql
SELECT ENAME, FLOOR(SAL/1000)*1000 AS FLOOR_SAL
FROM EMPLOYEE;
```

---

**Q17.** Find remainder when salary divided by 1000.

```sql
SELECT ENAME, MOD(SAL,1000) AS REMAINDER
FROM EMPLOYEE;
```

---

## ⚙️ **5️⃣ CASE Expressions**

**Q18.** Classify employees based on salary.

```sql
SELECT ENAME, SAL,
CASE
  WHEN SAL >= 3000 THEN 'HIGH'
  WHEN SAL BETWEEN 1500 AND 2999 THEN 'MEDIUM'
  ELSE 'LOW'
END AS SAL_CATEGORY
FROM EMPLOYEE;
```

**Result (partial):**

| ENAME | SAL  | SAL_CATEGORY |
| ----- | ---- | ------------ |
| KING  | 5000 | HIGH         |
| ALLEN | 1600 | MEDIUM       |
| SMITH | 800  | LOW          |

---

**Q19.** Display message if commission is null or present.

```sql
SELECT ENAME,
CASE
  WHEN COMM IS NULL THEN 'No Commission'
  WHEN COMM = 0 THEN 'Zero Commission'
  ELSE 'Has Commission'
END AS COMM_STATUS
FROM EMPLOYEE;
```

---

**Q20.** Combine department and employee info with CASE logic.

```sql
SELECT E.ENAME, D.DNAME,
CASE D.LOC
  WHEN 'NEW YORK' THEN 'Head Office'
  WHEN 'CHICAGO' THEN 'Sales Branch'
  ELSE 'Regional Branch'
END AS LOCATION_TYPE
FROM EMPLOYEE E
JOIN DEPARTMENT D ON E.DEPTNO = D.DEPTNO;
```

---

