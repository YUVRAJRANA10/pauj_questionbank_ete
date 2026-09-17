import java.util.*;
public class Solution {
    static int total(int a, int b, int c) { return a + b + c; }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(); int b = sc.nextInt(); int c = sc.nextInt();
        System.out.println(total(a, b, c));
    }
}
