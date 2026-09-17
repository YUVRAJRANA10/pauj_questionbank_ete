import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int idx = sc.nextInt();
        int div = sc.nextInt();
        try {
            System.out.println(arr[idx] / div);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Invalid Index");
        } catch (ArithmeticException e) {
            System.out.println("Division By Zero");
        }
    }
}
