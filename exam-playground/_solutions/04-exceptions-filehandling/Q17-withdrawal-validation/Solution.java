import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int balance = sc.nextInt();
        int amount = sc.nextInt();
        try {
            if (amount <= 0) throw new IllegalArgumentException();
            if (amount > balance) throw new ArithmeticException();
            System.out.println(balance - amount);
        } catch (IllegalArgumentException e) {
            System.out.println("Invalid Amount");
        } catch (ArithmeticException e) {
            System.out.println("Insufficient Balance");
        }
    }
}
