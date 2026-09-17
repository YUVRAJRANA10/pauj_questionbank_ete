import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] salaries = new int[n];
        for (int i = 0; i < n; i++) salaries[i] = sc.nextInt();
        int threshold = sc.nextInt();
        System.out.println(Arrays.stream(salaries).filter(salary -> salary > threshold).sum());
    }
}
