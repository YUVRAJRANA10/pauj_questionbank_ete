import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Map<Integer, String> names = new LinkedHashMap<>();
        for (int i = 0; i < n; i++) { int id = sc.nextInt(); String name = sc.next(); int dept = sc.nextInt(); String dname = sc.next(); names.putIfAbsent(id, name + " " + dname); }
        for (Map.Entry<Integer, String> e : names.entrySet()) System.out.println(e.getKey() + " " + e.getValue());
    }
}
