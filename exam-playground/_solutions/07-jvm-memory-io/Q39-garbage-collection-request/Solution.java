import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<String> temp = new ArrayList<>();
        for (int i = 0; i < n; i++) temp.add("obj" + i);
        temp.clear();
        System.gc();
        System.out.println("Garbage Collection Requested");
    }
}
