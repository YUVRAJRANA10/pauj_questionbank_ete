# Q14-hashmap-product-quantity-total

An inventory system maintains product IDs and their quantities using a HashMap. A manager 
wants to calculate the total quantity available for a particular product category represented 
by a set of product IDs. 
Write a Java program to store product ID and quantity pairs in a HashMap. Given M product 
IDs, calculate the total quantity of those products. If a product ID is not present in the map, 
its quantity should not be included. 
Input Format 

--- PAGE 11 ---
The first line contains N. 
The next N lines contain product ID and quantity. 
The next line contains M. 
The following line contains M product IDs. 
Output Format 
Print the total quantity of the specified products. 
Code Constraints 
1 ≤ N ≤ 1000 
1 ≤ M ≤ 100 
1 ≤ Product ID ≤ 100000 
0 ≤ Quantity ≤ 10000 
Sample Input 
5 
101 20 
102 35 
103 15 
104 50 
105 25 
4 
101 103 105 110 
Sample Output 
60
