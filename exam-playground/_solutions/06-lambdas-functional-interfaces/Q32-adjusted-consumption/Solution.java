import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        double[] arr = new double[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextDouble();
        for (int i = 0; i < n; i++) { if (i > 0) System.out.print(" " ); System.out.printf("%.2f", arr[i] * 1.10); }
        System.out.println();
    }
}
