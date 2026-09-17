import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Vector<Integer> items = new Vector<>();
        for (int i = 0; i < n; i++) items.add(sc.nextInt());
        int target = sc.nextInt();
        int value = sc.nextInt();
        int idx = -1;
        for (int i = 0; i < items.size(); i++) { if (items.get(i) == target) { idx = i; break; } }
        if (idx == -1) System.out.println("Container Not Found");
        else { items.add(idx + 1, value); for (int i = 0; i < items.size(); i++) { if (i > 0) System.out.print(" " ); System.out.print(items.get(i)); } System.out.println(); }
    }
}
