# Q09-cancel-divisible-token-numbers

A hospital maintains the token numbers of patients waiting for registration using an 
ArrayList. During registration, some token numbers are cancelled. 

--- PAGE 7 ---
Write a Java program to store the token numbers in an ArrayList, remove all token numbers 
that are divisible by a given cancellation number, and display the remaining token numbers 
in their original order. 
Input Format 
The first line contains an integer N. 
The second line contains N space-separated token numbers. 
The third line contains the cancellation number. 
Output Format 
Print the remaining token numbers separated by a single space. 
If no token remains, print -1. 
Code Constraints 
1 ≤ N ≤ 1000 
1 ≤ Token Number ≤ 100000 
1 ≤ Cancellation Number ≤ 100 
Sample Input 
8 
12 15 18 21 24 25 30 31 
3 
Sample Output 
15 25 31
