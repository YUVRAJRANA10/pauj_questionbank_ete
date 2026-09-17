# Q39-garbage-collection-request

A document-processing application creates temporary String objects while processing 
documents. After the objects are no longer required, the application requests the JVM to 
perform garbage collection. 
Write a Java program that creates a specified number of temporary objects, removes their 
references, requests garbage collection using the appropriate JVM method, and finally prints 
Garbage Collection Requested. 
Input Format 
The first line contains the number of temporary objects. 
Output Format 
Print: 
Garbage Collection Requested 
Code Constraints 
1 ≤ N ≤ 10000 
Sample Input 
100 
Sample Output 

--- PAGE 35 ---
Garbage Collection Requested
