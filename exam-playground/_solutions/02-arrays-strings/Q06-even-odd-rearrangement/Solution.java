import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] values = new int[n];
        for (int i = 0; i < n; i++) values[i] = sc.nextInt();
        // TODO: rearrange in place while preserving order within each group.
        for (int value : values) {
            if (value % 2 == 0) System.out.print(value + " ");
        }
        for (int value : values) {
            if (value % 2 != 0) System.out.print(value + " ");
        }
        System.out.println();
    }
}
