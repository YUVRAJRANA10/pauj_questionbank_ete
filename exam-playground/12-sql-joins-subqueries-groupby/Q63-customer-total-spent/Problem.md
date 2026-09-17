# Q63-customer-total-spent

An online shopping system stores orders placed by customers. The company wants to 
calculate the total amount spent by each customer. 
Write a MySQL query that groups the orders by customer and calculates the total order 
amount for every customer. 
Input Format 
The first line contains an integer N. 
The next N lines contain: 
order_id customer_id amount 
Output Format 
Display: 
customer_id total_amount 
in ascending order of customer_id. 
Constraints 
• 
1 ≤ N ≤ 100  
• 
Amount is a positive integer.  
Sample Input 
5 
1 101 1200 
2 102 800 
3 101 1500 

--- PAGE 53 ---
4 103 2000 
5 102 700 
Sample Output 
101 2700 
102 1500 
103 2000
