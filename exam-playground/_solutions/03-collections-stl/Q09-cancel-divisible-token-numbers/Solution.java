import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Integer> tokens = new ArrayList<>();
        for (int i = 0; i < n; i++) tokens.add(sc.nextInt());
        int cancel = sc.nextInt();
        for (int i = tokens.size() - 1; i >= 0; i--) { if (tokens.get(i) % cancel == 0) tokens.remove(i); }
        if (tokens.isEmpty()) System.out.println(-1);
        else { for (int i = 0; i < tokens.size(); i++) { if (i > 0) System.out.print(" " ); System.out.print(tokens.get(i)); } System.out.println(); }
    }
}
