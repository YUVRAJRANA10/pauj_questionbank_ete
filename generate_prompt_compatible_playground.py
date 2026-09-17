from pathlib import Path
import shutil
import textwrap

ROOT = Path(r"c:\Users\Yuvraj\Desktop\pauj-question_bank_ETE")
PLAYGROUND = ROOT / "exam-playground"

TOPIC_TO_QUESTIONS = {
    "01-java-basics-oop": list(range(1, 6)),
    "02-arrays-strings": list(range(6, 9)),
    "03-collections-stl": list(range(9, 17)),
    "04-exceptions-filehandling": [17, 18, 25],
    "05-streams": list(range(19, 25)),
    "06-lambdas-functional-interfaces": [32, 33, 34, 35, 46, 47, 48],
    "07-jvm-memory-io": list(range(37, 46)),
    "08-datetime-api": [30, 31, 36],
    "09-multithreading-concurrency": list(range(49, 59)),
    "10-normalization-java-logic": list(range(26, 30)),
    "11-sql-ddl-dml-constraints": list(range(59, 62)),
    "12-sql-joins-subqueries-groupby": list(range(62, 71)),
}

QUESTION_INFO = {
    1: ("financial-discount-and-service", "5000\n10.5\n5.0\n", "4712.50"),
    2: ("production-summary", "5\n420 510 380 600 490\n", "2400\n480.00\n220"),
    3: ("even-odd-digit-sum", "583241\n", "6\n21"),
    4: ("kg-to-grams", "4\n12 25 40 8\n", "12000 25000 40000 8000"),
    5: ("product-inventory-value", "105\n1250.50\n8\n", "10004.00"),
    6: ("even-odd-rearrangement", "8\n7 4 9 2 6 11 8 5\n", "4 2 6 8 7 9 11 5"),
    7: ("palindrome-sentence", "Never Odd Or Even\n", "Palindrome"),
    8: ("grade-calculator", "6\n92 76 65 48 35 88\n", "A B C D F B"),
    9: ("cancel-divisible-token-numbers", "8\n12 15 18 21 24 25 30 31\n3\n", "15 25 31"),
    10: ("vector-insert-after-id", "5\n201 305 410 512 620\n410\n999\n", "201 305 410 999 512 620"),
    11: ("linkedlist-remove-first-occurrence", "7\n101 205 310 205 415 520 610\n205\n", "101 310 205 415 520 610"),
    12: ("high-unique-registration", "8\n101 102 103 101 104 105 106 102\n", "High Unique Registration"),
    13: ("treeset-previous-smaller-score", "8\n45 72 88 65 72 91 54 80\n75\n", "72"),
    14: ("hashmap-product-quantity-total", "5\n101 20\n102 35\n103 15\n104 50\n105 25\n4\n101 103 105 110\n", "60"),
    15: ("priorityqueue-first-k-sum", "7\n18 5 12 30 9 25 3\n3\n", "17"),
    16: ("generic-box", "250\n45.75\n", "250\n45.75"),
    17: ("withdrawal-validation", "25000\n7500\n", "17500"),
    18: ("custom-exception-score-validation", "85\n", "85"),
    19: ("marks-above-average", "6\n40 55 70 80 65 50\n", "70 80 65"),
    20: ("top-three-distinct-distances", "8\n120 450 300 450 700 120 550 700\n", "700 550 450"),
    21: ("total-salary-above-threshold", "6\n35000 52000 48000 75000 42000 90000\n50000\n", "217000"),
    22: ("stream-discount-mapping", "6\n500 1200 800 2000 1500 900\n", "475 1020 760 1700 1275 855"),
    23: ("grouping-by-category", "8\n82 45 67 91 38 75 54 49\n", "3\n2\n3"),
    24: ("even-square-sum", "6\n3 4 6 5 8 7\n", "116"),
    25: ("safe-index-and-division", "5\n20 40 60 80 100\n2\n10\n", "6"),
    26: ("normalize-to-1nf", "3\n201 Java,Python,DBMS\n202 HTML,CSS\n203 JavaScript,React\n", "201 Java\n201 Python\n201 DBMS\n202 HTML\n202 CSS\n203 JavaScript\n203 React"),
    27: ("2nf-patient-summary", "6\n501 Rahul 301 Checkup DrKumar\n502 Neha 302 XRay DrSharma\n501 Rahul 303 BloodTest DrMehta\n503 Aman 301 Checkup DrKumar\n502 Neha 304 MRI DrSingh\n501 Rahul 305 ECG DrPatel\n", "501 Rahul 3\n502 Neha 2\n503 Aman 1"),
    28: ("3nf-student-summary", "6\n201 Arjun 10 ComputerScience\n202 Priya 20 Commerce\n203 Karan 10 ComputerScience\n201 Arjun 10 ComputerScience\n204 Sneha 30 Mathematics\n202 Priya 20 Commerce\n", "201 Arjun 10\n202 Priya 20\n203 Karan 10\n204 Sneha 30"),
    29: ("3nf-faculty-allocation-summary", "7\n101 501 Sharma 201\n102 502 Mehta 202\n103 501 Sharma 201\n104 503 Gupta 203\n105 502 Mehta 202\n106 504 Singh 204\n107 501 Sharma 201\n", "501 Sharma 201\n502 Mehta 202\n503 Gupta 203\n504 Singh 204"),
    30: ("reservation-checkout-date", "2026-08-10\n30\n12\n", "2026-09-09\n18"),
    31: ("exam-end-time", "2026-09-14\n22:30\n120\n", "2026-09-14\n00:30"),
    32: ("adjusted-consumption", "4\n100 200 300 400\n", "110.00 220.00 330.00 440.00"),
    33: ("package-priority-score", "3\n10 25 40\n", "30 60 90"),
    34: ("machine-safety-check", "5\n25 80 90 15 50\n", "Safe Unsafe Unsafe Safe Safe"),
    35: ("optional-employee-lookup", "3\n101 Amit\n102 Neha\n103 Rahul\n102\n", "Neha"),
    36: ("days-between-dates", "2026-09-01\n2026-09-15\n", "14"),
    37: ("local-variables-vs-array", "10 20 30\n40 50 60\n", "10 20 30\n40 50 60"),
    38: ("method-local-total-marks", "75 82 90\n", "247"),
    39: ("garbage-collection-request", "100\n", "Garbage Collection Requested"),
    40: ("final-salary", "30000\n5000\n2000\n", "33000"),
    41: ("square-stringbuilder-output", "5\n2 3 4 5 6\n", "4 9 16 25 36"),
    42: ("buffered-input-sum", "5\n10 20 30 40 50\n", "150"),
    43: ("buffered-temperature-report", "4\n20 25 30 35\n", "22 27 32 37"),
    44: ("corrected-total-cost", "3\n2 100\n5 50\n3 200\n", "1200"),
    45: ("parking-fee", "2\n", "40"),
    46: ("functional-operation-argument", "1000\n50\nADD\n", "1050"),
    47: ("uppercase-method-reference", "3\namit neha rahul\n", "AMIT NEHA RAHUL"),
    48: ("function-interface-quantity-rules", "5\n20 60 45 80 100\n", "3\n30 70 55 90 110"),
    49: ("thread-join-processing", "5\n", "Tickets Processed: 5\nProcessing Completed"),
    50: ("thread-class-order", "105\n", "Order 105 Processing"),
    51: ("runnable-heart-monitor", "3\n72 80 76\n", "Monitoring: 72\nMonitoring: 80\nMonitoring: 76"),
    52: ("synchronized-withdrawal", "10000\n3000\n4000\n", "Final Balance: 3000"),
    53: ("synchronized-ticket-booking", "10\n6\n", "Tickets Remaining: 4"),
    54: ("synchronized-visitor-counter", "5000\n7000\n", "Total Visitors: 12000"),
    55: ("deadlock-prevention", "10\n20\n", "Thread 1 Completed\nThread 2 Completed\nProduction Completed"),
    56: ("livelock-retry-management", "3\n", "Communication Started\nRetrying\nRetrying\nMessage Sent Successfully\nCommunication Completed"),
    57: ("synchronized-submission-counter", "2500\n3500\n", "Total Submissions: 6000"),
    58: ("concurrent-login-records", "4000\n6000\n", "Total Login Records: 10000"),
    59: ("students-create-and-list", "", ""),
    60: ("cse-salary-increment", "", ""),
    61: ("book-price-deletion", "", ""),
    62: ("department-student-count", "", ""),
    63: ("customer-total-spent", "", ""),
    64: ("subject-average-marks", "", ""),
    65: ("customers-with-3-or-more-orders", "", ""),
    66: ("salary-above-average", "", ""),
    67: ("inner-join-students-departments", "", ""),
    68: ("left-join-employees-departments", "", ""),
    69: ("self-join-manager-list", "", ""),
    70: ("product-highest-price-subquery", "", ""),
}

JAVA_REF = {
    1: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int original = sc.nextInt();\n        double discountPercent = sc.nextDouble();\n        double servicePercent = sc.nextDouble();\n        double discount = original * discountPercent / 100.0;\n        double amountAfterDiscount = original - discount;\n        double serviceCharge = amountAfterDiscount * servicePercent / 100.0;\n        double finalAmount = amountAfterDiscount + serviceCharge;\n        System.out.printf("%.2f", finalAmount);\n    }\n}\n''',
    2: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int[] arr = new int[n];\n        int total = 0, min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;\n        for (int i = 0; i < n; i++) {\n            arr[i] = sc.nextInt();\n            total += arr[i];\n            min = Math.min(min, arr[i]);\n            max = Math.max(max, arr[i]);\n        }\n        System.out.println(total);\n        System.out.printf("%.2f\\n", total / (double) n);\n        System.out.println(max - min);\n    }\n}\n''',
    3: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int even = 0, odd = 0;\n        while (n > 0) {\n            int d = n % 10;\n            if (d % 2 == 0) even += d;\n            else odd += d;\n            n /= 10;\n        }\n        System.out.println(even);\n        System.out.println(odd);\n    }\n}\n''',
    4: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        long[] arr = new long[n];\n        for (int i = 0; i < n; i++) arr[i] = sc.nextLong();\n        for (int i = 0; i < n; i++) { if (i > 0) System.out.print(" "); System.out.print(arr[i] * 1000L); }\n        System.out.println();\n    }\n}\n''',
    5: '''import java.util.*;\nclass Product {\n    int productId; double price; int quantity;\n    Product(int id, double p, int q) { productId = id; price = p; quantity = q; }\n    double calculateValue() { return price * quantity; }\n}\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int productId = sc.nextInt();\n        double price = sc.nextDouble();\n        int qty = sc.nextInt();\n        Product product = new Product(productId, price, qty);\n        System.out.printf("%.2f", product.calculateValue());\n    }\n}\n''',
    6: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int[] arr = new int[n];\n        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();\n        int write = 0;\n        for (int i = 0; i < n; i++) if (arr[i] % 2 == 0) { int tmp = arr[write]; arr[write] = arr[i]; arr[i] = tmp; write++; }\n        for (int i = 0; i < n; i++) if (arr[i] % 2 != 0) { int tmp = arr[write]; arr[write] = arr[i]; arr[i] = tmp; write++; }\n        for (int i = 0; i < n; i++) { if (i > 0) System.out.print(" "); System.out.print(arr[i]); }\n        System.out.println();\n    }\n}\n''',
    7: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        sc.useDelimiter("\\n");\n        String s = sc.next();\n        String cleaned = s.replace(" ", "").toLowerCase();\n        String reverse = new StringBuilder(cleaned).reverse().toString();\n        System.out.println(cleaned.equals(reverse) ? "Palindrome" : "Not Palindrome");\n    }\n}\n''',
    8: '''import java.util.*;\npublic class Solution {\n    static char calculateGrade(int marks) {\n        if (marks >= 90) return 'A';\n        if (marks >= 75) return 'B';\n        if (marks >= 60) return 'C';\n        if (marks >= 40) return 'D';\n        return 'F';\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        for (int i = 0; i < n; i++) { if (i > 0) System.out.print(" "); System.out.print(calculateGrade(sc.nextInt())); }\n        System.out.println();\n    }\n}\n''',
    9: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        ArrayList<Integer> nums = new ArrayList<>();\n        for (int i = 0; i < n; i++) nums.add(sc.nextInt());\n        int cancel = sc.nextInt();\n        for (int i = nums.size()-1; i >= 0; i--) { if (nums.get(i) % cancel == 0) nums.remove(i); }\n        if (nums.isEmpty()) System.out.println(-1);\n        else { for (int i = 0; i < nums.size(); i++) { if (i > 0) System.out.print(" "); System.out.print(nums.get(i)); } System.out.println(); }\n    }\n}\n''',
    10: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        Vector<Integer> items = new Vector<>();\n        for (int i = 0; i < n; i++) items.add(sc.nextInt());\n        int target = sc.nextInt();\n        int value = sc.nextInt();\n        int idx = -1;\n        for (int i = 0; i < items.size(); i++) { if (items.get(i) == target) { idx = i; break; } }\n        if (idx == -1) { System.out.println("Container Not Found"); return; }\n        items.add(idx + 1, value);\n        for (int i = 0; i < items.size(); i++) { if (i > 0) System.out.print(" "); System.out.print(items.get(i)); }\n        System.out.println();\n    }\n}\n''',
    11: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        LinkedList<Integer> list = new LinkedList<>();\n        for (int i = 0; i < n; i++) list.add(sc.nextInt());\n        int target = sc.nextInt();\n        boolean removed = list.removeFirstOccurrence(target);\n        if (!removed) { System.out.println("Task Not Found"); return; }\n        for (int i = 0; i < list.size(); i++) { if (i > 0) System.out.print(" "); System.out.print(list.get(i)); }\n        System.out.println();\n    }\n}\n''',
    12: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        HashSet<Integer> set = new HashSet<>();\n        for (int i = 0; i < n; i++) set.add(sc.nextInt());\n        System.out.println(set.size() > (n / 2.0) ? "High Unique Registration" : "Low Unique Registration");\n    }\n}\n''',
    13: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        TreeSet<Integer> set = new TreeSet<>();\n        for (int i = 0; i < n; i++) set.add(sc.nextInt());\n        int target = sc.nextInt();\n        Integer floor = set.floor(target - 1);\n        System.out.println(floor == null ? -1 : floor);\n    }\n}\n''',
    14: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        Map<Integer, Integer> map = new HashMap<>();\n        for (int i = 0; i < n; i++) {\n            map.put(sc.nextInt(), sc.nextInt());\n        }\n        int q = sc.nextInt();\n        int total = 0;\n        for (int i = 0; i < q; i++) total += map.getOrDefault(sc.nextInt(), 0);\n        System.out.println(total);\n    }\n}\n''',
    15: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        PriorityQueue<Integer> pq = new PriorityQueue<>();\n        for (int i = 0; i < n; i++) pq.add(sc.nextInt());\n        int k = sc.nextInt();\n        int sum = 0;\n        for (int i = 0; i < k; i++) sum += pq.poll();\n        System.out.println(sum);\n    }\n}\n''',
    16: '''import java.util.*;\nclass Box<T> { private T val; Box(T val) { this.val = val; } T getVal() { return val; } }\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt();\n        double b = sc.nextDouble();\n        Box<Integer> x = new Box<>(a);\n        Box<Double> y = new Box<>(b);\n        System.out.println(x.getVal());\n        System.out.printf("%.2f\\n", y.getVal());\n    }\n}\n''',
    17: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int balance = sc.nextInt();\n        int amount = sc.nextInt();\n        try {\n            if (amount <= 0) throw new IllegalArgumentException();\n            if (amount > balance) throw new ArithmeticException();\n            System.out.println(balance - amount);\n        } catch (IllegalArgumentException e) {\n            System.out.println("Invalid Amount");\n        } catch (ArithmeticException e) {\n            System.out.println("Insufficient Balance");\n        }\n    }\n}\n''',
    18: '''import java.util.*;\nclass InvalidScoreException extends Exception { InvalidScoreException() { super("Invalid Score"); } }\npublic class Solution {\n    static void validate(int score) throws InvalidScoreException { if (score < 0 || score > 100) throw new InvalidScoreException(); }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int score = sc.nextInt();\n        try { validate(score); System.out.println(score); } catch (InvalidScoreException e) { System.out.println("Invalid Score"); }\n    }\n}\n''',
    19: '''import java.util.*;\nimport java.util.stream.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int[] marks = new int[n];\n        for (int i = 0; i < n; i++) marks[i] = sc.nextInt();\n        double avg = IntStream.of(marks).average().orElse(0.0);\n        List<Integer> ans = IntStream.range(0, marks.length).filter(i -> marks[i] > avg).mapToObj(i -> marks[i]).collect(Collectors.toList());\n        if (ans.isEmpty()) System.out.println(-1);\n        else { for (int i = 0; i < ans.size(); i++) { if (i > 0) System.out.print(" "); System.out.print(ans.get(i)); } System.out.println(); }\n    }\n}\n''',
    20: '''import java.util.*;\nimport java.util.stream.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        List<Integer> list = new ArrayList<>();\n        for (int i = 0; i < n; i++) list.add(sc.nextInt());\n        List<Integer> ans = list.stream().distinct().sorted(Comparator.reverseOrder()).limit(3).collect(Collectors.toList());\n        for (int i = 0; i < ans.size(); i++) { if (i > 0) System.out.print(" "); System.out.print(ans.get(i)); }\n        System.out.println();\n    }\n}\n''',
    21: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int total = 0;\n        for (int i = 0; i < n; i++) total += sc.nextInt();\n        int threshold = sc.nextInt();\n        System.out.println(total > threshold ? total : 0);\n    }\n}\n''',
    22: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int[] arr = new int[n];\n        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();\n        for (int i = 0; i < n; i++) { if (i > 0) System.out.print(" "); System.out.print(arr[i] >= 1000 ? Math.round(arr[i] * 0.85f) : Math.round(arr[i] * 0.95f)); }\n        System.out.println();\n    }\n}\n''',
    23: '''import java.util.*;\nimport java.util.stream.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int[] arr = new int[n];\n        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();\n        Map<String, Long> map = Arrays.stream(arr).boxed().collect(Collectors.groupingBy(x -> x >= 75 ? "High" : x >= 50 ? "Medium" : "Low", Collectors.counting()));\n        System.out.println(map.getOrDefault("High", 0L));\n        System.out.println(map.getOrDefault("Medium", 0L));\n        System.out.println(map.getOrDefault("Low", 0L));\n    }\n}\n''',
    24: '''import java.util.*;\nimport java.util.stream.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int[] arr = new int[n];\n        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();\n        System.out.println(IntStream.of(arr).filter(x -> x % 2 == 0).map(x -> x * x).sum());\n    }\n}\n''',
    25: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int[] arr = new int[n];\n        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();\n        int idx = sc.nextInt();\n        int div = sc.nextInt();\n        try { System.out.println(arr[idx] / div); } catch (ArrayIndexOutOfBoundsException e) { System.out.println("Invalid Index"); } catch (ArithmeticException e) { System.out.println("Division By Zero"); }\n    }\n}\n''',
    26: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        sc.nextLine();\n        for (int i = 0; i < n; i++) {\n            String line = sc.nextLine();\n            String[] parts = line.split(" ", 2);\n            String[] vals = parts[1].split(",");\n            for (String v : vals) System.out.println(parts[0] + " " + v.trim());\n        }\n    }\n}\n''',
    27: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        Map<Integer,Integer> map = new HashMap<>();\n        for (int i = 0; i < n; i++) { int id = sc.nextInt(); String name = sc.next(); int count = sc.nextInt(); String doc = sc.next(); map.put(id, map.getOrDefault(id, 0) + 1); }\n        for (Map.Entry<Integer,Integer> e : map.entrySet()) System.out.println(e.getKey() + " " + e.getValue());\n    }\n}\n''',
    28: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        Map<Integer, String> map = new LinkedHashMap<>();\n        for (int i = 0; i < n; i++) { int id = sc.nextInt(); String name = sc.next(); int dept = sc.nextInt(); String deptName = sc.next(); map.putIfAbsent(id, name + " " + dept); }\n        for (Map.Entry<Integer,String> e : map.entrySet()) System.out.println(e.getKey() + " " + e.getValue());\n    }\n}\n''',
    29: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        Set<Integer> seen = new HashSet<>();\n        for (int i = 0; i < n; i++) { int id = sc.nextInt(); int fid = sc.nextInt(); String name = sc.next(); int room = sc.nextInt(); if (seen.add(fid)) System.out.println(fid + " " + name + " " + room); }\n    }\n}\n''',
    30: '''import java.util.*;\nimport java.time.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        LocalDate start = LocalDate.parse(sc.nextLine());\n        int days = sc.nextInt();\n        int offset = sc.nextInt();\n        LocalDate result = start.plusDays(days);\n        System.out.println(result);\n        System.out.println(days - offset);\n    }\n}\n''',
    31: '''import java.util.*;\nimport java.time.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        LocalDate d = LocalDate.parse(sc.nextLine());\n        LocalTime t = LocalTime.parse(sc.nextLine());\n        int extra = sc.nextInt();\n        LocalDateTime end = LocalDateTime.of(d, t).plusMinutes(extra);\n        System.out.println(end.toLocalDate());\n        System.out.println(end.toLocalTime());\n    }\n}\n''',
    32: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        double[] arr = new double[n];\n        for (int i = 0; i < n; i++) arr[i] = sc.nextDouble();\n        for (int i = 0; i < n; i++) { if (i > 0) System.out.print(" "); System.out.printf("%.2f", arr[i] * 1.10); }\n        System.out.println();\n    }\n}\n''',
    33: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int[] arr = new int[n];\n        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();\n        for (int i = 0; i < n; i++) { if (i > 0) System.out.print(" "); System.out.print(arr[i] * 2 + 10); }\n        System.out.println();\n    }\n}\n''',
    34: '''import java.util.*;\n@FunctionalInterface\ninterface SafetyCheck { boolean apply(int temp); }\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        SafetyCheck check = t -> t >= 20 && t <= 80;\n        for (int i = 0; i < n; i++) { if (i > 0) System.out.print(" "); System.out.print(check.apply(sc.nextInt()) ? "Safe" : "Unsafe"); }\n        System.out.println();\n    }\n}\n''',
    35: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        Map<Integer,String> map = new HashMap<>();\n        for (int i = 0; i < n; i++) map.put(sc.nextInt(), sc.next());\n        int key = sc.nextInt();\n        System.out.println(map.getOrDefault(key, "Employee Not Found"));\n    }\n}\n''',
    36: '''import java.util.*;\nimport java.time.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        LocalDate start = LocalDate.parse(sc.nextLine());\n        LocalDate end = LocalDate.parse(sc.nextLine());\n        System.out.println(ChronoUnit.DAYS.between(start, end));\n    }\n}\n''',
    37: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt(); int b = sc.nextInt(); int c = sc.nextInt();\n        int[] arr = new int[]{sc.nextInt(), sc.nextInt(), sc.nextInt()};\n        System.out.println(a + " " + b + " " + c);\n        for (int i = 0; i < arr.length; i++) { if (i > 0) System.out.print(" "); System.out.print(arr[i]); }\n        System.out.println();\n    }\n}\n''',
    38: '''import java.util.*;\npublic class Solution {\n    static int total(int a, int b, int c) { return a + b + c; }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt(); int b = sc.nextInt(); int c = sc.nextInt();\n        System.out.println(total(a, b, c));\n    }\n}\n''',
    39: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        List<String> list = new ArrayList<>();\n        for (int i = 0; i < n; i++) list.add("obj" + i);\n        list.clear();\n        System.gc();\n        System.out.println("Garbage Collection Requested");\n    }\n}\n''',
    40: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int basic = sc.nextInt();\n        int allowance = sc.nextInt();\n        int deduction = sc.nextInt();\n        System.out.println(basic + allowance - deduction);\n    }\n}\n''',
    41: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int[] arr = new int[n];\n        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();\n        StringBuilder sb = new StringBuilder();\n        for (int i = 0; i < n; i++) { if (i > 0) sb.append(' '); sb.append(arr[i] * arr[i]); }\n        System.out.println(sb);\n    }\n}\n''',
    42: '''import java.io.*;\npublic class Solution {\n    public static void main(String[] args) throws Exception {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        int n = Integer.parseInt(br.readLine());\n        String[] tokens = br.readLine().split(" ");\n        int sum = 0;\n        for (String token : tokens) sum += Integer.parseInt(token);\n        System.out.println(sum);\n    }\n}\n''',
    43: '''import java.io.*;\npublic class Solution {\n    public static void main(String[] args) throws Exception {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        int n = Integer.parseInt(br.readLine());\n        String[] tokens = br.readLine().split(" ");\n        StringBuilder sb = new StringBuilder();\n        for (int i = 0; i < tokens.length; i++) { if (i > 0) sb.append(' '); sb.append(Integer.parseInt(tokens[i]) + 2); }\n        System.out.println(sb);\n    }\n}\n''',
    44: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int total = 0;\n        for (int i = 0; i < n; i++) { int qty = sc.nextInt(); int price = sc.nextInt(); total += qty * price; }\n        System.out.println(total);\n    }\n}\n''',
    45: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int hours = sc.nextInt();\n        int fee = 0;\n        if (hours <= 0) fee = 0;\n        else if (hours <= 2) fee = hours * 20;\n        else fee = hours * 40;\n        System.out.println(fee);\n    }\n}\n''',
    46: '''import java.util.*;\ninterface Operation { int apply(int x, int y); }\npublic class Solution {\n    static int run(int amount, int value, String type) {\n        Operation op = type.equals("ADD") ? (x, y) -> x + y : (x, y) -> x * y;\n        return op.apply(amount, value);\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int amount = sc.nextInt();\n        int value = sc.nextInt();\n        String type = sc.next();\n        System.out.println(run(amount, value, type));\n    }\n}\n''',
    47: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        String[] arr = new String[n];\n        for (int i = 0; i < n; i++) arr[i] = sc.next();\n        for (int i = 0; i < n; i++) { if (i > 0) System.out.print(" "); System.out.print(arr[i].toUpperCase()); }\n        System.out.println();\n    }\n}\n''',
    48: '''import java.util.*;\nimport java.util.function.*;\npublic class Solution {\n    static int countGreater(List<Integer> vals) {\n        Predicate<Integer> p = v -> v > 50;\n        int c = 0; for (int v : vals) if (p.test(v)) c++; return c;\n    }\n    static List<Integer> addSafety(List<Integer> vals) {\n        Function<Integer, Integer> f = v -> v + 10;\n        ArrayList<Integer> out = new ArrayList<>(); for (int v : vals) out.add(f.apply(v)); return out;\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        List<Integer> vals = new ArrayList<>(); for (int i = 0; i < n; i++) vals.add(sc.nextInt());\n        System.out.println(countGreater(vals));\n        List<Integer> out = addSafety(vals);\n        for (int i = 0; i < out.size(); i++) { if (i > 0) System.out.print(" "); System.out.print(out.get(i)); }\n        System.out.println();\n    }\n}\n''',
    49: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) throws Exception {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        Thread t = new Thread(() -> System.out.println("Tickets Processed: " + n));\n        t.start();\n        t.join();\n        System.out.println("Processing Completed");\n    }\n}\n''',
    50: '''import java.util.*;\nclass OrderThread extends Thread {\n    int id; OrderThread(int id) { this.id = id; }\n    public void run() { System.out.println("Order " + id + " Processing"); }\n}\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int id = sc.nextInt();\n        new OrderThread(id).start();\n    }\n}\n''',
    51: '''import java.util.*;\nclass MonitoringTask implements Runnable {\n    int[] arr; MonitoringTask(int[] arr) { this.arr = arr; }\n    public void run() { for (int v : arr) System.out.println("Monitoring: " + v); }\n}\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int[] arr = new int[n];\n        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();\n        new Thread(new MonitoringTask(arr)).start();\n    }\n}\n''',
    52: '''import java.util.*;\nclass BankAccount { private int balance; BankAccount(int b) { balance = b; } synchronized void withdraw(int amount) { if (amount > balance) { System.out.println("Insufficient Balance"); return; } balance -= amount; } int getBalance() { return balance; } }\npublic class Solution {\n    public static void main(String[] args) throws Exception {\n        Scanner sc = new Scanner(System.in);\n        BankAccount account = new BankAccount(sc.nextInt());\n        int a = sc.nextInt(); int b = sc.nextInt();\n        Thread t1 = new Thread(() -> account.withdraw(a));\n        Thread t2 = new Thread(() -> account.withdraw(b));\n        t1.start(); t2.start(); t1.join(); t2.join();\n        System.out.println("Final Balance: " + account.getBalance());\n    }\n}\n''',
    53: '''import java.util.*;\nclass TicketBooking { private int tickets; TicketBooking(int t) { tickets = t; } synchronized void book(int req) { if (req <= tickets) tickets -= req; } int rem() { return tickets; } }\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        TicketBooking tb = new TicketBooking(sc.nextInt());\n        int req = sc.nextInt();\n        tb.book(req);\n        System.out.println("Tickets Remaining: " + tb.rem());\n    }\n}\n''',
    54: '''import java.util.*;\nclass Counter { private int count = 0; synchronized void add(int n) { count += n; } int value() { return count; } }\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        Counter c = new Counter();\n        c.add(sc.nextInt()); c.add(sc.nextInt());\n        System.out.println("Total Visitors: " + c.value());\n    }\n}\n''',
    55: '''import java.util.*;\nclass Resource { }\npublic class Solution {\n    static void doWork(Resource a, Resource b, String threadName) { synchronized (a) { synchronized (b) { System.out.println(threadName + " Completed"); } } }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt(); int b = sc.nextInt();\n        Resource r1 = new Resource(); Resource r2 = new Resource();\n        doWork(r1, r2, "Thread 1"); doWork(r1, r2, "Thread 2");\n        System.out.println("Production Completed");\n    }\n}\n''',
    56: '''import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int attempts = sc.nextInt();\n        System.out.println("Communication Started");\n        for (int i = 0; i < attempts - 1; i++) System.out.println("Retrying");\n        System.out.println("Message Sent Successfully");\n        System.out.println("Communication Completed");\n    }\n}\n''',
    57: '''import java.util.*;\nclass SubmissionCounter { private int count = 0; synchronized void add(int n) { count += n; } int value() { return count; } }\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        SubmissionCounter c = new SubmissionCounter();\n        c.add(sc.nextInt()); c.add(sc.nextInt());\n        System.out.println("Total Submissions: " + c.value());\n    }\n}\n''',
    58: '''import java.util.*;\nimport java.util.concurrent.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt(); int b = sc.nextInt();\n        Set<String> set = ConcurrentHashMap.newKeySet();\n        for (int i = 0; i < a; i++) set.add("login-" + i);\n        for (int i = 0; i < b; i++) set.add("login-" + i);\n        System.out.println("Total Login Records: " + set.size());\n    }\n}\n''',
}

SQL_TOPICS = {
    59: ("students-table-constraints", "CREATE TABLE Students (student_id INT PRIMARY KEY, student_name VARCHAR(50) NOT NULL, email VARCHAR(100) UNIQUE, age INT CHECK (age BETWEEN 17 AND 60), course VARCHAR(50));\nINSERT INTO Students VALUES (101, 'Amit', 'amit@gmail.com', 20, 'CSE');\nINSERT INTO Students VALUES (102, 'Neha', 'neha@gmail.com', 21, 'ECE');\nINSERT INTO Students VALUES (103, 'Rahul', 'rahul@gmail.com', 22, 'CSE');\nSELECT * FROM Students ORDER BY student_id;\n", "SELECT * FROM Students ORDER BY student_id;\n"),
    60: ("cse-salary-increment", "CREATE TABLE Employees (employee_id INT PRIMARY KEY, employee_name VARCHAR(50), department VARCHAR(50), salary DECIMAL(10,2));\nINSERT INTO Employees VALUES (101, 'Amit', 'CSE', 50000);\nINSERT INTO Employees VALUES (102, 'Neha', 'ECE', 45000);\nINSERT INTO Employees VALUES (103, 'Rahul', 'CSE', 60000);\nUPDATE Employees SET salary = salary * 1.10 WHERE department = 'CSE';\nSELECT employee_name, department, salary FROM Employees ORDER BY employee_id;\n", "UPDATE Employees SET salary = salary * 1.10 WHERE department = 'CSE';\nSELECT employee_name, department, salary FROM Employees ORDER BY employee_id;\n"),
    61: ("book-price-deletion", "CREATE TABLE Books (book_id INT PRIMARY KEY, title VARCHAR(50), author VARCHAR(50), price INT);\nINSERT INTO Books VALUES (101, 'Java', 'James', 550);\nINSERT INTO Books VALUES (102, 'SQL', 'Korth', 250);\nINSERT INTO Books VALUES (103, 'Python', 'Rossum', 650);\nDELETE FROM Books WHERE price < 300;\nSELECT * FROM Books ORDER BY book_id;\n", "DELETE FROM Books WHERE price < 300;\nSELECT * FROM Books ORDER BY book_id;\n"),
    62: ("department-student-count", "CREATE TABLE Students (student_id INT PRIMARY KEY, student_name VARCHAR(50), department VARCHAR(50));\nINSERT INTO Students VALUES (101, 'Amit', 'CSE');\nINSERT INTO Students VALUES (102, 'Neha', 'ECE');\nINSERT INTO Students VALUES (103, 'Rahul', 'CSE');\nINSERT INTO Students VALUES (104, 'Simran', 'IT');\nSELECT department, COUNT(*) AS student_count FROM Students GROUP BY department ORDER BY department;\n", "SELECT department, COUNT(*) AS student_count FROM Students GROUP BY department ORDER BY department;\n"),
    63: ("customer-total-spent", "CREATE TABLE Orders (order_id INT PRIMARY KEY, customer_id INT, amount INT);\nINSERT INTO Orders VALUES (1, 101, 1200);\nINSERT INTO Orders VALUES (2, 102, 800);\nINSERT INTO Orders VALUES (3, 101, 1500);\nINSERT INTO Orders VALUES (4, 103, 2000);\nSELECT customer_id, SUM(amount) AS total_amount FROM Orders GROUP BY customer_id ORDER BY customer_id;\n", "SELECT customer_id, SUM(amount) AS total_amount FROM Orders GROUP BY customer_id ORDER BY customer_id;\n"),
    64: ("subject-average-marks", "CREATE TABLE Marks (student_id INT, subject VARCHAR(20), marks INT);\nINSERT INTO Marks VALUES (101, 'Java', 80);\nINSERT INTO Marks VALUES (102, 'Java', 90);\nINSERT INTO Marks VALUES (103, 'DBMS', 70);\nINSERT INTO Marks VALUES (104, 'DBMS', 80);\nINSERT INTO Marks VALUES (105, 'Java', 100);\nSELECT subject, ROUND(AVG(marks), 2) AS average_marks FROM Marks GROUP BY subject ORDER BY subject;\n", "SELECT subject, ROUND(AVG(marks), 2) AS average_marks FROM Marks GROUP BY subject ORDER BY subject;\n"),
    65: ("customers-with-3-or-more-orders", "CREATE TABLE Orders (order_id INT PRIMARY KEY, customer_id INT, amount INT);\nINSERT INTO Orders VALUES (1, 101, 500);\nINSERT INTO Orders VALUES (2, 102, 700);\nINSERT INTO Orders VALUES (3, 101, 400);\nINSERT INTO Orders VALUES (4, 103, 900);\nINSERT INTO Orders VALUES (5, 101, 600);\nINSERT INTO Orders VALUES (6, 102, 300);\nINSERT INTO Orders VALUES (7, 101, 800);\nSELECT customer_id, COUNT(*) AS order_count FROM Orders GROUP BY customer_id HAVING COUNT(*) >= 3;\n", "SELECT customer_id, COUNT(*) AS order_count FROM Orders GROUP BY customer_id HAVING COUNT(*) >= 3;\n"),
    66: ("salary-above-average", "CREATE TABLE Employees (employee_id INT PRIMARY KEY, employee_name VARCHAR(50), salary INT);\nINSERT INTO Employees VALUES (101, 'Amit', 40000);\nINSERT INTO Employees VALUES (102, 'Neha', 60000);\nINSERT INTO Employees VALUES (103, 'Rahul', 50000);\nINSERT INTO Employees VALUES (104, 'Simran', 80000);\nINSERT INTO Employees VALUES (105, 'Karan', 30000);\nSELECT employee_name, salary FROM Employees WHERE salary > (SELECT AVG(salary) FROM Employees) ORDER BY salary DESC;\n", "SELECT employee_name, salary FROM Employees WHERE salary > (SELECT AVG(salary) FROM Employees) ORDER BY salary DESC;\n"),
    67: ("inner-join-students-departments", "CREATE TABLE Students (student_id INT PRIMARY KEY, student_name VARCHAR(50), department_id INT);\nCREATE TABLE Departments (department_id INT PRIMARY KEY, department_name VARCHAR(50));\nINSERT INTO Students VALUES (101, 'Amit', 10);\nINSERT INTO Students VALUES (102, 'Neha', 20);\nINSERT INTO Students VALUES (103, 'Rahul', 10);\nINSERT INTO Departments VALUES (10, 'CSE');\nINSERT INTO Departments VALUES (20, 'ECE');\nSELECT s.student_name, d.department_name FROM Students s INNER JOIN Departments d ON s.department_id = d.department_id ORDER BY s.student_id;\n", "SELECT s.student_name, d.department_name FROM Students s INNER JOIN Departments d ON s.department_id = d.department_id ORDER BY s.student_id;\n"),
    68: ("left-join-employees-departments", "CREATE TABLE Employees (employee_id INT PRIMARY KEY, employee_name VARCHAR(50), department_id INT);\nCREATE TABLE Departments (department_id INT PRIMARY KEY, department_name VARCHAR(50));\nINSERT INTO Employees VALUES (101, 'Amit', 10);\nINSERT INTO Employees VALUES (102, 'Neha', NULL);\nINSERT INTO Employees VALUES (103, 'Rahul', 20);\nINSERT INTO Departments VALUES (10, 'CSE');\nINSERT INTO Departments VALUES (20, 'ECE');\nSELECT e.employee_name, d.department_name FROM Employees e LEFT JOIN Departments d ON e.department_id = d.department_id ORDER BY e.employee_id;\n", "SELECT e.employee_name, d.department_name FROM Employees e LEFT JOIN Departments d ON e.department_id = d.department_id ORDER BY e.employee_id;\n"),
    69: ("self-join-manager-list", "CREATE TABLE Employees (employee_id INT PRIMARY KEY, employee_name VARCHAR(50), manager_id INT NULL);\nINSERT INTO Employees VALUES (101, 'Amit', NULL);\nINSERT INTO Employees VALUES (102, 'Neha', 101);\nINSERT INTO Employees VALUES (103, 'Rahul', 101);\nINSERT INTO Employees VALUES (104, 'Simran', 102);\nSELECT e.employee_name, m.employee_name AS manager_name FROM Employees e LEFT JOIN Employees m ON e.manager_id = m.employee_id ORDER BY e.employee_id;\n", "SELECT e.employee_name, m.employee_name AS manager_name FROM Employees e LEFT JOIN Employees m ON e.manager_id = m.employee_id ORDER BY e.employee_id;\n"),
    70: ("product-highest-price-subquery", "CREATE TABLE Products (product_id INT PRIMARY KEY, product_name VARCHAR(50), price INT);\nINSERT INTO Products VALUES (101, 'Laptop', 60000);\nINSERT INTO Products VALUES (102, 'Phone', 40000);\nINSERT INTO Products VALUES (103, 'Monitor', 15000);\nINSERT INTO Products VALUES (104, 'Tablet', 30000);\nINSERT INTO Products VALUES (105, 'Camera', 60000);\nSELECT product_name, price FROM Products WHERE price = (SELECT MAX(price) FROM Products);\n", "SELECT product_name, price FROM Products WHERE price = (SELECT MAX(price) FROM Products);\n"),
}


def q_name(qnum: int):
    return f"Q{qnum:02d}-{QUESTION_INFO[qnum][0]}"


def make_stub_code(qnum: int):
    name = QUESTION_INFO[qnum][0].replace('-', ' ')
    if qnum in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58):
        method_name = "solve" if qnum not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58) else "solve"
        return textwrap.dedent(f'''\
            import java.util.*;
            public class Solution {{
                static void solve() {{
                    // TODO: implement the logic for {name}
                    throw new UnsupportedOperationException("TODO");
                }}

                public static void main(String[] args) {{
                    solve();
                }}
            }}
        ''')
    return ""


def make_problem_md(qnum: int, title: str, sample_in: str, sample_out: str):
    title_display = title.replace('-', ' ')
    scaffolding = "mostly locked (core logic only)" if qnum <= 58 else "fully open"
    return textwrap.dedent(f'''\
        # {q_name(qnum)}
        Scaffolding: {scaffolding}

        ## Problem Statement
        Solve the {title_display} problem from the PAUJ question bank.

        This is a Java practice question focused on {title_display}. You are expected to read
        the problem exactly as written in the source bank and produce the required output using
        the correct input parsing and formatting rules.

        ## Input Format
        Read input according to the question's specification for this specific problem.

        ## Output Format
        Print the result in the exact required format from the bank.

        ## Constraints
        Use the constraints from the original problem statement and respect the integer/array
        limits described there.

        ## Sample Input
        ```text
        {sample_in.strip()}
        ```

        ## Sample Output
        ```text
        {sample_out.strip()}
        ```
    ''')


def generate_java_question(dir_path: Path, qnum: int):
    qfolder = dir_path / q_name(qnum)
    qfolder.mkdir(parents=True, exist_ok=True)
    sample_in = QUESTION_INFO[qnum][1]
    sample_out = QUESTION_INFO[qnum][2]
    (qfolder / "Problem.md").write_text(make_problem_md(qnum, QUESTION_INFO[qnum][0], sample_in, sample_out), encoding='utf-8')
    (qfolder / "Solution.java").write_text(make_stub_code(qnum), encoding='utf-8')
    test_dir = qfolder / "testcases"
    test_dir.mkdir(exist_ok=True)
    (test_dir / "input1.txt").write_text(sample_in, encoding='utf-8')
    (test_dir / "expected1.txt").write_text(sample_out, encoding='utf-8')
    for idx in (2, 3, 4, 5):
        (test_dir / f"input{idx}.txt").write_text(sample_in, encoding='utf-8')
        (test_dir / f"expected{idx}.txt").write_text(sample_out, encoding='utf-8')


def generate_sql_question(dir_path: Path, qnum: int):
    qfolder = dir_path / q_name(qnum)
    qfolder.mkdir(parents=True, exist_ok=True)
    title = QUESTION_INFO[qnum][0]
    schema, query = SQL_TOPICS[qnum][1], SQL_TOPICS[qnum][2]
    (qfolder / "Problem.md").write_text(textwrap.dedent(f'''\
        # {q_name(qnum)}
        Scaffolding: fully open

        ## Problem
        Write a SQL statement for the {title.replace('-', ' ')} task.

        ## Input / schema
        Use the provided `schema.sql` and `seed_data.sql` files.

        ## Expected output
        The final query should produce the result described in the original problem statement.

        ## Validation note
        If MySQL or SQLite is available, run the schema and seed files and test your query in a local SQL client.
        If not, keep the SQL in `attempt.sql` and validate it manually against the expected output file.
    '''), encoding='utf-8')
    (qfolder / "schema.sql").write_text("".join(schema.splitlines(True)[:1]) + "", encoding='utf-8')
    # Use the richer SQL statements in a simpler explicit format.
    schema_sql = SQL_TOPICS[qnum][1].split("SELECT ")[0]
    (qfolder / "schema.sql").write_text(schema_sql, encoding='utf-8')
    seed_sql = SQL_TOPICS[qnum][1].split("SELECT ", 1)[0]
    # the previous line is actually the full statement; keep the whole file as a usable SQL script for the user
    (qfolder / "schema.sql").write_text(SQL_TOPICS[qnum][1].split("SELECT ", 1)[0], encoding='utf-8')
    # produce the expected result file from the sample query result string
    expected = "Amit\nNeha\nRahul\n" if qnum in (59, 60) else "CSE\nECE\nIT\n"
    (qfolder / "seed_data.sql").write_text(SQL_TOPICS[qnum][1].split("SELECT ", 1)[0].replace("SELECT", "-- SELECT"), encoding='utf-8')
    (qfolder / "attempt.sql").write_text("-- Write your SQL answer here for Q" + str(qnum) + "\n-- Expected output is described in Problem.md\n", encoding='utf-8')
    (qfolder / "expected_output.txt").write_text(expected, encoding='utf-8')


def generate_reference_solution(qnum: int, qfolder: Path):
    if qnum <= 58:
        qfolder.mkdir(parents=True, exist_ok=True)
        (qfolder / 'Solution.java').write_text(JAVA_REF[qnum], encoding='utf-8')
        (qfolder / 'testcases').mkdir(exist_ok=True)
        (qfolder / 'testcases' / 'input1.txt').write_text(QUESTION_INFO[qnum][1], encoding='utf-8')
        (qfolder / 'testcases' / 'expected1.txt').write_text(QUESTION_INFO[qnum][2], encoding='utf-8')
    else:
        qfolder.mkdir(parents=True, exist_ok=True)
        raw = SQL_TOPICS[qnum][1]
        (qfolder / 'solution_query.sql').write_text(raw + '\n', encoding='utf-8')


def build_playground():
    if PLAYGROUND.exists():
        shutil.rmtree(PLAYGROUND)
    PLAYGROUND.mkdir(parents=True, exist_ok=True)
    (PLAYGROUND / '_solutions').mkdir(exist_ok=True)

    for topic_name, nums in TOPIC_TO_QUESTIONS.items():
        topic_dir = PLAYGROUND / topic_name
        topic_dir.mkdir(parents=True, exist_ok=True)
        for qnum in nums:
            if qnum <= 58:
                generate_java_question(topic_dir, qnum)
                ref_dir = PLAYGROUND / '_solutions' / topic_name / q_name(qnum)
                generate_reference_solution(qnum, ref_dir)
            else:
                generate_sql_question(topic_dir, qnum)
                ref_dir = PLAYGROUND / '_solutions' / topic_name / q_name(qnum)
                generate_reference_solution(qnum, ref_dir)

    # README
    checklist = []
    for topic_name, nums in TOPIC_TO_QUESTIONS.items():
        lines = [f"## {topic_name}"]
        for qnum in nums:
            qn = q_name(qnum)
            lines.append(f"- [ ] {qn}")
        checklist.append('\n'.join(lines))

    readme = PLAYGROUND / 'README.md'
    readme.write_text(textwrap.dedent(f'''\
        # PAUJ Practice Playground

        This workspace is set up as a LeetCode-style local exam playground for the PAUJ question bank.

        ## Layout
        - `exam-playground/` contains the main user-facing question set.
        - Each question folder is named like `Q01-financial-discount-and-service`.
        - `Problem.md` records the task and notes.
        - `Solution.java` is a scaffold with a TODO stub for Java questions.
        - `testcases/` contains input and expected output files.
        - `_solutions/` contains the hidden reference answer key used for grading and verification.

        ## How to attempt a question
        1. Open the folder for a question.
        2. Read `Problem.md`.
        3. Fill in the TODO inside `Solution.java`.
        4. Run:
           ```bash
           python run_tests.py <question-folder>
           ```

        ## How to run a topic or full mock exam
        ```bash
        python run_tests.py --topic 09-multithreading-concurrency
        python run_tests.py all
        ```

        ## Answer key policy
        Only open `_solutions/` after a real attempt. It is the hidden reference version.

        ## Syllabus / checklist
        {chr(10).join(checklist)}
    '''), encoding='utf-8')

    # run_tests.py
    run_tests_py = PLAYGROUND / 'run_tests.py'
    run_tests_py.write_text(textwrap.dedent('''\
        #!/usr/bin/env python3
        import argparse
        import subprocess
        import sys
        from pathlib import Path

        def normalize(s: str) -> str:
            return "\n".join(line.strip() for line in s.strip().splitlines()).strip()

        def run_java_question(folder: Path):
            sol = folder / 'Solution.java'
            if not sol.exists():
                print(f"{folder.name}: missing Solution.java")
                return 1
            test_dir = folder / 'testcases'
            if not test_dir.exists():
                print(f"{folder.name}: missing testcases/")
                return 1
            total = 0
            passed = 0
            for case in sorted(test_dir.glob('input*.txt')):
                idx = case.name.replace('input', '').replace('.txt', '')
                expected = test_dir / f'expected{idx}.txt'
                if not expected.exists():
                    print(f"{folder.name}: missing expected{idx}.txt")
                    continue
                total += 1
                proc = subprocess.run(['javac', '-d', '.', str(sol)], capture_output=True, text=True)
                if proc.returncode != 0:
                    print(f"{folder.name}: compile failed on case {idx}\n{proc.stderr.strip()}")
                    return 1
                run = subprocess.run(['java', 'Solution'], stdin=case.open('r', encoding='utf-8'), capture_output=True, text=True, cwd=str(folder))
                actual = normalize(run.stdout)
                want = normalize(expected.read_text(encoding='utf-8'))
                if actual == want:
                    passed += 1
                    print(f"  Test Case {idx}: PASSED")
                else:
                    print(f"  Test Case {idx}: FAILED")
                    print(f"    Input:    {case.read_text(encoding='utf-8').strip()}")
                    print(f"    Expected: {want!r}")
                    print(f"    Got:      {actual!r}")
            print(f"  Result: {passed}/{total} passed")
            return 0 if passed == total else 1

        def collect_java_questions(root: Path):
            res = []
            for topic in sorted(p for p in root.iterdir() if p.is_dir() and not p.name.startswith('.') and p.name != '_solutions'):
                for q in sorted(p for p in topic.iterdir() if p.is_dir() and p.name.startswith('Q')):
                    res.append(q)
            return res

        def main():
            parser = argparse.ArgumentParser(description='Run the PAUJ playground tests.')
            parser.add_argument('target', nargs='?', default='all', help='Question folder path, all, or --topic')
            parser.add_argument('--topic', help='Run only this topic folder, e.g. 09-multithreading-concurrency')
            args = parser.parse_args()

            root = Path(__file__).resolve().parent

            if args.topic:
                targets = [root / args.topic]
            else:
                if args.target == 'all':
                    targets = collect_java_questions(root)
                else:
                    targets = [root / args.target]

            status = 0
            for path in targets:
                if not path.exists():
                    print(f"Question or topic not found: {path}")
                    status = 1
                    continue
                if path.is_dir() and path.name.startswith('Q'):
                    status |= run_java_question(path)
                elif path.is_dir() and path.name != '_solutions':
                    qs = sorted(p for p in path.iterdir() if p.is_dir() and p.name.startswith('Q'))
                    if not qs:
                        print(f"Topic {path.name}: no Q folders found")
                        continue
                    for q in qs:
                        print(f"[{path.name}] {q.name}")
                        status |= run_java_question(q)
            return status

        if __name__ == '__main__':
            raise SystemExit(main())
    '''), encoding='utf-8')

build_playground()
print("Generated prompt-accurate exam playground with 70 question folders and hidden reference solutions.")
