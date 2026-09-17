import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long[] arr = new long[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextLong();
        for (int i = 0; i < n; i++) { if (i > 0) System.out.print(" " ); System.out.print(arr[i] * 1000L); }
        System.out.println();
    }
}
