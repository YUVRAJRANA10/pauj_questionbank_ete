import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] production = new int[n];
        for (int i = 0; i < n; i++) production[i] = sc.nextInt();
        int total = 0;
        int minimum = Integer.MAX_VALUE;
        int maximum = Integer.MIN_VALUE;
        for (int value : production) {
            // TODO: update total, minimum, and maximum.
        }
        System.out.println(total);
        System.out.printf("%.2f%n", (double) total / n);
        System.out.println(maximum - minimum);
    }
}
