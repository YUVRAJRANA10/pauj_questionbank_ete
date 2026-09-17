import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double originalAmount = sc.nextDouble();
        double discountPercent = sc.nextDouble();
        double servicePercent = sc.nextDouble();
        double finalAmount = calculateFinalAmount(
                originalAmount, discountPercent, servicePercent);
        System.out.printf("%.2f%n", finalAmount);
    }

    static double calculateFinalAmount(double amount, double discountPercent,
                                       double servicePercent) {
        // TODO: apply the discount first, then calculate service charge.
        return 0.0;
    }
}
