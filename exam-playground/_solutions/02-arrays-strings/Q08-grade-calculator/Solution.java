import java.util.*;
public class Solution {
    static char calculateGrade(int marks) {
        if (marks >= 90) return 'A';
        if (marks >= 75) return 'B';
        if (marks >= 60) return 'C';
        if (marks >= 40) return 'D';
        return 'F';
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) { if (i > 0) System.out.print(" " ); System.out.print(calculateGrade(sc.nextInt())); }
        System.out.println();
    }
}
