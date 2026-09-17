CREATE TABLE Students (student_id INT PRIMARY KEY, student_name VARCHAR(50) NOT NULL, email VARCHAR(100) UNIQUE, age INT CHECK (age BETWEEN 17 AND 60), course VARCHAR(50));
INSERT INTO Students VALUES (101, 'Amit', 'amit@gmail.com', 20, 'CSE');
INSERT INTO Students VALUES (102, 'Neha', 'neha@gmail.com', 21, 'ECE');
INSERT INTO Students VALUES (103, 'Rahul', 'rahul@gmail.com', 22, 'CSE');
