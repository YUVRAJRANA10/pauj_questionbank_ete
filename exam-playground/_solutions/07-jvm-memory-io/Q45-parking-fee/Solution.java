import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int hours = sc.nextInt();
        int fee = 0;
        if (hours <= 0) fee = 0;
        else if (hours <= 2) fee = hours * 20;
        else fee = hours * 40;
        System.out.println(fee);
    }
}
