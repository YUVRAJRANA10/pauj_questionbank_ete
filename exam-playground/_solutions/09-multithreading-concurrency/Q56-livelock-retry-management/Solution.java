import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int attempts = sc.nextInt();
        System.out.println("Communication Started");
        for (int i = 0; i < attempts - 1; i++) System.out.println("Retrying");
        System.out.println("Message Sent Successfully");
        System.out.println("Communication Completed");
    }
}
