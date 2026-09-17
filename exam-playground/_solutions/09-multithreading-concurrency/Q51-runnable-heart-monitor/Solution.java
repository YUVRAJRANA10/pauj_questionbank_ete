import java.util.*;
class MonitoringTask implements Runnable {
    int[] arr; MonitoringTask(int[] arr) { this.arr = arr; }
    public void run() { for (int v : arr) System.out.println("Monitoring: " + v); }
}
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        new Thread(new MonitoringTask(arr)).start();
    }
}
