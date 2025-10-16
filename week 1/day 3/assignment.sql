CREATE TABLE Dept(
    Deptno NUMBER PRIMARY KEY,
    Dname VARCHAR(20) NOT NULL,
    Loc VARCHAR(20)
);

CREATE TABLE Emps (
    Empno NUMBER PRIMARY KEY,
    Ename VARCHAR(50) NOT NULL,
    Job VARCHAR(20),
    Sal NUMBER DEFAULT 0 NOT NULL,
    Deptno NUMBER,
    CONSTRAINT fk_deptno FOREIGN KEY (Deptno) REFERENCES Dept(Deptno)
);

INSERT INTO Dept VALUES (10, 'HR', 'NEW YORK');
INSERT INTO Dept VALUES (20, 'IT', 'ZURICH');
INSERT INTO Dept (Deptno, Dname) VALUES (30, 'Operations');
INSERT INTO Dept VALUES (40, 'Sales', 'Bern');

INSERT INTO Emps VALUES (1, 'Harshini', 'Data Analyst', 80000, 20);
INSERT INTO Emps VALUES (2, 'Rosh', 'Data Analyst', 50000, 20);
INSERT INTO Emps VALUES (3, 'Mrinal', 'HR', 40000, 10);
INSERT INTO Emps VALUES (4, 'Emma', 'Sales', 50000, 40);
INSERT INTO Emps (Empno, Ename, Sal, Deptno) VALUES (5, 'Tarun', 40000, 30);
INSERT INTO Emps VALUES (6, 'Riya', 'SDE', 50000, 20);
INSERT INTO Emps VALUES (7, 'Vivek', 'SDE', 50000, 20);

--Types of Subqueries
-- Single-row Subquery
-- Finds employees whose salary is above the company’s average salary
SELECT ename, sal FROM emps WHERE sal > (SELECT AVG(sal) FROM emps);

-- Multi-row Subquery
-- Finds employees who work in departments located in NEW YORK
SELECT ename, deptno FROM emps WHERE deptno IN (SELECT deptno FROM dept WHERE loc = 'NEW YORK');

--Multi-column Subquery
-- Finds employees having the same job and department as employee 2
SELECT empno, ename, job, deptno FROM emps WHERE (job, deptno) IN (SELECT job, deptno FROM emps WHERE empno = 2);

--Correlated Subquery
-- Lists employees whose salary is higher than the average salary of their department
SELECT e.ename, e.sal, e.deptno FROM emps e WHERE e.sal > (SELECT AVG(e.sal) FROM emps  WHERE deptno = e.deptno);

-- Subqueries in Different Clauses
--  In the WHERE Clause
SELECT * FROM emps WHERE deptno IN (SELECT deptno FROM dept WHERE loc ='Zurich');

-- In the HAVING Clause
--Shows departments where the average salary is greater than the overall average salary
SELECT deptno, AVG(sal) FROM emps GROUP BY deptno HAVING AVG(sal) > (SELECT AVG(sal) FROM emps);

-- In the SELECT Clause
--Displays each employee’s name along with their department name
SELECT e.ename, (SELECT d.dname from dept d WHERE d.deptno = e.deptno) AS Department FROM emps e;

--  Increases salaries by 10% for all employees in the SALES department
UPDATE emps SET sal = sal * 0.1 WHERE deptno = (SELECT deptno FROM dept WHERE dname = 'IT');

---------- Questions ----------

-- Display employee names along with their department names.
SELECT e.ename, d.dname FROM emps e JOIN dept d ON e.deptno = d.deptno;

-- List all employees with their job titles and the location of their department.
SELECT e.ename, e.job, d.loc FROM emps e JOIN dept d ON e.deptno = d.deptno;

-- Display employees who work in the SALES department.
SELECT d.dname, e.ename FROM dept d JOIN emps e ON d.deptno = e.deptno WHERE d.dname = 'Sales';

-- List all employees along with their department name and location, including departments that have no employees.
SELECT e.ename, d.dname, d.loc FROM dept d LEFT JOIN emps e ON e.deptno = d.deptno;

-- Display all departments and employees, even if some employees are not assigned to any department.
SELECT d.dname, e.ename FROM dept d LEFT JOIN emps e ON e.deptno = d.deptno;

-- Show each department name and  total salary paid to its employees.
SELECT d.dname AS Department, SUM(e.sal) AS Total_salary FROM dept d LEFT JOIN emps e ON d.deptno = e.deptno GROUP BY d.dname;

-- Find departments that have more than 3 employees.  Display dname and no. of employees.
SELECT d.dname, COUNT(e.ename) AS Number_of_employees FROM dept d JOIN emps e ON d.deptno = e.deptno GROUP BY d.dname HAVING COUNT(*) > 3;

-- Display employees who work in the same location as the IT department.
SELECT e.ename FROM dept d JOIN emps e ON d.deptno = e.deptno WHERE d.loc IN (SELECT loc FROM dept WHERE dname = 'IT');

--  For each department, display the employee who has the highest salary.
SELECT e.ename, d.dname AS Department, e.sal FROM emps e JOIN dept d ON e.deptno = d.deptno WHERE e.sal = (SELECT MAX(sal) FROM emps WHERE deptno = d.deptno);

-- List employees whose salary is greater than the average salary of their department.
SELECT d.dname, e.ename, e.sal, d.dname, COALESCE(avg_table.avg_sal, 0) AS avg_sal FROM emps e
    JOIN dept d ON e.deptno = d.deptno
    LEFT JOIN (SELECT deptno, AVG(sal) AS avg_sal FROM emps GROUP BY deptno) avg_table
    ON e.deptno = avg_table.deptno;