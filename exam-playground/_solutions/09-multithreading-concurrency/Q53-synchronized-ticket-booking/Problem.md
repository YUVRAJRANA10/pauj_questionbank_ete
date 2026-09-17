# Q53-synchronized-ticket-booking

A movie-ticket booking system maintains a shared number of available tickets. Two booking 
threads attempt to reserve tickets simultaneously. 
Write a Java program that uses a synchronized block to protect the critical section where 
tickets are booked. 
Each successful booking decreases the available ticket count by one. If there are not enough 
tickets, no additional tickets should be booked. 
Input Format 
The first line contains the initial number of tickets. 

--- PAGE 44 ---
The second line contains the number of booking requests. 
Output Format 
Print: 
Tickets Remaining: <number> 
Code Constraints 
0 ≤ Tickets ≤ 10000 
0 ≤ Requests ≤ 10000 
Sample Input 
10 
6 
Sample Output 
Tickets Remaining: 4
