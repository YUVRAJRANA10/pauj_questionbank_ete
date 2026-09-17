import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        LinkedList<Integer> list = new LinkedList<>();
        for (int i = 0; i < n; i++) list.add(sc.nextInt());
        int target = sc.nextInt();
        if (!list.removeFirstOccurrence(target)) System.out.println("Task Not Found");
        else { for (int i = 0; i < list.size(); i++) { if (i > 0) System.out.print(" " ); System.out.print(list.get(i)); } System.out.println(); }
    }
}
