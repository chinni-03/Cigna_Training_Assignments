-- ASSIGNMENT 1
DECLARE
    p NUMBER;
    r NUMBER;
    t NUMBER;
    simple_interest NUMBER;
BEGIN
    p := 10;
    r := 10;
    t := 10;
    simple_interest := (p * r * t)/100;
    DBMS_OUTPUT.PUT_LINE('Simple Interest for p = 10 , r = 10 and t = 10: ' || simple_interest);
END;

-- ASSIGNMENT 2
DECLARE
    emp_name VARCHAR(20);
    salary NUMBER;
    bonus NUMBER;
BEGIN
    emp_name := 'Harshini';
    salary := 50000;
    IF salary > 50000 THEN
        bonus := 0.1 * salary;
        DBMS_OUTPUT.PUT_LINE(emp_name || ' salary after bonus: ' || (salary + bonus));
    ELSE
        bonus := 0.15 * salary;
        DBMS_OUTPUT.PUT_LINE(emp_name || ' salary after bonus: ' || (salary + bonus));
    END IF;
END;

-- ASSIGNMENT 3
DECLARE
    v_dept dept%ROWTYPE;
BEGIN
    SELECT * INTO v_dept FROM dept WHERE deptno = 20;
    DBMS_OUTPUT.PUT_LINE(v_dept.dname || ' department is located in ' || v_dept.loc);
EXCEPTION
   WHEN NO_DATA_FOUND THEN
      DBMS_OUTPUT.PUT_LINE('No such department found!');
END;

-- ASSIGNMENT 4
DROP TABLE Marks;
DROP TABLE Student;
CREATE TABLE Student (
    sname VARCHAR(50),
    sid NUMBER PRIMARY KEY
);

CREATE TABLE Marks (
    marks NUMBER,
    sid NUMBER,
    CONSTRAINT fk_sid FOREIGN KEY (sid) REFERENCES Student (sid)
);

INSERT INTO Student VALUES ('Harshini', 11);
INSERT INTO Student VALUES ('Rosh', 12);
INSERT INTO Student VALUES ('Viv', 13);
INSERT INTO Student VALUES ('Bub', 14);

INSERT INTO Marks VALUES (99, 11);
INSERT INTO Marks VALUES (99, 12);
INSERT INTO Marks VALUES (99, 13);
INSERT INTO Marks VALUES (99, 14);

DECLARE
    TYPE marks_table IS TABLE OF NUMBER INDEX BY VARCHAR2(10);
    v_marks marks_table;
    
    total NUMBER;
    avg_marks NUMBER;
BEGIN
    FOR rec in (SELECT s.sname, m.marks FROM Student s JOIN Marks m ON s.sid = m.sid) LOOP
        v_marks(rec.sname) := rec.marks;
        DBMS_OUTPUT.PUT_LINE(rec.sname || ' scored ' || v_marks(rec.sname));
    END LOOP;
    SELECT SUM(marks) INTO total FROM Marks;
    SELECT AVG(marks) INTO avg_marks FROM Marks;
    DBMS_OUTPUT.PUT_LINE('Total marks: ' || total);
    DBMS_OUTPUT.PUT_LINE('Average marks: ' || avg_marks);
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No data available!');
END;

-- ASSIGNMENT 5
DECLARE
    TYPE t_country_capital IS TABLE OF VARCHAR2(50) INDEX BY VARCHAR2(50);
    
    v_capitals t_country_capital;
    v_key VARCHAR2(50);
    v_answer VARCHAR(50);
BEGIN
    v_capitals('USA') := 'Washington';
    v_capitals('France') := 'Paris';
    v_capitals('Switzerland') := 'Zurich';
    v_capitals('China') := 'Beijing';
    v_capitals('Uk') := 'London';
    v_capitals('Ireland') := 'Dublin';
    
    v_key := 'Switzerland';
    
    IF v_capitals.EXISTS(v_key) THEN
        DBMS_OUTPUT.PUT_LINE('Capital of ' || v_key || ' is ' || v_capitals(v_key));
    ELSE
        DBMS_OUTPUT.PUT_LINE('Capital not available in the array!');
    END IF;
END;