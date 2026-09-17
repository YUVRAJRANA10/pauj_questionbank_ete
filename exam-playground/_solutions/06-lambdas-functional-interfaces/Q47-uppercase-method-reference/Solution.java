import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String[] arr = new String[n];
        for (int i = 0; i < n; i++) arr[i] = sc.next();
        for (int i = 0; i < n; i++) { if (i > 0) System.out.print(" " ); System.out.print(arr[i].toUpperCase()); }
        System.out.println();
    }
}
