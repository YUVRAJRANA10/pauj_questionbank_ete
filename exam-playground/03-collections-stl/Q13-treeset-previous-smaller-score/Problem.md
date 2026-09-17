# Q13-treeset-previous-smaller-score

--- PAGE 10 ---
A company maintains employee performance scores. The scores must be stored in a TreeSet 
so that duplicate scores are automatically removed and the remaining scores are maintained 
in sorted order. 
The management wants to find the highest score that is strictly less than a given target 
score. 
Write a Java program using TreeSet to perform this operation. If no such score exists, print -
1. 
Input Format 
The first line contains an integer N. 
The second line contains N space-separated scores. 
The third line contains the target score. 
Output Format 
Print the greatest score smaller than the target score. 
Code Constraints 
1 ≤ N ≤ 1000 
0 ≤ Score ≤ 100 
0 ≤ Target Score ≤ 100 
Sample Input 
8 
45 72 88 65 72 91 54 80 
75 
Sample Output 
72
