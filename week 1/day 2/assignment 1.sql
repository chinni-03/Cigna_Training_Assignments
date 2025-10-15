-- List books with exactly one available copy
SELECT * FROM Books WHERE Available_Copies=1;
-- List authors who's name starts with a specific letter (ex. 'J')
SELECT * FROM Authors WHERE Author_Name LIKE 'J%';
-- List members with no address records
SELECT * FROM Members WHERE ADDRESS IS NULL;
-- List borrowing with specific borrow date
SELECT * FROM Borrowings WHERE Borrow_Date=TO_DATE('10/14/2025', 'MM-DD-YYYY');
-- List books with a publication year after 1990
SELECT * FROM Books WHERE Publication_Year > 1990;
-- List borrowings with no fines
SELECT * FROM Borrowings WHERE Fine=0;
-- List members sorted by membership date in descending order
SELECT * FROM Members ORDER BY Membership_Date DESC;
-- Count the total number of authors
SELECT COUNT(*) FROM Authors;
-- List books with title containing a specific word (ex. 'potter')
SELECT * FROM Books WHERE Title LIKE '%Potter%';
-- List borrowings returned on a specific date
SELECT * FROM Borrowings WHERE Return_Date=TO_DATE('10/14/2025', 'MM-DD-YYYY');
-- List members with specific area code in their phone number
SELECT * FROM Members WHERE Phone LIKE '111%';
-- List books sorted by title alphabetically
SELECT * FROM Books ORDER BY Title;
-- Sum the total available copies across all books
SELECT SUM(Available_Copies) FROM Books;
-- List borrowings with due date in a speciic month (ex. Oct 2025)
SELECT * FROM Borrowings WHERE TO_CHAR(Due_Date, 'YYYY-MM') ='2025-10';
-- List authors with names longer than 10 characters
SELECT * FROM Authors WHERE LENGTH(Author_Name)>10;
