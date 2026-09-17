# Q56-livelock-retry-management

A communication system has two threads that need to send messages through a shared 
communication channel. The threads repeatedly give way to each other instead of 
proceeding, which can result in a livelock. 
Write a Java program that simulates a limited number of retry attempts. After the specified 
number of attempts, the communication should proceed successfully. 

--- PAGE 46 ---
Input Format 
The first line contains the maximum number of retry attempts. 
Output Format 
Print: 
Communication Started 
For every unsuccessful retry, print: 
Retrying 
When communication succeeds, print: 
Message Sent Successfully 
Communication Completed 
Code Constraints 
1 ≤ Attempts ≤ 10 
Sample Input 
3 
Sample Output 
Communication Started 
Retrying 
Retrying 
Message Sent Successfully 
Communication Completed
