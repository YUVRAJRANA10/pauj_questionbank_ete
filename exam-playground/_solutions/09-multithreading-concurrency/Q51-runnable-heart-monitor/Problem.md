# Q51-runnable-heart-monitor

A hospital monitoring system receives heart-rate readings from a patient-monitoring device. 
The readings must be processed by a separate thread created using the Runnable interface. 
Write a Java program that implements Runnable and creates a thread to display each heart-
rate reading. 
Input Format 
The first line contains the number of readings. 
The second line contains N heart-rate readings separated by spaces. 
Output Format 
For every reading, print: 
Monitoring: <reading> 
Each reading should be printed on a separate line. 
Code Constraints 
1 ≤ N ≤ 100 
40 ≤ Reading ≤ 200 
Sample Input 
3 
72 80 76 
Sample Output 
Monitoring: 72 
Monitoring: 80 
Monitoring: 76
