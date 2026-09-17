import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i = 0; i < n; i++) pq.add(sc.nextInt());
        int k = sc.nextInt();
        int sum = 0;
        for (int i = 0; i < k; i++) sum += pq.poll();
        System.out.println(sum);
    }
}
