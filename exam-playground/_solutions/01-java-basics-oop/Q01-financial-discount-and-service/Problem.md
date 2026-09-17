# Q01-financial-discount-and-service

A financial application calculates the final amount payable by a customer after applying a 
discount and a service charge. The application receives the original amount as an integer 
and the discount and service charge as decimal percentages. 
The final amount is calculated as: 
Final Amount = Original Amount − Discount + Service Charge 
where: 
Discount = Original Amount × Discount Percentage / 100 
Service Charge = Amount after Discount × Service Charge Percentage / 100 
Write a Java program to calculate and display the final amount rounded to two decimal 
places. The program should use appropriate primitive data types to avoid loss of decimal 
precision during the calculation. 
Input Format 
The first line contains an integer representing the original amount. 
The second line contains a decimal value representing the discount percentage. 
The third line contains a decimal value representing the service charge percentage. 
Output Format 
Print the final amount rounded to two decimal places. 
Code Constraints 
1 ≤ Original Amount ≤ 1000000 
0 ≤ Discount Percentage ≤ 100 
0 ≤ Service Charge Percentage ≤ 20 
Sample Input 
5000 
10.5 
5.0 
Sample Output 
4712.50 
 
 

--- PAGE 2 ---
