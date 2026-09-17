import java.util.*;
class Resource { }
public class Solution {
    static void doWork(Resource a, Resource b, String threadName) {
        synchronized (a) { synchronized (b) { System.out.println(threadName + " Completed"); } }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(); int b = sc.nextInt();
        Resource r1 = new Resource(); Resource r2 = new Resource();
        doWork(r1, r2, "Thread 1");
        doWork(r1, r2, "Thread 2");
        System.out.println("Production Completed");
    }
}
