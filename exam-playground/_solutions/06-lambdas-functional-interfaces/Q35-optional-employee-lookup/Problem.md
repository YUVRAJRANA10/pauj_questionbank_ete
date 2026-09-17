# Q35-optional-employee-lookup

An employee management system searches for an employee name using an employee ID. If 
the employee exists, the system should display the employee name. If the ID is not found, it 
should display Employee Not Found. 

--- PAGE 32 ---
Write a Java program using Optional to safely handle the possibility of a missing employee 
without directly checking for a null value. 
Input Format 
The first line contains the number of employees. 
The next N lines contain employee ID and employee name. 
The last line contains the ID to search. 
Output Format 
Print the employee name if the ID exists. Otherwise, print Employee Not Found. 
Code Constraints 
1 ≤ N ≤ 100 
1 ≤ Employee ID ≤ 100000 
Sample Input 
3 
101 Amit 
102 Neha 
103 Rahul 
102 
Sample Output 
Neha
