import java.io.*;
public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] tokens = br.readLine().trim().split("\\s+");
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < tokens.length; i++) { if (i > 0) sb.append(' '); sb.append(Integer.parseInt(tokens[i]) + 2); }
        System.out.println(sb);
    }
}
