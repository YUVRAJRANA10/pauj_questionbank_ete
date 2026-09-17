import java.util.*;
interface Operation { int apply(int x, int y); }
public class Solution {
    static int applyOperation(int amount, int value, String type) {
        Operation op = type.equals("ADD") ? (x, y) -> x + y : (x, y) -> x * y;
        return op.apply(amount, value);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int amount = sc.nextInt();
        int value = sc.nextInt();
        String type = sc.next();
        System.out.println(applyOperation(amount, value, type));
    }
}
