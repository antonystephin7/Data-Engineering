-- Create a view to display customer name, account number, account type, and balance.
CREATE VIEW Customer_Account_View AS 
SELECT c.CustomerName, a.AccountNumber, a.AccountType, a.Balance FROM Customers c JOIN Accounts a ON c.CustomerID = a.CustomerID;

-- Create a view to display customers whose account balance is greater than ₹50,000.
CREATE VIEW High_Balance_Customers AS
SELECT c.CustomerName, a.AccountNumber, a.AccountType, a.Balance FROM Customers c JOIN Accounts a ON c.CustomerID = a.CustomerID WHERE a.Balance > 50000;

-- Create a view showing all active bank accounts.
CREATE VIEW Active_Bank_Accounts AS
SELECT * FROM Accounts WHERE Status = 'Active';

-- Create a view displaying customer transaction details, including customer name, transaction type, amount, and transaction date.
CREATE VIEW Customer_Transaction_View AS
SELECT c.CustomerName, t.TransactionType, t.Amount, t.TransactionDate FROM Customers c JOIN Accounts a ON c.CustomerID = a.CustomerID 
JOIN Transactions t ON a.AccountID = t.AccountID;

-- Create a view showing customers who have performed transactions during the current month.
CREATE VIEW Current_Month_Customers AS
SELECT DISTINCT c.CustomerID, c.CustomerName FROM Customers c JOIN Accounts a ON c.CustomerID = a.CustomerID JOIN Transactions t ON a.AccountID = t.AccountID
WHERE t.TransactionDate >= DATE_FORMAT(CURDATE(), '%Y-%m-01') AND t.TransactionDate < DATE_ADD(DATE_FORMAT(CURDATE(), '%Y-%m-01'), INTERVAL 1 MONTH);

-- Create a view displaying product name, category, price, and available stock.
CREATE VIEW Product_Stock_View AS
SELECT ProductName, Category, Price, Stock AS Available_Stock FROM Products;

-- Display the view
SELECT * FROM Product_Stock_View;

-- Create a view showing products whose stock is below the reorder level.
CREATE VIEW Low_Stock_Products AS 
SELECT ProductName, Category, Price, Stock, ReorderLevel FROM Products WHERE Stock < ReorderLevel;

-- Display the view
SELECT * FROM Low_Stock_Products;

-- Create a view displaying customer name, order ID, order date, and order amount.
CREATE VIEW Customer_Order_View AS
SELECT c.CustomerName, o.OrderID, o.OrderDate, o.OrderAmount FROM Customers AS c INNER JOIN Orders AS o ON c.CustomerID = o.CustomerID;

-- Display the view
SELECT * FROM Customer_Order_View;

-- Create a view showing all pending orders.
CREATE VIEW Pending_Orders AS 
SELECT * FROM Orders WHERE Status = 'Pending';

-- Display the view
SELECT * FROM Pending_Orders;

-- Create a view displaying order details along with customer and product information using joins.
CREATE VIEW Order_Details_View AS
SELECT o.OrderID, o.OrderDate, c.CustomerName, p.ProductName, p.Category, od.Quantity, od.Price, (od.Quantity * od.Price) AS Total_Amount FROM Orders AS o
INNER JOIN Customers AS c ON o.CustomerID = c.CustomerID INNER JOIN OrderDetails AS od ON o.OrderID = od.OrderID INNER JOIN Products AS p ON od.ProductID = p.ProductID;

-- Display the view
SELECT * FROM Order_Details_View;

-- Create a view to display the total amount spent by each customer.
CREATE VIEW Customer_Total_Spending AS
SELECT c.CustomerID, c.CustomerName, SUM(o.OrderAmount) AS Total_Spent FROM Customers AS c INNER JOIN Orders AS o ON c.CustomerID = o.CustomerID GROUP BY c.CustomerID, c.CustomerName;

-- Display the view
SELECT * FROM Customer_Total_Spending;

-- Create a view showing category-wise total sales.
CREATE VIEW Category_Wise_Sales AS
SELECT p.Category, SUM(od.Quantity * od.Price) AS Total_Sales FROM Products AS p INNER JOIN OrderDetails AS od ON p.ProductID = od.ProductID GROUP BY p.Category;

-- Display the view
SELECT * FROM Category_Wise_Sales;

-- Create a view displaying products based on total quantity sold.
CREATE VIEW Top_Selling_Products AS
SELECT p.ProductID, p.ProductName, SUM(od.Quantity) AS Total_Quantity_Sold FROM Products AS p INNER JOIN OrderDetails AS od ON p.ProductID = od.ProductID GROUP BY p.ProductID, p.ProductName;

-- Display products from highest to lowest quantity sold
SELECT * FROM Top_Selling_Products ORDER BY Total_Quantity_Sold DESC;

-- Create a view displaying employee name, department, designation, and salary.
CREATE VIEW Employee_Details_View AS 
SELECT EmployeeName, Department, Designation, Salary FROM Employees;

-- Create a view showing employees whose salary is greater than ₹50,000.
CREATE VIEW High_Salary_Employees AS
SELECT EmployeeName, Department, Designation, Salary FROM Employees WHERE Salary > 50000;

-- Create a view displaying employees belonging to the IT department.
CREATE VIEW IT_Department_Employees AS
SELECT EmployeeName, Department, Designation, Salary FROM Employees WHERE Department = 'IT';

-- Create a view showing department-wise employee count.
CREATE VIEW Department_Employee_Count AS
SELECT Department, COUNT(*) AS Employee_Count FROM Employees GROUP BY Department;

-- Create a view showing department-wise average salary.
CREATE VIEW Department_Average_Salary AS
SELECT Department, AVG(Salary) AS Average_Salary FROM Employees GROUP BY Department;

-- Create a view displaying employees along with their manager's name using a self join.
CREATE VIEW Employee_Manager_View AS
SELECT e.EmployeeName, e.Department, e.Designation, e.Salary, m.EmployeeName AS ManagerName FROM Employees AS e LEFT JOIN Employees AS m ON e.ManagerID = m.EmployeeID;

-- Create a view showing employees who joined the company within the last 1 year.
CREATE VIEW Recent_Employees AS
SELECT EmployeeName, Department, Designation, Salary, JoiningDate FROM Employees WHERE JoiningDate >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR) AND JoiningDate <= CURDATE();