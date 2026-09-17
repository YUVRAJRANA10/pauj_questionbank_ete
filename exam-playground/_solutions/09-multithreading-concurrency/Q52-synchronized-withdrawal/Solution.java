import java.util.*;
class BankAccount { private int balance; BankAccount(int b) { balance = b; } synchronized void withdraw(int amount) { if (amount > balance) { System.out.println("Insufficient Balance"); return; } balance -= amount; } int getBalance() { return balance; } }
public class Solution {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        BankAccount account = new BankAccount(sc.nextInt());
        int a = sc.nextInt(); int b = sc.nextInt();
        Thread t1 = new Thread(() -> account.withdraw(a));
        Thread t2 = new Thread(() -> account.withdraw(b));
        t1.start(); t2.start(); t1.join(); t2.join();
        System.out.println("Final Balance: " + account.getBalance());
    }
}
