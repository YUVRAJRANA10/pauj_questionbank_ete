import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        TreeSet<Integer> set = new TreeSet<>();
        for (int i = 0; i < n; i++) set.add(sc.nextInt());
        int target = sc.nextInt();
        Integer floor = set.floor(target - 1);
        System.out.println(floor == null ? -1 : floor);
    }
}
