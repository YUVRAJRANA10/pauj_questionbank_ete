# Q59-students-create-and-list

--- PAGE 48 ---
A university is developing a student management system. The database must store student 
information while ensuring that important data follows appropriate rules. 
Create a MySQL table named Students with the following fields: 
• 
student_id  
• 
student_name  
• 
email  
• 
age  
• 
course  
The table must ensure that student_id is the primary key, student_name cannot be NULL, 
email is unique, and age must be between 17 and 60. 
After creating the table, insert the given student records and display all records in ascending 
order of student_id. 
Input Format 
The first line contains an integer N, representing the number of students. 
The next N lines contain: 
student_id student_name email age course 
Output Format 
Display all student records in ascending order of student_id. 
Constraints 
• 
1 ≤ N ≤ 100  
• 
17 ≤ age ≤ 60  
• 
student_id is unique.  
• 
Email addresses are unique.  
• 
Student names and course names contain no spaces.  
Sample Input 
3 
101 Amit amit@gmail.com 20 CSE 
102 Neha neha@gmail.com 21 ECE 
103 Rahul rahul@gmail.com 22 CSE 

--- PAGE 49 ---
Sample Output 
101 Amit amit@gmail.com 20 CSE 
102 Neha neha@gmail.com 21 ECE 
103 Rahul rahul@gmail.com 22 CSE
