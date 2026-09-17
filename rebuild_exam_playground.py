from pathlib import Path
import subprocess
import tempfile

root = Path(r"c:\Users\Yuvraj\Desktop\pauj-question_bank_ETE")
playground = root / "exam-playground"
playground.mkdir(exist_ok=True)

for topic in playground.iterdir():
    if topic.is_dir() and not topic.name.startswith('.'):
        for child in list(topic.iterdir()):
            if child.name.startswith('Q') and child.is_dir():
                for inner in list(child.iterdir()):
                    if inner.is_dir() and inner.name == 'testcases':
                        pass
        if topic.name != '_solutions':
            for child in list(topic.iterdir()):
                if child.name.startswith('Q'):
                    if child.is_dir():
                        for sub in list(child.iterdir()):
                            if sub.is_dir() and sub.name == 'testcases':
                                pass

# Canonical topic mapping: each question appears once.
topic_map = {
    "01-java-basics-oop": list(range(1, 6)),
    "02-arrays-strings": [6, 7, 8],
    "03-collections-stl": list(range(9, 17)),
    "04-exceptions-filehandling": [17, 18, 25],
    "05-streams": list(range(19, 25)),
    "06-lambdas-functional-interfaces": [32, 33, 34, 35, 46, 47, 48],
    "07-jvm-memory-io": list(range(37, 46)),
    "08-datetime-api": [30, 31, 36],
    "09-multithreading-concurrency": list(range(49, 59)),
    "10-normalization-java-logic": [26, 27, 28, 29],
    "11-sql-ddl-dml-constraints": [59, 60, 61],
    "12-sql-joins-subqueries-groupby": list(range(62, 71)),
}

q_names = {
    1: "Q01-financial-discount-and-service",
    2: "Q02-production-summary",
    3: "Q03-even-odd-digit-sum",
    4: "Q04-kg-to-grams",
    5: "Q05-product-inventory-value",
    6: "Q06-even-odd-rearrangement",
    7: "Q07-palindrome-sentence",
    8: "Q08-grade-calculator",
    9: "Q09-cancel-divisible-token-numbers",
    10: "Q10-vector-insert-after-id",
    11: "Q11-linkedlist-remove-first-occurrence",
    12: "Q12-high-unique-registration",
    13: "Q13-treeset-previous-smaller-score",
    14: "Q14-hashmap-product-quantity-total",
    15: "Q15-priorityqueue-first-k-sum",
    16: "Q16-generic-box",
    17: "Q17-withdrawal-validation",
    18: "Q18-custom-exception-score-validation",
    19: "Q19-marks-above-average",
    20: "Q20-top-three-distinct-distances",
    21: "Q21-total-salary-above-threshold",
    22: "Q22-stream-discount-mapping",
    23: "Q23-grouping-by-category",
    24: "Q24-even-square-sum",
    25: "Q25-safe-index-and-division",
    26: "Q26-normalize-to-1nf",
    27: "Q27-2nf-patient-summary",
    28: "Q28-3nf-student-summary",
    29: "Q29-3nf-faculty-allocation-summary",
    30: "Q30-reservation-checkout-date",
    31: "Q31-exam-end-time",
    32: "Q32-adjusted-consumption",
    33: "Q33-package-priority-score",
    34: "Q34-machine-safety-check",
    35: "Q35-optional-employee-lookup",
    36: "Q36-days-between-dates",
    37: "Q37-local-variables-vs-array",
    38: "Q38-method-local-total-marks",
    39: "Q39-garbage-collection-request",
    40: "Q40-final-salary",
    41: "Q41-square-stringbuilder-output",
    42: "Q42-buffered-input-sum",
    43: "Q43-buffered-temperature-report",
    44: "Q44-corrected-total-cost",
    45: "Q45-parking-fee",
    46: "Q46-functional-operation-argument",
    47: "Q47-uppercase-method-reference",
    48: "Q48-function-interface-quantity-rules",
    49: "Q49-thread-join-processing",
    50: "Q50-thread-class-order",
    51: "Q51-runnable-heart-monitor",
    52: "Q52-synchronized-withdrawal",
    53: "Q53-synchronized-ticket-booking",
    54: "Q54-synchronized-visitor-counter",
    55: "Q55-deadlock-prevention",
    56: "Q56-livelock-retry-management",
    57: "Q57-synchronized-submission-counter",
    58: "Q58-concurrent-login-records",
    59: "Q59-students-create-and-list",
    60: "Q60-cse-salary-increment",
    61: "Q61-book-price-deletion",
    62: "Q62-department-student-count",
    63: "Q63-customer-total-spent",
    64: "Q64-subject-average-marks",
    65: "Q65-customers-with-3-or-more-orders",
    66: "Q66-salary-above-average",
    67: "Q67-inner-join-students-departments",
    68: "Q68-left-join-employees-departments",
    69: "Q69-self-join-manager-list",
    70: "Q70-product-highest-price-subquery",
}

java_templates = {
    1: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int original = sc.nextInt();\n        double discountPercent = sc.nextDouble();\n        double servicePercent = sc.nextDouble();\n        double discount = original * discountPercent / 100.0;\n        double amountAfterDiscount = original - discount;\n        double serviceCharge = amountAfterDiscount * servicePercent / 100.0;\n        double finalAmount = amountAfterDiscount + serviceCharge;\n        System.out.printf(\"%.2f\", finalAmount);\n    }\n}\n""",
    2: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int[] arr = new int[n];\n        int total = 0, min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;\n        for (int i = 0; i < n; i++) {\n            arr[i] = sc.nextInt();\n            total += arr[i];\n            min = Math.min(min, arr[i]);\n            max = Math.max(max, arr[i]);\n        }\n        System.out.println(total);\n        System.out.printf(\"%.2f\\n\", total / (double) n);\n        System.out.println(max - min);\n    }\n}\n""",
    3: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int even = 0, odd = 0;\n        while (n > 0) {\n            int d = n % 10;\n            if (d % 2 == 0) even += d;\n            else odd += d;\n            n /= 10;\n        }\n        System.out.println(even);\n        System.out.println(odd);\n    }\n}\n""",
    4: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        long[] arr = new long[n];\n        for (int i = 0; i < n; i++) arr[i] = sc.nextLong();\n        for (int i = 0; i < n; i++) { if (i > 0) System.out.print(\" \" ); System.out.print(arr[i] * 1000L); }\n        System.out.println();\n    }\n}\n""",
    5: """import java.util.*;\nclass Product {\n    int productId; double price; int quantity;\n    Product(int id, double p, int q) { productId = id; price = p; quantity = q; }\n    double calculateValue() { return price * quantity; }\n}\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int id = sc.nextInt();\n        double price = sc.nextDouble();\n        int qty = sc.nextInt();\n        Product p = new Product(id, price, qty);\n        System.out.printf(\"%.2f\", p.calculateValue());\n    }\n}\n""",
    6: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int[] arr = new int[n];\n        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();\n        int write = 0;\n        for (int i = 0; i < n; i++) if (arr[i] % 2 == 0) { int tmp = arr[write]; arr[write] = arr[i]; arr[i] = tmp; write++; }\n        for (int i = 0; i < n; i++) if (arr[i] % 2 != 0) { int tmp = arr[write]; arr[write] = arr[i]; arr[i] = tmp; write++; }\n        for (int i = 0; i < n; i++) { if (i > 0) System.out.print(\" \" ); System.out.print(arr[i]); }\n        System.out.println();\n    }\n}\n""",
    7: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        sc.useDelimiter(\"\\n\");\n        String s = sc.next();\n        String cleaned = s.replace(\" \", \"\").toLowerCase();\n        String reverse = new StringBuilder(cleaned).reverse().toString();\n        System.out.println(cleaned.equals(reverse) ? \"Palindrome\" : \"Not Palindrome\");\n    }\n}\n""",
    8: """import java.util.*;\npublic class Solution {\n    static char calculateGrade(int marks) {\n        if (marks >= 90) return 'A';\n        if (marks >= 75) return 'B';\n        if (marks >= 60) return 'C';\n        if (marks >= 40) return 'D';\n        return 'F';\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        for (int i = 0; i < n; i++) { if (i > 0) System.out.print(\" \" ); System.out.print(calculateGrade(sc.nextInt())); }\n        System.out.println();\n    }\n}\n""",
    9: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        ArrayList<Integer> tokens = new ArrayList<>();\n        for (int i = 0; i < n; i++) tokens.add(sc.nextInt());\n        int cancel = sc.nextInt();\n        for (int i = tokens.size() - 1; i >= 0; i--) { if (tokens.get(i) % cancel == 0) tokens.remove(i); }\n        if (tokens.isEmpty()) System.out.println(-1);\n        else { for (int i = 0; i < tokens.size(); i++) { if (i > 0) System.out.print(\" \" ); System.out.print(tokens.get(i)); } System.out.println(); }\n    }\n}\n""",
    10: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        Vector<Integer> items = new Vector<>();\n        for (int i = 0; i < n; i++) items.add(sc.nextInt());\n        int target = sc.nextInt();\n        int value = sc.nextInt();\n        int idx = -1;\n        for (int i = 0; i < items.size(); i++) { if (items.get(i) == target) { idx = i; break; } }\n        if (idx == -1) System.out.println(\"Container Not Found\");\n        else { items.add(idx + 1, value); for (int i = 0; i < items.size(); i++) { if (i > 0) System.out.print(\" \" ); System.out.print(items.get(i)); } System.out.println(); }\n    }\n}\n""",
    11: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        LinkedList<Integer> list = new LinkedList<>();\n        for (int i = 0; i < n; i++) list.add(sc.nextInt());\n        int target = sc.nextInt();\n        if (!list.removeFirstOccurrence(target)) System.out.println(\"Task Not Found\");\n        else { for (int i = 0; i < list.size(); i++) { if (i > 0) System.out.print(\" \" ); System.out.print(list.get(i)); } System.out.println(); }\n    }\n}\n""",
    12: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        HashSet<Integer> set = new HashSet<>();\n        for (int i = 0; i < n; i++) set.add(sc.nextInt());\n        System.out.println(set.size() > (n / 2.0) ? \"High Unique Registration\" : \"Low Unique Registration\");\n    }\n}\n""",
    13: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        TreeSet<Integer> set = new TreeSet<>();\n        for (int i = 0; i < n; i++) set.add(sc.nextInt());\n        int target = sc.nextInt();\n        Integer floor = set.floor(target - 1);\n        System.out.println(floor == null ? -1 : floor);\n    }\n}\n""",
    14: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        Map<Integer, Integer> map = new HashMap<>();\n        for (int i = 0; i < n; i++) { map.put(sc.nextInt(), sc.nextInt()); }\n        int q = sc.nextInt();\n        int total = 0;\n        for (int i = 0; i < q; i++) total += map.getOrDefault(sc.nextInt(), 0);\n        System.out.println(total);\n    }\n}\n""",
    15: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        PriorityQueue<Integer> pq = new PriorityQueue<>();\n        for (int i = 0; i < n; i++) pq.add(sc.nextInt());\n        int k = sc.nextInt();\n        int sum = 0;\n        for (int i = 0; i < k; i++) sum += pq.poll();\n        System.out.println(sum);\n    }\n}\n""",
    16: """import java.util.*;\nclass Box<T> { private T value; Box(T value) { this.value = value; } T getValue() { return value; } }\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt();\n        double b = sc.nextDouble();\n        Box<Integer> x = new Box<>(a);\n        Box<Double> y = new Box<>(b);\n        System.out.println(x.getValue());\n        System.out.printf(\"%.2f\\n\", y.getValue());\n    }\n}\n""",
    17: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int balance = sc.nextInt();\n        int amount = sc.nextInt();\n        try {\n            if (amount <= 0) throw new IllegalArgumentException();\n            if (amount > balance) throw new ArithmeticException();\n            System.out.println(balance - amount);\n        } catch (IllegalArgumentException e) {\n            System.out.println(\"Invalid Amount\");\n        } catch (ArithmeticException e) {\n            System.out.println(\"Insufficient Balance\");\n        }\n    }\n}\n""",
    18: """import java.util.*;\nclass InvalidScoreException extends Exception { InvalidScoreException() { super(\"Invalid Score\"); } }\npublic class Solution {\n    static void validateScore(int score) throws InvalidScoreException { if (score < 0 || score > 100) throw new InvalidScoreException(); }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int score = sc.nextInt();\n        try { validateScore(score); System.out.println(score); } catch (InvalidScoreException e) { System.out.println(\"Invalid Score\"); }\n    }\n}\n""",
    19: """import java.util.*;\nimport java.util.stream.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int[] marks = new int[n];\n        for (int i = 0; i < n; i++) marks[i] = sc.nextInt();\n        double avg = IntStream.of(marks).average().orElse(0.0);\n        List<Integer> ans = IntStream.range(0, marks.length).filter(i -> marks[i] > avg).mapToObj(i -> marks[i]).collect(Collectors.toList());\n        if (ans.isEmpty()) System.out.println(-1);\n        else { for (int i = 0; i < ans.size(); i++) { if (i > 0) System.out.print(\" \" ); System.out.print(ans.get(i)); } System.out.println(); }\n    }\n}\n""",
    20: """import java.util.*;\nimport java.util.stream.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        List<Integer> list = new ArrayList<>();\n        for (int i = 0; i < n; i++) list.add(sc.nextInt());\n        List<Integer> ans = list.stream().distinct().sorted(Comparator.reverseOrder()).limit(3).collect(Collectors.toList());\n        for (int i = 0; i < ans.size(); i++) { if (i > 0) System.out.print(\" \" ); System.out.print(ans.get(i)); }\n        System.out.println();\n    }\n}\n""",
    21: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int total = 0;\n        for (int i = 0; i < n; i++) total += sc.nextInt();\n        int threshold = sc.nextInt();\n        System.out.println(total > threshold ? total : 0);\n    }\n}\n""",
    22: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int[] arr = new int[n];\n        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();\n        for (int i = 0; i < n; i++) { if (i > 0) System.out.print(\" \" ); System.out.print(arr[i] >= 1000 ? Math.round(arr[i] * 0.85f) : Math.round(arr[i] * 0.95f)); }\n        System.out.println();\n    }\n}\n""",
    23: """import java.util.*;\nimport java.util.stream.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int[] arr = new int[n];\n        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();\n        Map<String, Long> map = Arrays.stream(arr).boxed().collect(Collectors.groupingBy(x -> x >= 75 ? \"High\" : x >= 50 ? \"Medium\" : \"Low\", Collectors.counting()));\n        System.out.println(map.getOrDefault(\"High\", 0L));\n        System.out.println(map.getOrDefault(\"Medium\", 0L));\n        System.out.println(map.getOrDefault(\"Low\", 0L));\n    }\n}\n""",
    24: """import java.util.*;\nimport java.util.stream.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int[] arr = new int[n];\n        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();\n        System.out.println(IntStream.of(arr).filter(x -> x % 2 == 0).map(x -> x * x).sum());\n    }\n}\n""",
    25: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int[] arr = new int[n];\n        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();\n        int idx = sc.nextInt();\n        int div = sc.nextInt();\n        try {\n            System.out.println(arr[idx] / div);\n        } catch (ArrayIndexOutOfBoundsException e) {\n            System.out.println(\"Invalid Index\");\n        } catch (ArithmeticException e) {\n            System.out.println(\"Division By Zero\");\n        }\n    }\n}\n""",
    26: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        sc.nextLine();\n        for (int i = 0; i < n; i++) {\n            String line = sc.nextLine();\n            String[] parts = line.split(\" \", 2);\n            String[] values = parts[1].split(\",\");\n            for (String v : values) System.out.println(parts[0] + \" \" + v);\n        }\n    }\n}\n""",
    27: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        Map<Integer, Integer> counts = new LinkedHashMap<>();\n        for (int i = 0; i < n; i++) {\n            int a = sc.nextInt();\n            String name = sc.next();\n            int b = sc.nextInt();\n            String doc = sc.next();\n            counts.put(a, counts.getOrDefault(a, 0) + 1);\n        }\n        for (Map.Entry<Integer, Integer> e : counts.entrySet()) System.out.println(e.getKey() + \" \" + e.getValue());\n    }\n}\n""",
    28: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        Map<Integer, String> names = new LinkedHashMap<>();\n        for (int i = 0; i < n; i++) { int id = sc.nextInt(); String name = sc.next(); int dept = sc.nextInt(); String dname = sc.next(); names.putIfAbsent(id, name + \" \" + dname); }\n        for (Map.Entry<Integer, String> e : names.entrySet()) System.out.println(e.getKey() + \" \" + e.getValue());\n    }\n}\n""",
    29: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        Set<Integer> seen = new HashSet<>();\n        for (int i = 0; i < n; i++) { int id = sc.nextInt(); int fid = sc.nextInt(); String name = sc.next(); int room = sc.nextInt(); if (seen.add(fid)) System.out.println(fid + \" \" + name + \" \" + room); }\n    }\n}\n""",
    30: """import java.util.*;\nimport java.time.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        LocalDate start = LocalDate.parse(sc.nextLine());\n        int days = sc.nextInt();\n        int with = sc.nextInt();\n        LocalDate out = start.plusDays(days);\n        System.out.println(out);\n        System.out.println(days - with);\n    }\n}\n""",
    31: """import java.util.*;\nimport java.time.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        LocalDate d = LocalDate.parse(sc.nextLine());\n        LocalTime t = LocalTime.parse(sc.nextLine());\n        int extra = sc.nextInt();\n        LocalDateTime end = LocalDateTime.of(d, t).plusMinutes(extra);\n        System.out.println(end.toLocalDate());\n        System.out.println(end.toLocalTime());\n    }\n}\n""",
    32: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        double[] arr = new double[n];\n        for (int i = 0; i < n; i++) arr[i] = sc.nextDouble();\n        for (int i = 0; i < n; i++) { if (i > 0) System.out.print(\" \" ); System.out.printf(\"%.2f\", arr[i] * 1.10); }\n        System.out.println();\n    }\n}\n""",
    33: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int[] arr = new int[n];\n        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();\n        for (int i = 0; i < n; i++) { if (i > 0) System.out.print(\" \" ); System.out.print(arr[i] * 2 + 10); }\n        System.out.println();\n    }\n}\n""",
    34: """import java.util.*;\n@FunctionalInterface\ninterface SafetyCheck { boolean apply(int temp); }\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        SafetyCheck check = t -> t >= 20 && t <= 80;\n        for (int i = 0; i < n; i++) { if (i > 0) System.out.print(\" \" ); System.out.print(check.apply(sc.nextInt()) ? \"Safe\" : \"Unsafe\"); }\n        System.out.println();\n    }\n}\n""",
    35: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        Map<Integer, String> map = new HashMap<>();\n        for (int i = 0; i < n; i++) map.put(sc.nextInt(), sc.next());\n        int key = sc.nextInt();\n        System.out.println(map.getOrDefault(key, \"Employee Not Found\"));\n    }\n}\n""",
    36: """import java.util.*;\nimport java.time.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        LocalDate start = LocalDate.parse(sc.nextLine());\n        LocalDate end = LocalDate.parse(sc.nextLine());\n        System.out.println(ChronoUnit.DAYS.between(start, end));\n    }\n}\n""",
    37: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt(); int b = sc.nextInt(); int c = sc.nextInt();\n        int[] arr = new int[]{sc.nextInt(), sc.nextInt(), sc.nextInt()};\n        System.out.println(a + \" \" + b + \" \" + c);\n        for (int i = 0; i < arr.length; i++) { if (i > 0) System.out.print(\" \" ); System.out.print(arr[i]); }\n        System.out.println();\n    }\n}\n""",
    38: """import java.util.*;\npublic class Solution {\n    static int total(int a, int b, int c) { return a + b + c; }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt(); int b = sc.nextInt(); int c = sc.nextInt();\n        System.out.println(total(a, b, c));\n    }\n}\n""",
    39: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        List<String> temp = new ArrayList<>();\n        for (int i = 0; i < n; i++) temp.add(\"obj\" + i);\n        temp.clear();\n        System.gc();\n        System.out.println(\"Garbage Collection Requested\");\n    }\n}\n""",
    40: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int basic = sc.nextInt();\n        int allowance = sc.nextInt();\n        int deduction = sc.nextInt();\n        System.out.println(basic + allowance - deduction);\n    }\n}\n""",
    41: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int[] arr = new int[n];\n        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();\n        StringBuilder sb = new StringBuilder();\n        for (int i = 0; i < n; i++) { if (i > 0) sb.append(' '); sb.append(arr[i] * arr[i]); }\n        System.out.println(sb);\n    }\n}\n""",
    42: """import java.io.*;\npublic class Solution {\n    public static void main(String[] args) throws Exception {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        int n = Integer.parseInt(br.readLine());\n        String[] tokens = br.readLine().split(\" \");\n        int sum = 0;\n        for (String token : tokens) sum += Integer.parseInt(token);\n        System.out.println(sum);\n    }\n}\n""",
    43: """import java.io.*;\npublic class Solution {\n    public static void main(String[] args) throws Exception {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        int n = Integer.parseInt(br.readLine());\n        String[] tokens = br.readLine().split(\" \");\n        StringBuilder sb = new StringBuilder();\n        for (int i = 0; i < tokens.length; i++) { if (i > 0) sb.append(' '); sb.append(Integer.parseInt(tokens[i]) + 2); }\n        System.out.println(sb);\n    }\n}\n""",
    44: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int total = 0;\n        for (int i = 0; i < n; i++) { int qty = sc.nextInt(); int price = sc.nextInt(); total += qty * price; }\n        System.out.println(total);\n    }\n}\n""",
    45: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int hours = sc.nextInt();\n        int fee = 0;\n        if (hours <= 0) fee = 0;\n        else if (hours <= 2) fee = hours * 20;\n        else fee = hours * 40;\n        System.out.println(fee);\n    }\n}\n""",
    46: """import java.util.*;\ninterface Operation { int apply(int x, int y); }\npublic class Solution {\n    static int applyOperation(int amount, int value, String type) {\n        Operation op = type.equals(\"ADD\") ? (x, y) -> x + y : (x, y) -> x * y;\n        return op.apply(amount, value);\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int amount = sc.nextInt();\n        int value = sc.nextInt();\n        String type = sc.next();\n        System.out.println(applyOperation(amount, value, type));\n    }\n}\n""",
    47: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        String[] arr = new String[n];\n        for (int i = 0; i < n; i++) arr[i] = sc.next();\n        for (int i = 0; i < n; i++) { if (i > 0) System.out.print(\" \" ); System.out.print(arr[i].toUpperCase()); }\n        System.out.println();\n    }\n}\n""",
    48: """import java.util.*;\nimport java.util.function.*;\npublic class Solution {\n    static int countGreater(List<Integer> vals) {\n        Predicate<Integer> p = v -> v > 50;\n        int c = 0; for (int v : vals) if (p.test(v)) c++; return c;\n    }\n    static List<Integer> addSafety(List<Integer> vals) {\n        Function<Integer, Integer> f = v -> v + 10;\n        ArrayList<Integer> out = new ArrayList<>(); for (int v : vals) out.add(f.apply(v)); return out;\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        List<Integer> vals = new ArrayList<>(); for (int i = 0; i < n; i++) vals.add(sc.nextInt());\n        System.out.println(countGreater(vals));\n        List<Integer> out = addSafety(vals);\n        for (int i = 0; i < out.size(); i++) { if (i > 0) System.out.print(\" \" ); System.out.print(out.get(i)); }\n        System.out.println();\n    }\n}\n""",
    49: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) throws Exception {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        Thread t = new Thread(() -> System.out.println(\"Tickets Processed: \" + n));\n        t.start();\n        t.join();\n        System.out.println(\"Processing Completed\");\n    }\n}\n""",
    50: """import java.util.*;\nclass OrderThread extends Thread {\n    int id; OrderThread(int id) { this.id = id; }\n    public void run() { System.out.println(\"Order \" + id + \" Processing\"); }\n}\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int id = sc.nextInt();\n        new OrderThread(id).start();\n    }\n}\n""",
    51: """import java.util.*;\nclass MonitoringTask implements Runnable {\n    int[] arr; MonitoringTask(int[] arr) { this.arr = arr; }\n    public void run() { for (int v : arr) System.out.println(\"Monitoring: \" + v); }\n}\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int[] arr = new int[n];\n        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();\n        new Thread(new MonitoringTask(arr)).start();\n    }\n}\n""",
    52: """import java.util.*;\nclass BankAccount { private int balance; BankAccount(int b) { balance = b; } synchronized void withdraw(int amount) { if (amount > balance) { System.out.println(\"Insufficient Balance\"); return; } balance -= amount; } int getBalance() { return balance; } }\npublic class Solution {\n    public static void main(String[] args) throws Exception {\n        Scanner sc = new Scanner(System.in);\n        BankAccount account = new BankAccount(sc.nextInt());\n        int a = sc.nextInt(); int b = sc.nextInt();\n        Thread t1 = new Thread(() -> account.withdraw(a));\n        Thread t2 = new Thread(() -> account.withdraw(b));\n        t1.start(); t2.start(); t1.join(); t2.join();\n        System.out.println(\"Final Balance: \" + account.getBalance());\n    }\n}\n""",
    53: """import java.util.*;\nclass TicketBooking { private int tickets; TicketBooking(int t) { tickets = t; } synchronized void book(int req) { if (req <= tickets) tickets -= req; } int rem() { return tickets; } }\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        TicketBooking tb = new TicketBooking(sc.nextInt());\n        int req = sc.nextInt();\n        tb.book(req);\n        System.out.println(\"Tickets Remaining: \" + tb.rem());\n    }\n}\n""",
    54: """import java.util.*;\nclass Counter { private int count = 0; synchronized void add(int n) { count += n; } int value() { return count; } }\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        Counter c = new Counter();\n        c.add(sc.nextInt()); c.add(sc.nextInt());\n        System.out.println(\"Total Visitors: \" + c.value());\n    }\n}\n""",
    55: """import java.util.*;\nclass Resource { }\npublic class Solution {\n    static void doWork(Resource a, Resource b, String threadName) {\n        synchronized (a) { synchronized (b) { System.out.println(threadName + \" Completed\"); } }\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt(); int b = sc.nextInt();\n        Resource r1 = new Resource(); Resource r2 = new Resource();\n        doWork(r1, r2, \"Thread 1\");\n        doWork(r1, r2, \"Thread 2\");\n        System.out.println(\"Production Completed\");\n    }\n}\n""",
    56: """import java.util.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int attempts = sc.nextInt();\n        System.out.println(\"Communication Started\");\n        for (int i = 0; i < attempts - 1; i++) System.out.println(\"Retrying\");\n        System.out.println(\"Message Sent Successfully\");\n        System.out.println(\"Communication Completed\");\n    }\n}\n""",
    57: """import java.util.*;\nclass SubmissionCounter { private int count = 0; synchronized void add(int n) { count += n; } int value() { return count; } }\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        SubmissionCounter c = new SubmissionCounter();\n        c.add(sc.nextInt()); c.add(sc.nextInt());\n        System.out.println(\"Total Submissions: \" + c.value());\n    }\n}\n""",
    58: """import java.util.*;\nimport java.util.concurrent.*;\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt(); int b = sc.nextInt();\n        Set<String> set = ConcurrentHashMap.newKeySet();\n        for (int i = 0; i < a; i++) set.add(\"login-\" + i);\n        for (int i = 0; i < b; i++) set.add(\"login-\" + i);\n        System.out.println(\"Total Login Records: \" + set.size());\n    }\n}\n""",
}

sample_inputs = {
    1: "5000\n10.5\n5.0\n",
    2: "5\n420 510 380 600 490\n",
    3: "583241\n",
    4: "4\n12 25 40 8\n",
    5: "105\n1250.50\n8\n",
    6: "8\n7 4 9 2 6 11 8 5\n",
    7: "Never Odd Or Even\n",
    8: "6\n92 76 65 48 35 88\n",
    9: "8\n12 15 18 21 24 25 30 31\n3\n",
    10: "5\n201 305 410 512 620\n410\n999\n",
    11: "7\n101 205 310 205 415 520 610\n205\n",
    12: "8\n101 102 103 101 104 105 106 102\n",
    13: "8\n45 72 88 65 72 91 54 80\n75\n",
    14: "5\n101 20\n102 35\n103 15\n104 50\n105 25\n4\n101 103 105 110\n",
    15: "7\n18 5 12 30 9 25 3\n3\n",
    16: "250\n45.75\n",
    17: "25000\n7500\n",
    18: "85\n",
    19: "6\n40 55 70 80 65 50\n",
    20: "8\n120 450 300 450 700 120 550 700\n",
    21: "6\n35000 52000 48000 75000 42000 90000\n50000\n",
    22: "6\n500 1200 800 2000 1500 900\n",
    23: "8\n82 45 67 91 38 75 54 49\n",
    24: "6\n3 4 6 5 8 7\n",
    25: "5\n20 40 60 80 100\n2\n10\n",
    26: "3\n201 Java,Python,DBMS\n202 HTML,CSS\n203 JavaScript,React\n",
    27: "6\n501 Rahul 301 Checkup DrKumar\n502 Neha 302 XRay DrSharma\n501 Rahul 303 BloodTest DrMehta\n503 Aman 301 Checkup DrKumar\n502 Neha 304 MRI DrSingh\n501 Rahul 305 ECG DrPatel\n",
    28: "6\n201 Arjun 10 ComputerScience\n202 Priya 20 Commerce\n203 Karan 10 ComputerScience\n201 Arjun 10 ComputerScience\n204 Sneha 30 Mathematics\n202 Priya 20 Commerce\n",
    29: "7\n101 501 Sharma 201\n102 502 Mehta 202\n103 501 Sharma 201\n104 503 Gupta 203\n105 502 Mehta 202\n106 504 Singh 204\n107 501 Sharma 201\n",
    30: "2026-08-10\n30\n12\n",
    31: "2026-09-14\n22:30\n120\n",
    32: "4\n100 200 300 400\n",
    33: "3\n10 25 40\n",
    34: "5\n25 80 90 15 50\n",
    35: "3\n101 Amit\n102 Neha\n103 Rahul\n102\n",
    36: "2026-09-01\n2026-09-15\n",
    37: "10 20 30\n40 50 60\n",
    38: "75 82 90\n",
    39: "100\n",
    40: "30000\n5000\n2000\n",
    41: "5\n2 3 4 5 6\n",
    42: "5\n10 20 30 40 50\n",
    43: "4\n20 25 30 35\n",
    44: "3\n2 100\n5 50\n3 200\n",
    45: "2\n",
    46: "1000\n50\nADD\n",
    47: "3\namit neha rahul\n",
    48: "5\n20 60 45 80 100\n",
    49: "5\n",
    50: "105\n",
    51: "3\n72 80 76\n",
    52: "10000\n3000\n4000\n",
    53: "10\n6\n",
    54: "5000\n7000\n",
    55: "10\n20\n",
    56: "3\n",
    57: "2500\n3500\n",
    58: "4000\n6000\n",
}

# Clean and rebuild the playground from canonical mapping.
for topic_name in sorted(p for p in playground.iterdir() if p.is_dir()):
    if topic_name.name == '_solutions':
        # remove stale mirrored solutions
        for child in list(topic_name.iterdir()):
            if child.is_dir():
                for sub in list(child.iterdir()):
                    if sub.is_dir():
                        for inner in list(sub.iterdir()):
                            if inner.is_dir():
                                for leaf in list(inner.iterdir()):
                                    if leaf.is_file():
                                        leaf.unlink()
                                inner.rmdir()
                            elif inner.is_file():
                                inner.unlink()
                        sub.rmdir()
                    elif sub.is_file():
                        sub.unlink()
                child.rmdir()
        continue
    for child in list(topic_name.iterdir()):
        if child.name.startswith('Q'):
            for sub in list(child.iterdir()):
                if sub.is_file():
                    sub.unlink()
            child.rmdir()

solutions_root = playground / '_solutions'
solutions_root.mkdir(exist_ok=True)

for topic_name, nums in topic_map.items():
    topic_dir = playground / topic_name
    topic_dir.mkdir(exist_ok=True)
    for num in nums:
        folder_name = q_names[num]
        q_dir = topic_dir / folder_name
        q_dir.mkdir(exist_ok=True)

        if num <= 58:
            (q_dir / 'Solution.java').write_text(java_templates[num], encoding='utf-8')
            test_dir = q_dir / 'testcases'
            test_dir.mkdir(exist_ok=True)
            inp = sample_inputs.get(num, '')
            (test_dir / 'input1.txt').write_text(inp, encoding='utf-8')

            with tempfile.TemporaryDirectory() as td:
                compile_result = subprocess.run(['javac', '-d', td, str(q_dir / 'Solution.java')], capture_output=True, text=True)
                if compile_result.returncode != 0:
                    raise RuntimeError(f"Compile failed for {folder_name}: {compile_result.stderr}")
                proc = subprocess.run(['java', '-cp', td, 'Solution'], input=inp, capture_output=True, text=True)
                expected = proc.stdout.strip() + '\n'
            (test_dir / 'expected1.txt').write_text(expected, encoding='utf-8')

            mirror_dir = solutions_root / topic_name / folder_name
            mirror_dir.mkdir(parents=True, exist_ok=True)
            (mirror_dir / 'Solution.java').write_text(java_templates[num], encoding='utf-8')
        else:
            q_dir.joinpath('Problem.md').write_text(f'# Problem\n\nQuestion {num}\n', encoding='utf-8')
            sql_text = {
                59: "CREATE TABLE Students (student_id INT PRIMARY KEY, student_name VARCHAR(50) NOT NULL, email VARCHAR(100) UNIQUE, age INT CHECK (age BETWEEN 17 AND 60), course VARCHAR(50));\nINSERT INTO Students VALUES (101, 'Amit', 'amit@gmail.com', 20, 'CSE');\nINSERT INTO Students VALUES (102, 'Neha', 'neha@gmail.com', 21, 'ECE');\nINSERT INTO Students VALUES (103, 'Rahul', 'rahul@gmail.com', 22, 'CSE');\nSELECT * FROM Students ORDER BY student_id;",
                60: "CREATE TABLE Employees (employee_id INT PRIMARY KEY, employee_name VARCHAR(50), department VARCHAR(50), salary DECIMAL(10,2));\nINSERT INTO Employees VALUES (101, 'Amit', 'CSE', 50000);\nINSERT INTO Employees VALUES (102, 'Neha', 'ECE', 45000);\nINSERT INTO Employees VALUES (103, 'Rahul', 'CSE', 60000);\nINSERT INTO Employees VALUES (104, 'Simran', 'IT', 55000);\nUPDATE Employees SET salary = salary * 1.10 WHERE department = 'CSE';\nSELECT employee_name, department, salary FROM Employees ORDER BY employee_id;",
                61: "CREATE TABLE Books (book_id INT PRIMARY KEY, title VARCHAR(50), author VARCHAR(50), price INT);\nINSERT INTO Books VALUES (101, 'Java', 'James', 550);\nINSERT INTO Books VALUES (102, 'SQL', 'Korth', 250);\nINSERT INTO Books VALUES (103, 'Python', 'Rossum', 650);\nINSERT INTO Books VALUES (104, 'Networks', 'Tanenbaum', 300);\nINSERT INTO Books VALUES (105, 'OS', 'Galvin', 200);\nDELETE FROM Books WHERE price < 300;\nSELECT * FROM Books ORDER BY book_id;",
                62: "CREATE TABLE Students (student_id INT PRIMARY KEY, student_name VARCHAR(50), department VARCHAR(50));\nINSERT INTO Students VALUES (101, 'Amit', 'CSE');\nINSERT INTO Students VALUES (102, 'Neha', 'ECE');\nINSERT INTO Students VALUES (103, 'Rahul', 'CSE');\nINSERT INTO Students VALUES (104, 'Simran', 'IT');\nINSERT INTO Students VALUES (105, 'Karan', 'CSE');\nINSERT INTO Students VALUES (106, 'Priya', 'ECE');\nSELECT department, COUNT(*) AS student_count FROM Students GROUP BY department ORDER BY department;",
                63: "CREATE TABLE Orders (order_id INT PRIMARY KEY, customer_id INT, amount INT);\nINSERT INTO Orders VALUES (1, 101, 1200);\nINSERT INTO Orders VALUES (2, 102, 800);\nINSERT INTO Orders VALUES (3, 101, 1500);\nINSERT INTO Orders VALUES (4, 103, 2000);\nINSERT INTO Orders VALUES (5, 102, 700);\nSELECT customer_id, SUM(amount) AS total_amount FROM Orders GROUP BY customer_id ORDER BY customer_id;",
                64: "CREATE TABLE Marks (student_id INT, subject VARCHAR(20), marks INT);\nINSERT INTO Marks VALUES (101, 'Java', 80);\nINSERT INTO Marks VALUES (102, 'Java', 90);\nINSERT INTO Marks VALUES (103, 'DBMS', 70);\nINSERT INTO Marks VALUES (104, 'DBMS', 80);\nINSERT INTO Marks VALUES (105, 'Java', 100);\nINSERT INTO Marks VALUES (106, 'DBMS', 90);\nSELECT subject, ROUND(AVG(marks), 2) AS average_marks FROM Marks GROUP BY subject ORDER BY subject;",
                65: "CREATE TABLE Orders (order_id INT PRIMARY KEY, customer_id INT, amount INT);\nINSERT INTO Orders VALUES (1, 101, 500);\nINSERT INTO Orders VALUES (2, 102, 700);\nINSERT INTO Orders VALUES (3, 101, 400);\nINSERT INTO Orders VALUES (4, 103, 900);\nINSERT INTO Orders VALUES (5, 101, 600);\nINSERT INTO Orders VALUES (6, 102, 300);\nINSERT INTO Orders VALUES (7, 101, 800);\nSELECT customer_id, COUNT(*) AS order_count FROM Orders GROUP BY customer_id HAVING COUNT(*) >= 3;",
                66: "CREATE TABLE Employees (employee_id INT PRIMARY KEY, employee_name VARCHAR(50), salary INT);\nINSERT INTO Employees VALUES (101, 'Amit', 40000);\nINSERT INTO Employees VALUES (102, 'Neha', 60000);\nINSERT INTO Employees VALUES (103, 'Rahul', 50000);\nINSERT INTO Employees VALUES (104, 'Simran', 80000);\nINSERT INTO Employees VALUES (105, 'Karan', 30000);\nSELECT employee_name, salary FROM Employees WHERE salary > (SELECT AVG(salary) FROM Employees) ORDER BY salary DESC;",
                67: "CREATE TABLE Students (student_id INT PRIMARY KEY, student_name VARCHAR(50), department_id INT);\nCREATE TABLE Departments (department_id INT PRIMARY KEY, department_name VARCHAR(50));\nINSERT INTO Students VALUES (101, 'Amit', 10);\nINSERT INTO Students VALUES (102, 'Neha', 20);\nINSERT INTO Students VALUES (103, 'Rahul', 10);\nINSERT INTO Departments VALUES (10, 'CSE');\nINSERT INTO Departments VALUES (20, 'ECE');\nSELECT s.student_name, d.department_name FROM Students s INNER JOIN Departments d ON s.department_id = d.department_id ORDER BY s.student_id;",
                68: "CREATE TABLE Employees (employee_id INT PRIMARY KEY, employee_name VARCHAR(50), department_id INT);\nCREATE TABLE Departments (department_id INT PRIMARY KEY, department_name VARCHAR(50));\nINSERT INTO Employees VALUES (101, 'Amit', 10);\nINSERT INTO Employees VALUES (102, 'Neha', NULL);\nINSERT INTO Employees VALUES (103, 'Rahul', 20);\nINSERT INTO Departments VALUES (10, 'CSE');\nINSERT INTO Departments VALUES (20, 'ECE');\nSELECT e.employee_name, d.department_name FROM Employees e LEFT JOIN Departments d ON e.department_id = d.department_id ORDER BY e.employee_id;",
                69: "CREATE TABLE Employees (employee_id INT PRIMARY KEY, employee_name VARCHAR(50), manager_id INT NULL);\nINSERT INTO Employees VALUES (101, 'Amit', NULL);\nINSERT INTO Employees VALUES (102, 'Neha', 101);\nINSERT INTO Employees VALUES (103, 'Rahul', 101);\nINSERT INTO Employees VALUES (104, 'Simran', 102);\nSELECT e.employee_name, m.employee_name AS manager_name FROM Employees e LEFT JOIN Employees m ON e.manager_id = m.employee_id ORDER BY e.employee_id;",
                70: "CREATE TABLE Products (product_id INT PRIMARY KEY, product_name VARCHAR(50), price INT);\nINSERT INTO Products VALUES (101, 'Laptop', 60000);\nINSERT INTO Products VALUES (102, 'Phone', 40000);\nINSERT INTO Products VALUES (103, 'Monitor', 15000);\nINSERT INTO Products VALUES (104, 'Tablet', 30000);\nINSERT INTO Products VALUES (105, 'Camera', 60000);\nSELECT product_name, price FROM Products WHERE price = (SELECT MAX(price) FROM Products);",
            }[num]
            (q_dir / 'schema.sql').write_text(sql_text, encoding='utf-8')
            mirror_dir = solutions_root / topic_name / folder_name
            mirror_dir.mkdir(parents=True, exist_ok=True)
            (mirror_dir / 'solution.sql').write_text(sql_text, encoding='utf-8')

# README summary.
readme = playground / 'README.md'
readme.write_text(
    '# Exam Playground\n\n'
    'This repository contains the PAUJ question-bank practice set with one canonical folder per numbered question.\n\n'
    '## Current structure\n'
    '- 1-5: Java basics/OOP\n'
    '- 6-8: arrays and strings\n'
    '- 9-16: collections and STL\n'
    '- 17-18, 25: exception handling and safe access\n'
    '- 19-24: streams\n'
    '- 26-29: normalization logic\n'
    '- 30-31, 36: date/time API\n'
    '- 32-35, 46-48: lambdas and functional interfaces\n'
    '- 37-45: JVM / memory / I/O\n'
    '- 49-58: multithreading and concurrency\n'
    '- 59-61: SQL DDL, DML, constraints\n'
    '- 62-70: SQL joins, subqueries, grouping\n\n'
    '## Validation\n'
    'Use `python run_tests.py --topic <folder>` to validate individual topics.\n',
    encoding='utf-8'
)

print('Rebuilt canonical playground structure for 70 unique questions.')
