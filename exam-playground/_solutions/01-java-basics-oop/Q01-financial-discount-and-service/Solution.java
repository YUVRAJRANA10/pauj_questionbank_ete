import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int original = sc.nextInt();
        double discountPercent = sc.nextDouble();
        double servicePercent = sc.nextDouble();
        double discount = original * discountPercent / 100.0;
        double amountAfterDiscount = original - discount;
        double serviceCharge = amountAfterDiscount * servicePercent / 100.0;
        double finalAmount = amountAfterDiscount + serviceCharge;
        System.out.printf("%.2f", finalAmount);
    }
}
