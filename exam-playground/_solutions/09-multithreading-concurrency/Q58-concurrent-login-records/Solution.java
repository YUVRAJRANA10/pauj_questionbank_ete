import java.util.*;
import java.util.concurrent.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(); int b = sc.nextInt();
        Set<String> set = ConcurrentHashMap.newKeySet();
        for (int i = 0; i < a; i++) set.add("login-" + i);
        for (int i = 0; i < b; i++) set.add("login-" + (a + i));
        System.out.println("Total Login Records: " + set.size());
    }
}
