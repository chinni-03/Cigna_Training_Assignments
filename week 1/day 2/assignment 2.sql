CREATE TABLE Product(
  Product_id NUMBER NOT NULL PRIMARY KEY,
  Product_name VARCHAR(50) NOT NULL,
  Product_category CHAR(50) NOT NULL,
  Price NUMBER NOT NULL CHECK (Price > 0),
  Stock NUMBER DEFAULT 0 CHECK (Stock > 0)
);

CREATE TABLE Customer(
  Customer_id NUMBER NOT NULL PRIMARY KEY,
  First_name VARCHAR(50) NOT NULL,
  Last_name VARCHAR(50) NOT NULL,
  Email VARCHAR(50) UNIQUE NOT NULL,
  Phone VARCHAR2(15)
);

CREATE TABLE Orders(
  Order_id NUMBER NOT NULL PRIMARY KEY,
  Customer_id NUMBER NOT NULL,
  Order_date DATE DEFAULT SYSDATE,
  Total_orders NUMBER DEFAULT 0,
  CONSTRAINT fk_customer FOREIGN KEY (Customer_id) REFERENCES Customer (Customer_id)
);

CREATE TABLE OrderDetails(
  OrderDetail_id NUMBER NOT NULL PRIMARY KEY,
  Order_id NUMBER NOT NULL,
  Product_id NUMBER NOT NULL,
  Quantity NUMBER DEFAULT 0,
  CONSTRAINT fk_order FOREIGN KEY (Order_id) REFERENCES Orders (Order_id),
  CONSTRAINT fk_product FOREIGN KEY (Product_id) REFERENCES Product (Product_id)
);

INSERT INTO Product (Product_id, Product_name, Product_category, Price, Stock) VALUES (1, 'Laptop', 'Electronics', 80000, 50);
INSERT INTO Product (Product_id, Product_name, Product_category, Price, Stock) VALUES (2, 'Mouse', 'Electronics', 700, 15);

INSERT INTO Customer (Customer_id, First_name, Last_name, Email, Phone) VALUES (1, 'Harshini', 'Vijendra Kumar', 'harshinivk12@gmail.com', '9901562607');
INSERT INTO Customer (Customer_id, First_name, Last_name, Email) VALUES (2, 'Rosh', 'RK Vashista', 'rosh@gmail.com');

INSERT INTO Orders (Order_id, Customer_id, Order_date, Total_orders) VALUES (1, 1, SYSDATE, 2);
INSERT INTO Orders (Order_id, Customer_id, Order_date, Total_orders) VALUES (2, 1, SYSDATE, 2);
INSERT INTO Orders (Order_id, Customer_id, Order_date, Total_orders) VALUES (3, 2, SYSDATE, 3);
INSERT INTO Orders (Order_id, Customer_id, Order_date, Total_orders) VALUES (4, 2, SYSDATE, 3);

INSERT INTO OrderDetails (OrderDetail_id, Order_id, Product_id, Quantity) VALUES (1, 1, 1, 2);
INSERT INTO OrderDetails (OrderDetail_id, Order_id, Product_id, Quantity) VALUES (2, 2, 2, 2);
INSERT INTO OrderDetails (OrderDetail_id, Order_id, Product_id, Quantity) VALUES (3, 3, 1, 2);
INSERT INTO OrderDetails (OrderDetail_id, Order_id, Product_id, Quantity) VALUES (4, 4, 2, 2);

-- Retrieve products with low stock (< 20)
SELECT Product_id, Product_name, Stock from Product WHERE Stock < 20;

-- Calculate the total amount spent by each customer
SELECT c.Customer_id, c.First_name, c.Last_name, SUM(p.Price * od.Quantity) AS Total_Amount
    FROM Customer c
    JOIN Orders o ON c.Customer_id = o.Customer_id
    JOIN OrderDetails od ON od.Order_id = o.Order_id
    JOIN Product p ON p.Product_id = od.Product_id
    GROUP BY c.Customer_id, c.First_name, c.Last_name;
    
-- Update the product stock quantities after orders are placed to reflect purchased items
UPDATE Product SET Stock=Stock - (
    SELECT SUM(Quantity) FROM OrderDetails
    WHERE OrderDetails.Product_id = Product.Product_id
);
SELECT Stock from Product;
