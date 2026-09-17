import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Set<Integer> seen = new HashSet<>();
        for (int i = 0; i < n; i++) { int id = sc.nextInt(); int fid = sc.nextInt(); String name = sc.next(); int room = sc.nextInt(); if (seen.add(fid)) System.out.println(fid + " " + name + " " + room); }
    }
}
