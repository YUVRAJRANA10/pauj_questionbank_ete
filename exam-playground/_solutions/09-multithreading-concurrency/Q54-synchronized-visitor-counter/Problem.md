# Q54-synchronized-visitor-counter

A website maintains a shared visitor counter. Two threads represent two groups of visitors, 
and each thread increments the same counter. 
Without proper synchronization, simultaneous updates can cause a race condition and 
produce an incorrect count. 
Write a Java program that safely updates the shared counter using synchronization so that 
every visitor is counted. 
Input Format 
The first line contains the number of visitors handled by the first thread. 
The second line contains the number of visitors handled by the second thread. 
Output Format 
Print: 
Total Visitors: <number> 
Code Constraints 
0 ≤ N ≤ 100000 
Sample Input 
5000 
7000 

--- PAGE 45 ---
Sample Output 
Total Visitors: 12000
