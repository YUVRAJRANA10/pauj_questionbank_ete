import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(); int b = sc.nextInt(); int c = sc.nextInt();
        int[] arr = new int[]{sc.nextInt(), sc.nextInt(), sc.nextInt()};
        System.out.println(a + " " + b + " " + c);
        for (int i = 0; i < arr.length; i++) { if (i > 0) System.out.print(" " ); System.out.print(arr[i]); }
        System.out.println();
    }
}
