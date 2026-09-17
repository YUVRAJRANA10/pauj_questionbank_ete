# Q69-self-join-manager-list

A company stores managers and employees in the same Employees table. Each employee 
record contains the ID of their manager. 
Write a MySQL query using a self join to display every employee along with the name of 
their manager. 
Employees who do not have a manager should also be included. 
Input Format 
The database contains: 
employee_id 
employee_name 
manager_id 
Output Format 
Display: 
employee_name manager_name 
in ascending order of employee ID. 
Sample Input 
101 Amit NULL 
102 Neha 101 

--- PAGE 59 ---
103 Rahul 101 
104 Simran 102 
Sample Output 
Amit NULL 
Neha Amit 
Rahul Amit 
Simran Neha
