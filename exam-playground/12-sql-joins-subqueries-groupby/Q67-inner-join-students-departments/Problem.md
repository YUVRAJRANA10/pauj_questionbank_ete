# Q67-inner-join-students-departments

A university stores student details in one table and department details in another table. 
The Students table contains student information and Departments contains department 
information. Write a MySQL query using an inner join to display each student's name along 
with the corresponding department name. 
Input Format 
The database contains the following information: 
Students 
student_id 
student_name 
department_id 
 
Departments 
department_id 
department_name 
Output Format 
Display: 
student_name department_name 
in ascending order of student_id. 
Constraints 
• 
Every student has a valid department.  
• 
department_id uniquely identifies a department.  
Sample Input 
Students 
101 Amit 10 
102 Neha 20 
103 Rahul 10 

--- PAGE 57 ---
 
Departments 
10 CSE 
20 ECE 
Sample Output 
Amit CSE 
Neha ECE 
Rahul CSE
