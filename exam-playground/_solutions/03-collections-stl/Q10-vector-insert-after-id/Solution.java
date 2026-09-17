import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Vector<Integer> containers = new Vector<>();
        for (int i = 0; i < n; i++) containers.add(sc.nextInt());
        int existingId = sc.nextInt();
        int newId = sc.nextInt();
        int index = containers.indexOf(existingId);
        if (index < 0) {
            System.out.println("Container Not Found");
        } else {
            containers.add(index + 1, newId);
            for (int i = 0; i < containers.size(); i++) {
                if (i > 0) System.out.print(" ");
                System.out.print(containers.get(i));
            }
            System.out.println();
        }
    }
}
