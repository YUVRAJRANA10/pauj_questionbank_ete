import java.util.*;
class Box<T> { private T value; Box(T value) { this.value = value; } T getValue() { return value; } }
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        double b = sc.nextDouble();
        Box<Integer> x = new Box<>(a);
        Box<Double> y = new Box<>(b);
        System.out.println(x.getValue());
        System.out.printf("%.2f\n", y.getValue());
    }
}
