# Q17-withdrawal-validation

A banking application accepts a withdrawal amount from a customer's account. A 
withdrawal is valid only when the amount is positive and does not exceed the available 
balance. 
Write a Java program using try-catch-finally to perform the withdrawal. Handle invalid 
withdrawal amounts and insufficient balance without terminating the program 
unexpectedly. 
If the withdrawal is valid, print the remaining balance. 
If the amount is invalid, print Invalid Amount. 
If the amount exceeds the balance, print Insufficient Balance. 
Input Format 
The first line contains the account balance. 
The second line contains the withdrawal amount. 
Output Format 
Print the remaining balance or the appropriate error message. 
Code Constraints 
0 ≤ Balance ≤ 1000000 
−1000 ≤ Withdrawal Amount ≤ 1000000 
Sample Input 
25000 
7500 
Sample Output 
17500
