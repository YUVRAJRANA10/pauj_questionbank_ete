CREATE TABLE Employees (employee_id INT PRIMARY KEY, employee_name VARCHAR(50), manager_id INT NULL);
INSERT INTO Employees VALUES (101, 'Amit', NULL);
INSERT INTO Employees VALUES (102, 'Neha', 101);
INSERT INTO Employees VALUES (103, 'Rahul', 101);
INSERT INTO Employees VALUES (104, 'Simran', 102);
