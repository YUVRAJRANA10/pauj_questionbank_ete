import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Map<Integer, String> map = new HashMap<>();
        for (int i = 0; i < n; i++) map.put(sc.nextInt(), sc.next());
        int key = sc.nextInt();
        System.out.println(map.getOrDefault(key, "Employee Not Found"));
    }
}
