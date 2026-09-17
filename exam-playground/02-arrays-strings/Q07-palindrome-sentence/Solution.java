import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String sentence = sc.nextLine();
        String normalized = sentence.replace(" ", "").toLowerCase();
        boolean palindrome = true;
        for (int left = 0, right = normalized.length() - 1;
             left < right; left++, right--) {
            // TODO: compare the characters at left and right.
        }
        System.out.println(palindrome ? "Palindrome" : "Not Palindrome");
    }
}
