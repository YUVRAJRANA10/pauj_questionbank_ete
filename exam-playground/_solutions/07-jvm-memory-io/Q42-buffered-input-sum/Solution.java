import java.io.*;
public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] tokens = br.readLine().trim().split("\\s+");
        int sum = 0;
        for (String token : tokens) sum += Integer.parseInt(token);
        System.out.println(sum);
    }
}
