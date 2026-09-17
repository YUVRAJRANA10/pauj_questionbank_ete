import java.util.*;
import java.util.stream.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] marks = new int[n];
        for (int i = 0; i < n; i++) marks[i] = sc.nextInt();
        double avg = IntStream.of(marks).average().orElse(0.0);
        List<Integer> ans = IntStream.range(0, marks.length).filter(i -> marks[i] > avg).mapToObj(i -> marks[i]).collect(Collectors.toList());
        if (ans.isEmpty()) System.out.println(-1);
        else { for (int i = 0; i < ans.size(); i++) { if (i > 0) System.out.print(" " ); System.out.print(ans.get(i)); } System.out.println(); }
    }
}
