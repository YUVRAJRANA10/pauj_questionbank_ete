import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int nextEven = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] % 2 == 0) {
                int value = arr[i];
                for (int j = i; j > nextEven; j--) arr[j] = arr[j - 1];
                arr[nextEven++] = value;
            }
        }
        for (int i = 0; i < n; i++) { if (i > 0) System.out.print(" " ); System.out.print(arr[i]); }
        System.out.println();
    }
}
