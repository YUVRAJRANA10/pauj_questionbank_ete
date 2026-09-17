# Q31-exam-end-time

A college examination system records the date and starting time of an examination. The 
examination lasts for a specified number of minutes. 
Develop a Java program using the Java Date-Time API to determine the examination's ending 
date and time. 
The program must: 
Read the examination date using LocalDate. 
Read the examination start time using LocalTime. 
Combine the date and time using LocalDateTime. 
Add the given examination duration in minutes. 
Display the resulting ending date and time. 
Display the year, month, and hour of the examination end time. 
Use LocalDate, LocalTime, and LocalDateTime for the required operations. 
Input Format 
The input consists of three lines: 
 

--- PAGE 29 ---
The first line contains the examination date in the format yyyy-MM-dd. 
The second line contains the examination start time in the format HH:mm. 
The third line contains the examination duration in minutes. 
Constraints 
The examination date is valid. 
Time is provided in 24-hour format. 
30 ≤ duration ≤ 300. 
Year is between 2020 and 2030. 
Output Format 
Print the following on separate lines: 
Examination end date 
Examination end time 
Year of the end date 
Month of the end date 
Hour of the end time 
Sample Input 
2026-09-14 
22:30 
120 
Sample Output 
2026-09-15 
00:30 
2026 
9 
0
