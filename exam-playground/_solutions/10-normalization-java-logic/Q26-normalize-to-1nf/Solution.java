import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            String line = sc.nextLine().trim();
            while (line.isEmpty()) line = sc.nextLine().trim();
            String[] parts = line.split(" ", 2);
            String[] values = parts[1].split(",");
            for (String v : values) System.out.println(parts[0] + " " + v);
        }
    }
}
