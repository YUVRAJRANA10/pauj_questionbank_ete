import java.util.*;
class OrderThread extends Thread {
    int id; OrderThread(int id) { this.id = id; }
    public void run() { System.out.println("Order " + id + " Processing"); }
}
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int id = sc.nextInt();
        new OrderThread(id).start();
    }
}
