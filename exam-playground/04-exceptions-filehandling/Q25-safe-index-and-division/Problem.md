# Q25-safe-index-and-division

A data processing system receives two integers and uses the first integer as an array index 
and the second integer as a divisor. 
Write a Java program using exception handling to manage both an invalid array index and 
division by zero. Use appropriate exception classes from Java's exception hierarchy and 
handle each situation separately. 
If the index is invalid, print: 
Invalid Index 
If the divisor is zero, print: 

--- PAGE 19 ---
Division By Zero 
Otherwise, print the value at the specified index divided by the divisor. 
Input Format 
The first line contains N. 
The second line contains N integers. 
The third line contains the index. 
The fourth line contains the divisor. 
Output Format 
Print the calculated result or the appropriate exception message. 
Code Constraints 
1 ≤ N ≤ 100 
−1000 ≤ Array Element ≤ 1000 
−100 ≤ Index ≤ 100 
−100 ≤ Divisor ≤ 100 
Sample Input 
5 
20 40 60 80 100 
2 
10 
Sample Output 
6
