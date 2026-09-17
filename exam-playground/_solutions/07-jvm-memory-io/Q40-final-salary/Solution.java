import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int basic = sc.nextInt();
        int allowance = sc.nextInt();
        int deduction = sc.nextInt();
        System.out.println(basic + allowance - deduction);
    }
}
