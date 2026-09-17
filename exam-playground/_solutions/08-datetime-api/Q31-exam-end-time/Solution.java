import java.util.*;
import java.time.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        LocalDate d = LocalDate.parse(sc.next());
        LocalTime t = LocalTime.parse(sc.next());
        int extra = sc.nextInt();
        LocalDateTime end = LocalDateTime.of(d, t).plusMinutes(extra);
        System.out.println(end.toLocalDate());
        System.out.println(end.toLocalTime());
        System.out.println(end.getYear());
        System.out.println(end.getMonthValue());
        System.out.println(end.getHour());
    }
}
