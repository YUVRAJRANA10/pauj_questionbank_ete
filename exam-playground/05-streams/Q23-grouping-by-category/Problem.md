# Q23-grouping-by-category

A university maintains student marks and wants to prepare a summary using the Stream API. 
Each mark must be classified into one of three categories: 
• 
High → marks ≥ 75  
• 
Medium → marks between 50 and 74  
• 
Low → marks below 50  
Use Collectors.groupingBy() to group the marks according to these categories and display 
the number of students in each category. 
Input Format 
The first line contains N. 
The second line contains N space-separated marks. 
Output Format 
Print: 
High: count 
Medium: count 
Low: count 
on separate lines. 
Code Constraints 
1 ≤ N ≤ 1000 
0 ≤ Marks ≤ 100 
Sample Input 
8 
82 45 67 91 38 75 54 49 
Sample Output 

--- PAGE 18 ---
High: 3 
Medium: 2 
Low: 3
