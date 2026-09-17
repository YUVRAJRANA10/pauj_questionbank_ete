import java.util.*;

public class Solution {
    static class Product {
        int id;
        double price;
        int quantity;

        double calculateValue() {
            // TODO: return price multiplied by quantity.
            return 0.0;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Product product = new Product();
        product.id = sc.nextInt();
        product.price = sc.nextDouble();
        product.quantity = sc.nextInt();
        System.out.printf("%.2f%n", product.calculateValue());
    }
}
