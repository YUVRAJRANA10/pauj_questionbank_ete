import java.util.*;
@FunctionalInterface
interface SafetyCheck { boolean apply(int temp); }
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        SafetyCheck check = t -> t >= 20 && t <= 80;
        for (int i = 0; i < n; i++) { if (i > 0) System.out.print(" " ); System.out.print(check.apply(sc.nextInt()) ? "Safe" : "Unsafe"); }
        System.out.println();
    }
}
