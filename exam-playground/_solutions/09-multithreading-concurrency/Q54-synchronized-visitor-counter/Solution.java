import java.util.*;
class Counter { private int count = 0; synchronized void add(int n) { count += n; } int value() { return count; } }
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Counter c = new Counter();
        c.add(sc.nextInt()); c.add(sc.nextInt());
        System.out.println("Total Visitors: " + c.value());
    }
}
