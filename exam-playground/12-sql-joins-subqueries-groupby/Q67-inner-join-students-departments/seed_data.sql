CREATE TABLE Students (student_id INT PRIMARY KEY, student_name VARCHAR(50), department_id INT);
CREATE TABLE Departments (department_id INT PRIMARY KEY, department_name VARCHAR(50));
INSERT INTO Departments VALUES (1, 'CSE');
INSERT INTO Departments VALUES (2, 'ECE');
INSERT INTO Students VALUES (101, 'Amit', 1);
INSERT INTO Students VALUES (102, 'Neha', 2);
INSERT INTO Students VALUES (103, 'Rahul', 1);
