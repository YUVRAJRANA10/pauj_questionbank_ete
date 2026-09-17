# Q52-synchronized-withdrawal

A bank account is accessed by two withdrawal requests running in separate threads. Both 
requests operate on the same account balance. 

--- PAGE 43 ---
Write a Java program using a synchronized withdrawal method so that only one thread can 
modify the account balance at a time. 
If sufficient balance is available, the amount should be withdrawn. Otherwise, print 
Insufficient Balance. 
Input Format 
The first line contains the initial account balance. 
The second line contains the withdrawal amount requested by the first thread. 
The third line contains the withdrawal amount requested by the second thread. 
Output Format 
If a withdrawal cannot be completed, print Insufficient Balance. 
After both threads finish, print: 
Final Balance: <balance> 
Code Constraints 
0 ≤ Balance ≤ 1000000 
0 ≤ Withdrawal Amount ≤ 1000000 
Sample Input 
10000 
3000 
4000 
Sample Output 
Final Balance: 3000
