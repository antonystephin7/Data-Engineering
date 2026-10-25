-- Display all departments for which at least one employee exists.
SELECT * FROM Departments d WHERE EXISTS (SELECT 1 FROM Employees e WHERE e.DepartmentID = d.DepartmentID);

-- Display employees who belong to a department that exists in the Departments table.
SELECT * FROM Employees e WHERE EXISTS (SELECT 1 FROM Departments d WHERE d.DepartmentID = e.DepartmentID);

-- Display students whose department exists in the Departments table.
SELECT * FROM Students s WHERE EXISTS (SELECT 1 FROM Departments d WHERE d.DepartmentID = s.DepartmentID);

-- Display customers who have at least one order.
SELECT * FROM Customers c WHERE EXISTS (SELECT 1 FROM Orders o WHERE o.CustomerID = c.CustomerID);

-- Display products that have been ordered at least once.
SELECT * FROM Products p WHERE EXISTS (SELECT 1 FROM OrderDetails od WHERE od.ProductID = p.ProductID);

-- Display employees who have at least one record in the EmployeeProjects table.
SELECT * FROM Employees e WHERE EXISTS (SELECT 1 FROM EmployeeProjects ep WHERE ep.EmployeeID = e.EmployeeID);

-- Display students who have at least one course enrollment.
SELECT * FROM Students s WHERE EXISTS (SELECT 1 FROM Enrollments en WHERE en.StudentID = s.StudentID);

-- Display customers who have at least one payment record.
SELECT * FROM Customers cf WHERE EXISTS (SELECT 1 FROM Payments p WHERE p.CustomerID = c.CustomerID);

-- Display products for which at least one order exists.
SELECT * FROM Products p WHERE EXISTS (SELECT 1 FROM OrderDetails od WHERE od.ProductID = p.ProductID);

-- Display departments that have at least one employee earning more than 50000.
SELECT * FROM Departments d WHERE EXISTS (SELECT 1 FROM Employees e WHERE e.DepartmentID = d.DepartmentID AND e.Salary > 50000);

-- Display employees whose department has at least one employee earning more than 70000.
SELECT * FROM Employees e WHERE EXISTS (SELECT 1 FROM Employees e2 WHERE e2.DepartmentID = e.DepartmentID AND e2.Salary > 70000);

-- Display students whose department has at least one student older than 21.
SELECT * FROM Students s WHERE EXISTS (SELECT 1 FROM Students s2 WHERE s2.DepartmentID = s.DepartmentID AND s2.Age > 21);

-- Display products whose category has at least one product costing more than 50000.
SELECT * FROM Products p WHERE EXISTS (SELECT 1 FROM Products p2 WHERE p2.CategoryID = p.CategoryID AND p2.Price > 50000);

-- Display books whose category has at least one book priced above 1000.
SELECT * FROM Books b WHERE EXISTS (SELECT 1 FROM Books b2 WHERE b2.CategoryID = b.CategoryID AND b2.Price > 1000);

-- Display customers who have placed an order with an order amount greater than 10000.
SELECT * FROM Customers c WHERE EXISTS (SELECT 1 FROM Orders o WHERE o.CustomerID = c.CustomerID AND o.OrderAmount > 10000);

-- Display employees who are assigned to at least one project.
SELECT * FROM Employees e WHERE EXISTS (SELECT 1 FROM EmployeeProjects ep WHERE ep.EmployeeID = e.EmployeeID);

-- Display students who have at least one assignment submitted.
SELECT * FROM Students s WHERE EXISTS (SELECT 1 FROM Assignments a WHERE a.StudentID = s.StudentID AND a.SubmissionDate IS NOT NULL);

-- Display courses that have at least one student enrolled.
SELECT * FROM Courses c WHERE EXISTS (SELECT 1 FROM Enrollments en WHERE en.CourseID = c.CourseID);

-- Display products that have at least one order with quantity greater than 10.
SELECT * FROM Products p WHERE EXISTS (SELECT 1 FROM OrderDetails od WHERE od.ProductID = p.ProductID AND od.Quantity > 10);

-- Display customers who have at least one order placed in 2026.
SELECT * FROM Customers c WHERE EXISTS (SELECT 1 FROM Orders o WHERE o.CustomerID = c.CustomerID AND o.OrderDate >= '2026-01-01' AND o.OrderDate <  '2027-01-01');

-- Display customers who have never placed an order.
SELECT * FROM Customers c WHERE NOT EXISTS (SELECT 1 FROM Orders o WHERE o.CustomerID = c.CustomerID);

-- Display products that have never been ordered.
SELECT * FROM Products p WHERE NOT EXISTS (SELECT 1 FROM OrderDetails od WHERE od.ProductID = p.ProductID);

-- Display employees who are not assigned to any project.
SELECT * FROM Employees e WHERE NOT EXISTS (SELECT 1 FROM EmployeeProjects ep WHERE ep.EmployeeID = e.EmployeeID);

-- Display students who have not enrolled in any course.
SELECT * FROM Students s WHERE NOT EXISTS (SELECT 1 FROM Enrollments en WHERE en.StudentID = s.StudentID);

-- Display courses in which no students are enrolled.
SELECT * FROM Courses c WHERE NOT EXISTS (SELECT 1 FROM Enrollments en WHERE en.CourseID = c.CourseID);

-- Display departments that have no employees.
SELECT * FROM Departments d WHERE NOT EXISTS (SELECT 1 FROM Employees e WHERE e.DepartmentID = d.DepartmentID);

-- Display customers who have no payment records.
SELECT * FROM Customers c WHERE NOT EXISTS (SELECT 1 FROM Payments p WHERE p.CustomerID = c.CustomerID);

-- Display products that have no order records.
SELECT * FROM Products p WHERE NOT EXISTS (SELECT 1 FROM OrderDetails od WHERE od.ProductID = p.ProductID);

-- Display employees who have no project assignments.
SELECT * FROM Employees e WHERE NOT EXISTS (SELECT 1 FROM EmployeeProjects ep WHERE ep.EmployeeID = e.EmployeeID);

-- Display students who have no assignment submissions.
SELECT * FROM Students s WHERE NOT EXISTS (SELECT 1 FROM Assignments a WHERE a.StudentID = s.StudentID AND a.SubmissionDate IS NOT NULL);

-- Display departments where no employee earns more than 70000.
SELECT * FROM Departments d WHERE NOT EXISTS (SELECT 1 FROM Employees e WHERE e.DepartmentID = d.DepartmentID AND e.Salary > 70000);

-- Display employees whose department has no employee earning more than 70000.
SELECT * FROM Employees e WHERE NOT EXISTS (SELECT 1 FROM Employees e2 WHERE e2.DepartmentID = e.DepartmentID AND e2.Salary > 70000);

-- Display products whose category has no product costing more than 50000.
SELECT * FROM Products p WHERE NOT EXISTS (SELECT 1 FROM Products p2 WHERE p2.CategoryID = p.CategoryID AND p2.Price > 50000);

-- Display books whose category has no book priced above 1000.
SELECT * FROM Books b WHERE NOT EXISTS (SELECT 1 FROM Books b2 WHERE b2.CategoryID = b.CategoryID AND b2.Price > 1000);

-- Display customers who have no orders above 10000.
SELECT * FROM Customers c WHERE NOT EXISTS (SELECT 1 FROM Orders o WHERE o.CustomerID = c.CustomerID AND o.OrderAmount > 10000);

-- Display courses with no student enrollment.
SELECT * FROM Courses c WHERE NOT EXISTS (SELECT 1 FROM Enrollments en WHERE en.CourseID = c.CourseID);

-- Display products that were not ordered during 2026.
SELECT * FROM Products p WHERE NOT EXISTS (SELECT 1 FROM OrderDetails od JOIN Orders o ON o.OrderID = od.OrderID WHERE od.ProductID = p.ProductID AND o.OrderDate >= '2026-01-01'
AND o.OrderDate <  '2027-01-01');

-- Display customers who have not placed any order during 2026.
SELECT * FROM Customers C WHERE NOT EXISTS (SELECT 1 FROM Orders o WHERE o.CustomerID = c.CustomerID AND o.OrderDate >= '2026-01-01' AND o.OrderDate <  '2027-01-01');

-- Display employees who have no project assignment with a status of 'Active'.
SELECT * FROM Employees e WHERE NOT EXISTS (SELECT 1 FROM EmployeeProjects ep WHERE ep.EmployeeID = e.EmployeeID AND ep.Status = 'Active');

-- Display students who have no assignment with a status of 'Submitted'.
SELECT * FROM Students s WHERE NOT EXISTS (SELECT 1 FROM Assignments a WHERE a.StudentID = s.StudentID AND a.Status = 'Submitted');
