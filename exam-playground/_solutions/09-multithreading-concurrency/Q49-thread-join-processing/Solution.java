import java.util.*;
public class Solution {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Thread t = new Thread(() -> System.out.println("Tickets Processed: " + n));
        t.start();
        t.join();
        System.out.println("Processing Completed");
    }
}
