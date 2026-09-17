# Q55-deadlock-prevention

A manufacturing system has two shared resources required by two processing threads. If the 
threads acquire the resources in different orders, they may wait indefinitely for each other, 
resulting in a deadlock. 
Write a Java program that uses two shared resources and ensures that both threads acquire 
the resources in the same order. This prevents deadlock and allows both operations to 
complete successfully. 
Input Format 
The first line contains the number of units processed by Thread 1. 
The second line contains the number of units processed by Thread 2. 
Output Format 
Print: 
Thread 1 Completed 
Thread 2 Completed 
Production Completed 
Code Constraints 
1 ≤ N ≤ 1000 
Sample Input 
10 
20 
Sample Output 
Thread 1 Completed 
Thread 2 Completed 
Production Completed
