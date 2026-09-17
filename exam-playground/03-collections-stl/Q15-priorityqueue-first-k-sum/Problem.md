# Q15-priorityqueue-first-k-sum

A service center assigns a priority number to each service request. A smaller number 
represents a higher priority. However, requests having the same priority must also be 
processed. 
Using a PriorityQueue, process all requests and calculate the sum of the first K priorities that 
are processed. 
Input Format 
The first line contains N. 

--- PAGE 12 ---
The second line contains N priority numbers. 
The third line contains K. 
Output Format 
Print the sum of the first K priorities removed from the PriorityQueue. 
Code Constraints 
1 ≤ K ≤ N ≤ 1000 
1 ≤ Priority ≤ 100000 
Sample Input 
7 
18 5 12 30 9 25 3 
3 
Sample Output 
17
