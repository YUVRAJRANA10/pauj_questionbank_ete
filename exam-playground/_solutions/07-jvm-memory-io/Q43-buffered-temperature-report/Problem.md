# Q43-buffered-temperature-report

--- PAGE 37 ---
A weather-monitoring system receives temperature readings continuously. Instead of 
printing each processed reading immediately, the system should construct the complete 
report using buffering. 
For each temperature, calculate: 
Processed Temperature = Temperature + 2 
Use BufferedReader for input and StringBuilder for constructing the output. 
Input Format 
The first line contains N. 
The second line contains N temperature readings. 
Output Format 
Print the processed temperatures separated by spaces. 
Code Constraints 
1 ≤ N ≤ 100000 
−100 ≤ Temperature ≤ 100 
Sample Input 
4 
20 25 30 35 
Sample Output 
22 27 32 37
