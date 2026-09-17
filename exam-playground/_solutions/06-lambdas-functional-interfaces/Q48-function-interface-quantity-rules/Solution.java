import java.util.*;
import java.util.function.*;
public class Solution {
    static int countGreater(List<Integer> vals) {
        Predicate<Integer> p = v -> v > 50;
        int c = 0; for (int v : vals) if (p.test(v)) c++; return c;
    }
    static List<Integer> addSafety(List<Integer> vals) {
        Function<Integer, Integer> f = v -> v + 10;
        ArrayList<Integer> out = new ArrayList<>(); for (int v : vals) out.add(f.apply(v)); return out;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<Integer> vals = new ArrayList<>(); for (int i = 0; i < n; i++) vals.add(sc.nextInt());
        System.out.println(countGreater(vals));
        List<Integer> out = addSafety(vals);
        for (int i = 0; i < out.size(); i++) { if (i > 0) System.out.print(" " ); System.out.print(out.get(i)); }
        System.out.println();
    }
}
