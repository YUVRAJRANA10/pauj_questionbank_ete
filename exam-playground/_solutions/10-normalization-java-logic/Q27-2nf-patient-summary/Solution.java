import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Map<Integer, String> names = new LinkedHashMap<>();
        Map<Integer, Integer> counts = new LinkedHashMap<>();
        for (int i = 0; i < n; i++) {
            int a = sc.nextInt();
            String name = sc.next();
            int b = sc.nextInt();
            sc.next();
            sc.next();
            names.putIfAbsent(a, name);
            counts.put(a, counts.getOrDefault(a, 0) + 1);
        }
        for (Map.Entry<Integer, Integer> e : counts.entrySet()) {
            System.out.println(e.getKey() + " " + names.get(e.getKey()) + " " + e.getValue());
        }
    }
}
