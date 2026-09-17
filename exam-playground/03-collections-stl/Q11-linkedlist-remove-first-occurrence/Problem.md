# Q11-linkedlist-remove-first-occurrence

A task management application maintains pending task IDs using a LinkedList. The system 
receives a task ID that has been completed and must remove its first occurrence from the 
list. 
Write a Java program to search for the given task ID and remove its first occurrence. If the 
task ID does not exist, print Task Not Found. 
Input Format 
The first line contains an integer N. 
The second line contains N space-separated task IDs. 
The third line contains the task ID to be removed. 
Output Format 
Print the updated list if the task exists. 
Otherwise, print Task Not Found. 
Code Constraints 

--- PAGE 9 ---
1 ≤ N ≤ 1000 
1 ≤ Task ID ≤ 1000000 
Sample Input 
7 
101 205 310 205 415 520 610 
205 
Sample Output 
101 310 205 415 520 610
