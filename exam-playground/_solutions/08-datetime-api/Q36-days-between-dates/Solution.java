import java.util.*;
import java.time.*;
import java.time.temporal.ChronoUnit;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        LocalDate start = LocalDate.parse(sc.next());
        LocalDate end = LocalDate.parse(sc.next());
        System.out.println(ChronoUnit.DAYS.between(start, end));
    }
}
