import java.util.*;

public class Solution {
    static char calculateGrade(int marks) {
        // TODO: implement the A/B/C/D/F ranges from Problem.md.
        return '?';
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            if (i > 0) System.out.print(" ");
            System.out.print(calculateGrade(sc.nextInt()));
        }
        System.out.println();
    }
}
