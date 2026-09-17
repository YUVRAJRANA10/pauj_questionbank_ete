import java.util.*;
import java.time.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        LocalDate start = LocalDate.parse(sc.next());
        int days = sc.nextInt();
        int with = sc.nextInt();
        LocalDate out = start.plusDays(days);
        System.out.println(out);
        System.out.println(days - with);
        System.out.println(out.getYear());
        System.out.println(out.getMonthValue());
    }
}
