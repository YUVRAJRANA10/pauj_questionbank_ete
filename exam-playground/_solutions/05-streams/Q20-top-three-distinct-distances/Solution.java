import java.util.*;
import java.util.stream.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < n; i++) list.add(sc.nextInt());
        List<Integer> ans = list.stream().distinct().sorted(Comparator.reverseOrder()).limit(3).collect(Collectors.toList());
        for (int i = 0; i < ans.size(); i++) { if (i > 0) System.out.print(" " ); System.out.print(ans.get(i)); }
        System.out.println();
    }
}
