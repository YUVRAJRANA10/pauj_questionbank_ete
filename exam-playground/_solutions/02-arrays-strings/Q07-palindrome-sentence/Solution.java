import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        String cleaned = s.replaceAll("\\s+", "").toLowerCase();
        String reverse = new StringBuilder(cleaned).reverse().toString();
        System.out.println(cleaned.equals(reverse) ? "Palindrome" : "Not Palindrome");
    }
}
