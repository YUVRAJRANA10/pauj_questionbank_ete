# Q68-left-join-employees-departments

A company wants to generate a report containing every employee, including employees who 
have not yet been assigned to a department. 
Write a MySQL query using a left join to display the employee name and department name. 
If an employee has no department, the department value should appear as NULL. 
Input Format 
The database contains: 
Employees 
employee_id 
employee_name 
department_id 
 
Departments 
department_id 
department_name 
Output Format 
Display: 
employee_name department_name 
in ascending order of employee_id. 
Sample Input 
Employees 

--- PAGE 58 ---
101 Amit 10 
102 Neha NULL 
103 Rahul 20 
 
Departments 
10 CSE 
20 ECE 
Sample Output 
Amit CSE 
Neha NULL 
Rahul ECE
