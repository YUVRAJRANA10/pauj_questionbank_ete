# Q62-department-student-count

A university stores student information along with the department in which each student is 
enrolled. The administration wants to know how many students belong to each department. 
Write a MySQL query that groups students according to their department and calculates the 
number of students in each department. 
Input Format 
The first line contains an integer N. 
The next N lines contain: 
student_id student_name department 
Output Format 
Display: 
department student_count 
in alphabetical order of department. 
Constraints 
• 
1 ≤ N ≤ 100  
• 
Each student belongs to one department.  
• 
Department names contain no spaces.  
Sample Input 
6 
101 Amit CSE 
102 Neha ECE 

--- PAGE 52 ---
103 Rahul CSE 
104 Simran IT 
105 Karan CSE 
106 Priya ECE 
Sample Output 
CSE 3 
ECE 2 
IT 1
