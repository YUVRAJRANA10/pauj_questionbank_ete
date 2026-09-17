# Q61-book-price-deletion

A library maintains details of its books, including book ID, title, author, and price. The 
librarian wants to remove all books whose price is below a specified minimum price. 
Delete all books whose price is less than the given minimum price and display the remaining 
books in ascending order of book_id. 
Input Format 
The first line contains an integer N, representing the number of books. 
The next N lines contain: 
book_id title author price 
The final line contains the minimum acceptable price. 
Output Format 
Display the remaining books as: 
book_id title author price 
in ascending order of book_id. 
Constraints 
• 
1 ≤ N ≤ 100  
• 
Price is a positive integer.  
• 
Book titles and author names contain no spaces.  
Sample Input 
5 
101 Java James 550 
102 SQL Korth 250 

--- PAGE 51 ---
103 Python Rossum 650 
104 Networks Tanenbaum 300 
105 OS Galvin 200 
300 
Sample Output 
101 Java James 550 
103 Python Rossum 650 
104 Networks Tanenbaum 300
