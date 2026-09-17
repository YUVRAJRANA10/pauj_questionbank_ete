import java.util.*;
class Product {
    int productId; double price; int quantity;
    Product(int id, double p, int q) { productId = id; price = p; quantity = q; }
    double calculateValue() { return price * quantity; }
}
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int id = sc.nextInt();
        double price = sc.nextDouble();
        int qty = sc.nextInt();
        Product p = new Product(id, price, qty);
        System.out.printf("%.2f", p.calculateValue());
    }
}
