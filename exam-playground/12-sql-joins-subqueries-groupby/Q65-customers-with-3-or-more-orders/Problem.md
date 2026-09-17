# Q65-customers-with-3-or-more-orders

An online shopping company wants to identify customers who have placed at least three 
orders. 
Write a MySQL query that groups orders by customer and displays only those customers 
whose total number of orders is three or more. 
Input Format 
The first line contains an integer N. 
The next N lines contain: 
order_id customer_id amount 
Output Format 
Display: 
customer_id order_count 
for customers having at least three orders. 
Constraints 
• 
1 ≤ N ≤ 200  
• 
Order IDs are unique.  
• 
Customer IDs are positive integers.  
Sample Input 
7 
1 101 500 
2 102 700 
3 101 400 
4 103 900 
5 101 600 

--- PAGE 55 ---
6 102 300 
7 101 800 
Sample Output 
101 4
