import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long[] weightsInGrams = new long[n];
        for (int i = 0; i < n; i++) {
            long kilograms = sc.nextLong();
            // TODO: convert kilograms to grams without integer overflow.
            weightsInGrams[i] = 0;
        }
        for (int i = 0; i < n; i++) {
            if (i > 0) System.out.print(" ");
            System.out.print(weightsInGrams[i]);
        }
        System.out.println();
    }
}
