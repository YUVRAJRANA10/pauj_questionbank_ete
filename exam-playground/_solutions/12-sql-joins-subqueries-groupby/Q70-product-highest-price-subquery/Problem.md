# Q70-product-highest-price-subquery

An online store wants to find the product or products having the highest price. 
Write a MySQL query using a subquery to display all products whose price is equal to the 
maximum product price. 
Input Format 
The first line contains an integer N. 
The next N lines contain: 
product_id product_name price 
Output Format 
Display: 
product_name price 
for every product having the maximum price. 
Constraints 
• 
1 ≤ N ≤ 100  
• 
Price is a positive integer.  
• 
More than one product may have the same maximum price.  
Sample Input 
5 
101 Laptop 60000 
102 Phone 40000 
103 Monitor 15000 

--- PAGE 60 ---
104 Tablet 30000 
105 Camera 60000 
Sample Output 
Laptop 60000 
Camera 60000
