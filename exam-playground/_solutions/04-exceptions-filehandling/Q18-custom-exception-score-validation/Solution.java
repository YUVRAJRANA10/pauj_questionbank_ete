import java.util.*;
class InvalidScoreException extends Exception { InvalidScoreException() { super("Invalid Score"); } }
public class Solution {
    static void validateScore(int score) throws InvalidScoreException { if (score < 0 || score > 100) throw new InvalidScoreException(); }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int score = sc.nextInt();
        try { validateScore(score); System.out.println(score); } catch (InvalidScoreException e) { System.out.println("Invalid Score"); }
    }
}
