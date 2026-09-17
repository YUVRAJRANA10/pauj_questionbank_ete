import java.util.*;
import java.util.stream.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        Map<String, Long> map = Arrays.stream(arr).boxed().collect(Collectors.groupingBy(x -> x >= 75 ? "High" : x >= 50 ? "Medium" : "Low", Collectors.counting()));
        System.out.println("High: " + map.getOrDefault("High", 0L));
        System.out.println("Medium: " + map.getOrDefault("Medium", 0L));
        System.out.println("Low: " + map.getOrDefault("Low", 0L));
    }
}
