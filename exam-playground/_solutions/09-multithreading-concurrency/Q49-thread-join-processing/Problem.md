# Q49-thread-join-processing

A railway ticketing system processes a number of ticket requests using a separate thread. 
The system should start the ticket-processing thread, allow it to process all requests, and 
wait for the thread to complete before the main program continues. 
Write a Java program that creates a thread to process the given number of ticket requests. 
The thread should print the number of processed requests. The main thread must wait for 
the ticket-processing thread to complete using join(). 
Input Format 
The first line contains the number of ticket requests. 
Output Format 
The thread should print the number of processed tickets. After the thread completes, print 
Processing Completed. 
Code Constraints 
0 ≤ N ≤ 1000 
Sample Input 
5 
Sample Output 
Tickets Processed: 5 
Processing Completed
