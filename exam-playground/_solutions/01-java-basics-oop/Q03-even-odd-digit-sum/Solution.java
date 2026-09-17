import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long number = sc.nextLong();
        int evenSum = 0;
        int oddSum = 0;
        while (number > 0) {
            int digit = (int) (number % 10);
            // TODO: add the digit to the correct sum.
            number /= 10;
        }
        System.out.println(evenSum);
        System.out.println(oddSum);
    }
}
