CREATE TABLE Employees (employee_id INT PRIMARY KEY, employee_name VARCHAR(50), department_id INT);
CREATE TABLE Departments (department_id INT PRIMARY KEY, department_name VARCHAR(50));
INSERT INTO Departments VALUES (1, 'CSE');
INSERT INTO Departments VALUES (2, 'ECE');
INSERT INTO Employees VALUES (101, 'Amit', 1);
INSERT INTO Employees VALUES (102, 'Neha', 2);
INSERT INTO Employees VALUES (103, 'Rahul', NULL);
