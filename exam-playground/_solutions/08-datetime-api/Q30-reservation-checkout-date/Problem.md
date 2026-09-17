# Q30-reservation-checkout-date

A hotel reservation system records the date on which a guest checks in and the number of 
nights included in the reservation. The system also records how many nights the guest has 
already stayed. 
Develop a Java program using the Java Date-Time API to process the reservation details and 
determine the reservation status. 
The program must: 
Calculate the checkout date by adding the complete reservation period to the check-in date. 
Determine the number of nights remaining by subtracting the nights already stayed from the 
total number of reserved nights. 
Extract and display the year and month from the calculated checkout date. 
Use the LocalDate class for all date calculations. 
Input Format 
The input consists of three lines: 
The first line contains the check-in date in the format yyyy-MM-dd. 
The second line contains the total number of nights reserved. 
The third line contains the number of nights already stayed. 
Output Format 
Print the following information on separate lines in the specified order: 
Checkout date 
Remaining nights 
Year of the checkout date 
Month of the checkout date 
Code Constraints 
The check-in date is valid. 

--- PAGE 28 ---
1 ≤ totalNights ≤ 365 
0 ≤ stayedNights < totalNights 
Year is between 2020 and 2030. 
Sample Input 
2026-08-10 
30 
12 
Sample Output 
2026-09-09 
18 
2026 
9
