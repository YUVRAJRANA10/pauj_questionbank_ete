import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        for (int i = 0; i < n; i++) { if (i > 0) System.out.print(" " ); System.out.print(arr[i] >= 1000 ? Math.round(arr[i] * 0.85f) : Math.round(arr[i] * 0.95f)); }
        System.out.println();
    }
}
