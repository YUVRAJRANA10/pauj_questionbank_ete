import java.util.*;
class TicketBooking { private int tickets; TicketBooking(int t) { tickets = t; } synchronized void book(int req) { if (req <= tickets) tickets -= req; } int rem() { return tickets; } }
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        TicketBooking tb = new TicketBooking(sc.nextInt());
        int req = sc.nextInt();
        tb.book(req);
        System.out.println("Tickets Remaining: " + tb.rem());
    }
}
