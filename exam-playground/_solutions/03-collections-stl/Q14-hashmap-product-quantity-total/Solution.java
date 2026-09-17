import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) { map.put(sc.nextInt(), sc.nextInt()); }
        int q = sc.nextInt();
        int total = 0;
        for (int i = 0; i < q; i++) total += map.getOrDefault(sc.nextInt(), 0);
        System.out.println(total);
    }
}
