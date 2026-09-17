from pathlib import Path
import re
import shutil
import textwrap

ROOT = Path(r"c:\Users\Yuvraj\Desktop\pauj-question_bank_ETE")
SOURCE = ROOT / "question_bank_extracted.txt"
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

TOPIC_LABELS = {
    "01-java-basics-oop": "Java basics and OOP",
    "02-arrays-strings": "Arrays and strings",
    "03-collections-stl": "Collections and STL",
    "04-exceptions-filehandling": "Exceptions and file handling",
    "05-streams": "Streams",
    "06-lambdas-functional-interfaces": "Lambdas and functional interfaces",
    "07-jvm-memory-io": "JVM, memory, and I/O",
    "08-datetime-api": "Date-Time API",
    "09-multithreading-concurrency": "Multithreading and concurrency",
    "10-normalization-java-logic": "Normalization and Java logic",
    "11-sql-ddl-dml-constraints": "SQL DDL, DML, and constraints",
    "12-sql-joins-subqueries-groupby": "SQL joins, subqueries, and grouping",
}

SQL_SCHEMA = {
    59: "CREATE TABLE Students (student_id INT PRIMARY KEY, student_name VARCHAR(50) NOT NULL, email VARCHAR(100) UNIQUE, age INT CHECK (age BETWEEN 17 AND 60), course VARCHAR(50));\n",
    60: "CREATE TABLE Employees (employee_id INT PRIMARY KEY, employee_name VARCHAR(50), department VARCHAR(50), salary DECIMAL(10,2));\n",
    61: "CREATE TABLE Books (book_id INT PRIMARY KEY, title VARCHAR(50), author VARCHAR(50), price INT);\n",
    62: "CREATE TABLE Students (student_id INT PRIMARY KEY, student_name VARCHAR(50), department VARCHAR(50));\n",
    63: "CREATE TABLE Orders (order_id INT PRIMARY KEY, customer_id INT, amount INT);\n",
    64: "CREATE TABLE Marks (student_id INT, subject VARCHAR(20), marks INT);\n",
    65: "CREATE TABLE Orders (order_id INT PRIMARY KEY, customer_id INT, amount INT);\n",
    66: "CREATE TABLE Employees (employee_id INT PRIMARY KEY, employee_name VARCHAR(50), salary INT);\n",
    67: "CREATE TABLE Students (student_id INT PRIMARY KEY, student_name VARCHAR(50), department_id INT);\nCREATE TABLE Departments (department_id INT PRIMARY KEY, department_name VARCHAR(50));\n",
    68: "CREATE TABLE Employees (employee_id INT PRIMARY KEY, employee_name VARCHAR(50), department_id INT);\nCREATE TABLE Departments (department_id INT PRIMARY KEY, department_name VARCHAR(50));\n",
    69: "CREATE TABLE Employees (employee_id INT PRIMARY KEY, employee_name VARCHAR(50), manager_id INT NULL);\n",
    70: "CREATE TABLE Products (product_id INT PRIMARY KEY, product_name VARCHAR(50), price INT);\n",
}


def build_source_map() -> dict[int, str]:
    text = SOURCE.read_text(encoding='utf-8')
    pattern = re.compile(r'(?ms)^\s*(\d+)\.\s*Problem Statement\s*(.*?)(?=^\s*\d+\.\s*Problem Statement|\Z)')
    items = {}
    for num_str, body in pattern.findall(text):
        qnum = int(num_str)
        section = body.strip().replace('\r', '')
        if not section:
            continue
        items[qnum] = section
    return items


def q_name(qnum: int) -> str:
    title = make_title(qnum)
    return f"Q{qnum:02d}-{title}"


def topic_name_for(qnum: int) -> str:
    for topic, nums in TOPIC_TO_QUESTIONS.items():
        if qnum in nums:
            return topic
    return "99-extra"


def make_title(qnum: int) -> str:
    raw = {
        1: 'financial-discount-and-service',
        2: 'production-summary',
        3: 'even-odd-digit-sum',
        4: 'kg-to-grams',
        5: 'product-inventory-value',
        6: 'even-odd-rearrangement',
        7: 'palindrome-sentence',
        8: 'grade-calculator',
        9: 'cancel-divisible-token-numbers',
        10: 'vector-insert-after-id',
        11: 'linkedlist-remove-first-occurrence',
        12: 'high-unique-registration',
        13: 'treeset-previous-smaller-score',
        14: 'hashmap-product-quantity-total',
        15: 'priorityqueue-first-k-sum',
        16: 'generic-box',
        17: 'withdrawal-validation',
        18: 'custom-exception-score-validation',
        19: 'marks-above-average',
        20: 'top-three-distinct-distances',
        21: 'total-salary-above-threshold',
        22: 'stream-discount-mapping',
        23: 'grouping-by-category',
        24: 'even-square-sum',
        25: 'safe-index-and-division',
        26: 'normalize-to-1nf',
        27: '2nf-patient-summary',
        28: '3nf-student-summary',
        29: '3nf-faculty-allocation-summary',
        30: 'reservation-checkout-date',
        31: 'exam-end-time',
        32: 'adjusted-consumption',
        33: 'package-priority-score',
        34: 'machine-safety-check',
        35: 'optional-employee-lookup',
        36: 'days-between-dates',
        37: 'local-variables-vs-array',
        38: 'method-local-total-marks',
        39: 'garbage-collection-request',
        40: 'final-salary',
        41: 'square-stringbuilder-output',
        42: 'buffered-input-sum',
        43: 'buffered-temperature-report',
        44: 'corrected-total-cost',
        45: 'parking-fee',
        46: 'functional-operation-argument',
        47: 'uppercase-method-reference',
        48: 'function-interface-quantity-rules',
        49: 'thread-join-processing',
        50: 'thread-class-order',
        51: 'runnable-heart-monitor',
        52: 'synchronized-withdrawal',
        53: 'synchronized-ticket-booking',
        54: 'synchronized-visitor-counter',
        55: 'deadlock-prevention',
        56: 'livelock-retry-management',
        57: 'synchronized-submission-counter',
        58: 'concurrent-login-records',
        59: 'students-create-and-list',
        60: 'cse-salary-increment',
        61: 'book-price-deletion',
        62: 'department-student-count',
        63: 'customer-total-spent',
        64: 'subject-average-marks',
        65: 'customers-with-3-or-more-orders',
        66: 'salary-above-average',
        67: 'inner-join-students-departments',
        68: 'left-join-employees-departments',
        69: 'self-join-manager-list',
        70: 'product-highest-price-subquery',
    }
    return raw[qnum]


def build_problem_markdown(qnum: int, source_section: str) -> str:
    title = q_name(qnum)
    cleaned = source_section.strip()
    # Convert the raw extracted content into a readable markdown block.
    # Keep the original wording so it matches the official source bank.
    return f"# {title}\n\n{cleaned}\n"


def build_solution_stub(qnum: int) -> str:
    name = make_title(qnum).replace('-', ' ')

    specific_starters = {
        1: '''\
            import java.util.*;

            public class Solution {
                public static void main(String[] args) {
                    Scanner sc = new Scanner(System.in);
                    double originalAmount = sc.nextDouble();
                    double discountPercent = sc.nextDouble();
                    double servicePercent = sc.nextDouble();
                    double finalAmount = calculateFinalAmount(
                            originalAmount, discountPercent, servicePercent);
                    System.out.printf("%.2f%n", finalAmount);
                }

                static double calculateFinalAmount(double amount, double discountPercent,
                                                   double servicePercent) {
                    // TODO: apply the discount first, then calculate service charge.
                    return 0.0;
                }
            }
        ''',
        2: '''\
            import java.util.*;

            public class Solution {
                public static void main(String[] args) {
                    Scanner sc = new Scanner(System.in);
                    int n = sc.nextInt();
                    int[] production = new int[n];
                    for (int i = 0; i < n; i++) production[i] = sc.nextInt();
                    int total = 0;
                    int minimum = Integer.MAX_VALUE;
                    int maximum = Integer.MIN_VALUE;
                    for (int value : production) {
                        // TODO: update total, minimum, and maximum.
                    }
                    System.out.println(total);
                    System.out.printf("%.2f%n", (double) total / n);
                    System.out.println(maximum - minimum);
                }
            }
        ''',
        3: '''\
            import java.util.*;

            public class Solution {
                public static void main(String[] args) {
                    Scanner sc = new Scanner(System.in);
                    long number = sc.nextLong();
                    int evenSum = 0;
                    int oddSum = 0;
                    while (number > 0) {
                        int digit = (int) (number % 10);
                        // TODO: add the digit to the correct sum.
                        number /= 10;
                    }
                    System.out.println(evenSum);
                    System.out.println(oddSum);
                }
            }
        ''',
        4: '''\
            import java.util.*;

            public class Solution {
                public static void main(String[] args) {
                    Scanner sc = new Scanner(System.in);
                    int n = sc.nextInt();
                    long[] weightsInGrams = new long[n];
                    for (int i = 0; i < n; i++) {
                        long kilograms = sc.nextLong();
                        // TODO: convert kilograms to grams without integer overflow.
                        weightsInGrams[i] = 0;
                    }
                    for (int i = 0; i < n; i++) {
                        if (i > 0) System.out.print(" ");
                        System.out.print(weightsInGrams[i]);
                    }
                    System.out.println();
                }
            }
        ''',
        5: '''\
            import java.util.*;

            public class Solution {
                static class Product {
                    int id;
                    double price;
                    int quantity;

                    double calculateValue() {
                        // TODO: return price multiplied by quantity.
                        return 0.0;
                    }
                }

                public static void main(String[] args) {
                    Scanner sc = new Scanner(System.in);
                    Product product = new Product();
                    product.id = sc.nextInt();
                    product.price = sc.nextDouble();
                    product.quantity = sc.nextInt();
                    System.out.printf("%.2f%n", product.calculateValue());
                }
            }
        ''',
        6: '''\
            import java.util.*;

            public class Solution {
                public static void main(String[] args) {
                    Scanner sc = new Scanner(System.in);
                    int n = sc.nextInt();
                    int[] values = new int[n];
                    for (int i = 0; i < n; i++) values[i] = sc.nextInt();
                    // TODO: rearrange in place while preserving order within each group.
                    for (int value : values) {
                        if (value % 2 == 0) System.out.print(value + " ");
                    }
                    for (int value : values) {
                        if (value % 2 != 0) System.out.print(value + " ");
                    }
                    System.out.println();
                }
            }
        ''',
        7: '''\
            import java.util.*;

            public class Solution {
                public static void main(String[] args) {
                    Scanner sc = new Scanner(System.in);
                    String sentence = sc.nextLine();
                    String normalized = sentence.replace(" ", "").toLowerCase();
                    boolean palindrome = true;
                    for (int left = 0, right = normalized.length() - 1;
                         left < right; left++, right--) {
                        // TODO: compare the characters at left and right.
                    }
                    System.out.println(palindrome ? "Palindrome" : "Not Palindrome");
                }
            }
        ''',
        8: '''\
            import java.util.*;

            public class Solution {
                static char calculateGrade(int marks) {
                    // TODO: implement the A/B/C/D/F ranges from Problem.md.
                    return '?';
                }

                public static void main(String[] args) {
                    Scanner sc = new Scanner(System.in);
                    int n = sc.nextInt();
                    for (int i = 0; i < n; i++) {
                        if (i > 0) System.out.print(" ");
                        System.out.print(calculateGrade(sc.nextInt()));
                    }
                    System.out.println();
                }
            }
        ''',
        9: '''\
            import java.util.*;

            public class Solution {
                public static void main(String[] args) {
                    Scanner sc = new Scanner(System.in);
                    int n = sc.nextInt();
                    ArrayList<Integer> tokens = new ArrayList<>();
                    for (int i = 0; i < n; i++) tokens.add(sc.nextInt());
                    int cancellationNumber = sc.nextInt();
                    tokens.removeIf(token -> token % cancellationNumber == 0);
                    if (tokens.isEmpty()) {
                        System.out.println(-1);
                    } else {
                        for (int i = 0; i < tokens.size(); i++) {
                            if (i > 0) System.out.print(" ");
                            System.out.print(tokens.get(i));
                        }
                        System.out.println();
                    }
                }
            }
        ''',
        10: '''\
            import java.util.*;

            public class Solution {
                public static void main(String[] args) {
                    Scanner sc = new Scanner(System.in);
                    int n = sc.nextInt();
                    Vector<Integer> containers = new Vector<>();
                    for (int i = 0; i < n; i++) containers.add(sc.nextInt());
                    int existingId = sc.nextInt();
                    int newId = sc.nextInt();
                    int index = containers.indexOf(existingId);
                    if (index < 0) {
                        System.out.println("Container Not Found");
                    } else {
                        containers.add(index + 1, newId);
                        for (int i = 0; i < containers.size(); i++) {
                            if (i > 0) System.out.print(" ");
                            System.out.print(containers.get(i));
                        }
                        System.out.println();
                    }
                }
            }
        ''',
    }
    if qnum in specific_starters:
        return textwrap.dedent(specific_starters[qnum])

    if 1 <= qnum <= 25:
        return textwrap.dedent(f'''\
            import java.util.*;

            public class Solution {{
                public static void main(String[] args) {{
                    Scanner sc = new Scanner(System.in);

                    // TODO: read problem-specific input
                    // Example pattern for this question: {name}
                    // Use the exact input format from Problem.md.

                    // --- starter skeleton ---
                    // int n = sc.nextInt();
                    // int[] values = new int[n];
                    // for (int i = 0; i < n; i++) {{
                    //     values[i] = sc.nextInt();
                    // }}
                    //
                    // TODO: implement the required logic and print the answer.

                    System.out.println("TODO: implement solution for {name}");
                }}
            }}
        ''')

    if 26 <= qnum <= 36:
        return textwrap.dedent(f'''\
            import java.util.*;

            public class Solution {{
                public static void main(String[] args) {{
                    Scanner sc = new Scanner(System.in);

                    // TODO: read and normalize the input for: {name}
                    // This category depends on data processing / normalization / Date-Time logic.

                    // Example shape:
                    // int n = sc.nextInt();
                    // sc.nextLine();
                    // for (int i = 0; i < n; i++) {{
                    //     String line = sc.nextLine();
                    //     // parse and process each line
                    // }}

                    System.out.println("TODO: implement solution for {name}");
                }}
            }}
        ''')

    if 37 <= qnum <= 48:
        return textwrap.dedent(f'''\
            import java.util.*;

            public class Solution {{
                public static void main(String[] args) {{
                    Scanner sc = new Scanner(System.in);

                    // TODO: implement the Java memory / stream / lambda / functional interface task:
                    // {name}

                    // Example patterns commonly used in this category:
                    // int n = sc.nextInt();
                    // int[] nums = new int[n];
                    // for (int i = 0; i < n; i++) nums[i] = sc.nextInt();
                    //
                    // for (int x : nums)
                    //     System.out.println(x);

                    System.out.println("TODO: implement solution for {name}");
                }}
            }}
        ''')

    if 49 <= qnum <= 58:
        return textwrap.dedent(f'''\
            import java.util.*;

            public class Solution {{
                public static void main(String[] args) throws Exception {{
                    Scanner sc = new Scanner(System.in);

                    // TODO: implement the thread / concurrency task: {name}
                    // Use the required pattern from Problem.md:
                    // - Thread class
                    // - Runnable
                    // - synchronized block
                    // - join()

                    // Example starter:
                    // int n = sc.nextInt();
                    // System.out.println("Processing: " + n);

                    System.out.println("TODO: implement solution for {name}");
                }}
            }}
        ''')

    return textwrap.dedent(f'''\
        import java.util.*;

        public class Solution {{
            public static void main(String[] args) {{
                Scanner sc = new Scanner(System.in);
                // TODO: complete solution for: {name}
                System.out.println("TODO: implement solution for {name}");
            }}
        }}
    ''')


def build_sql_files(qnum: int):
    if qnum == 59:
        schema = "CREATE TABLE Students (student_id INT PRIMARY KEY, student_name VARCHAR(50) NOT NULL, email VARCHAR(100) UNIQUE, age INT CHECK (age BETWEEN 17 AND 60), course VARCHAR(50));\nINSERT INTO Students VALUES (101, 'Amit', 'amit@gmail.com', 20, 'CSE');\nINSERT INTO Students VALUES (102, 'Neha', 'neha@gmail.com', 21, 'ECE');\nINSERT INTO Students VALUES (103, 'Rahul', 'rahul@gmail.com', 22, 'CSE');\n"
        attempt = "-- Write your SQL query here\nSELECT * FROM Students ORDER BY student_id;\n"
        expected = "101 Amit amit@gmail.com 20 CSE\n102 Neha neha@gmail.com 21 ECE\n103 Rahul rahul@gmail.com 22 CSE\n"
    elif qnum == 60:
        schema = "CREATE TABLE Employees (employee_id INT PRIMARY KEY, employee_name VARCHAR(50), department VARCHAR(50), salary DECIMAL(10,2));\nINSERT INTO Employees VALUES (101, 'Amit', 'CSE', 50000);\nINSERT INTO Employees VALUES (102, 'Neha', 'ECE', 45000);\nINSERT INTO Employees VALUES (103, 'Rahul', 'CSE', 60000);\nINSERT INTO Employees VALUES (104, 'Simran', 'IT', 55000);\n"
        attempt = "-- Write your SQL query here\nUPDATE Employees SET salary = salary * 1.10 WHERE department = 'CSE';\nSELECT employee_name, department, salary FROM Employees ORDER BY employee_id;\n"
        expected = "Amit CSE 55000.00\nNeha ECE 45000.00\nRahul CSE 66000.00\nSimran IT 55000.00\n"
    elif qnum == 61:
        schema = "CREATE TABLE Books (book_id INT PRIMARY KEY, title VARCHAR(50), author VARCHAR(50), price INT);\nINSERT INTO Books VALUES (101, 'Java', 'James', 550);\nINSERT INTO Books VALUES (102, 'SQL', 'Korth', 250);\nINSERT INTO Books VALUES (103, 'Python', 'Rossum', 650);\nINSERT INTO Books VALUES (104, 'Networks', 'Tanenbaum', 300);\nINSERT INTO Books VALUES (105, 'OS', 'Galvin', 200);\n"
        attempt = "-- Write your SQL query here\nDELETE FROM Books WHERE price < 300;\nSELECT * FROM Books ORDER BY book_id;\n"
        expected = "101 Java James 550\n103 Python Rossum 650\n104 Networks Tanenbaum 300\n"
    elif qnum == 62:
        schema = "CREATE TABLE Students (student_id INT PRIMARY KEY, student_name VARCHAR(50), department VARCHAR(50));\nINSERT INTO Students VALUES (101, 'Amit', 'CSE');\nINSERT INTO Students VALUES (102, 'Neha', 'ECE');\nINSERT INTO Students VALUES (103, 'Rahul', 'CSE');\nINSERT INTO Students VALUES (104, 'Simran', 'IT');\nINSERT INTO Students VALUES (105, 'Karan', 'CSE');\nINSERT INTO Students VALUES (106, 'Priya', 'ECE');\n"
        attempt = "-- Count students in each department.\nSELECT department, COUNT(*) AS student_count\nFROM Students\nGROUP BY department\nORDER BY department;\n"
        expected = "CSE 3\nECE 2\nIT 1\n"
    elif qnum == 63:
        schema = "CREATE TABLE Orders (order_id INT PRIMARY KEY, customer_id INT, amount INT);\nINSERT INTO Orders VALUES (1, 101, 100);\nINSERT INTO Orders VALUES (2, 101, 250);\nINSERT INTO Orders VALUES (3, 102, 300);\nINSERT INTO Orders VALUES (4, 103, 50);\n"
        attempt = "-- Calculate each customer's total spending.\nSELECT customer_id, SUM(amount) AS total_spent\nFROM Orders\nGROUP BY customer_id\nORDER BY customer_id;\n"
        expected = "101 350\n102 300\n103 50\n"
    elif qnum == 64:
        schema = "CREATE TABLE Marks (student_id INT, subject VARCHAR(20), marks INT);\nINSERT INTO Marks VALUES (101, 'Java', 80);\nINSERT INTO Marks VALUES (102, 'Java', 70);\nINSERT INTO Marks VALUES (103, 'SQL', 90);\nINSERT INTO Marks VALUES (104, 'SQL', 60);\nINSERT INTO Marks VALUES (105, 'Python', 75);\n"
        attempt = "-- Find the average marks for every subject.\nSELECT subject, AVG(marks) AS average_marks\nFROM Marks\nGROUP BY subject\nORDER BY subject;\n"
        expected = "Java 75.0000\nPython 75.0000\nSQL 75.0000\n"
    elif qnum == 65:
        schema = "CREATE TABLE Orders (order_id INT PRIMARY KEY, customer_id INT, amount INT);\nINSERT INTO Orders VALUES (1, 101, 100);\nINSERT INTO Orders VALUES (2, 101, 250);\nINSERT INTO Orders VALUES (3, 101, 75);\nINSERT INTO Orders VALUES (4, 102, 300);\nINSERT INTO Orders VALUES (5, 102, 50);\nINSERT INTO Orders VALUES (6, 103, 80);\nINSERT INTO Orders VALUES (7, 103, 90);\nINSERT INTO Orders VALUES (8, 103, 120);\n"
        attempt = "-- List customers who placed at least three orders.\nSELECT customer_id, COUNT(*) AS order_count\nFROM Orders\nGROUP BY customer_id\nHAVING COUNT(*) >= 3\nORDER BY customer_id;\n"
        expected = "101 3\n103 3\n"
    elif qnum == 66:
        schema = "CREATE TABLE Employees (employee_id INT PRIMARY KEY, employee_name VARCHAR(50), salary INT);\nINSERT INTO Employees VALUES (101, 'Amit', 50000);\nINSERT INTO Employees VALUES (102, 'Neha', 70000);\nINSERT INTO Employees VALUES (103, 'Rahul', 60000);\nINSERT INTO Employees VALUES (104, 'Simran', 40000);\n"
        attempt = "-- Find employees earning above the average salary.\nSELECT employee_name, salary\nFROM Employees\nWHERE salary > (SELECT AVG(salary) FROM Employees)\nORDER BY salary;\n"
        expected = "Rahul 60000\nNeha 70000\n"
    elif qnum == 67:
        schema = "CREATE TABLE Students (student_id INT PRIMARY KEY, student_name VARCHAR(50), department_id INT);\nCREATE TABLE Departments (department_id INT PRIMARY KEY, department_name VARCHAR(50));\nINSERT INTO Departments VALUES (1, 'CSE');\nINSERT INTO Departments VALUES (2, 'ECE');\nINSERT INTO Students VALUES (101, 'Amit', 1);\nINSERT INTO Students VALUES (102, 'Neha', 2);\nINSERT INTO Students VALUES (103, 'Rahul', 1);\n"
        attempt = "-- Show each student with the department name.\nSELECT s.student_name, d.department_name\nFROM Students s\nINNER JOIN Departments d ON s.department_id = d.department_id\nORDER BY s.student_id;\n"
        expected = "Amit CSE\nNeha ECE\nRahul CSE\n"
    elif qnum == 68:
        schema = "CREATE TABLE Employees (employee_id INT PRIMARY KEY, employee_name VARCHAR(50), department_id INT);\nCREATE TABLE Departments (department_id INT PRIMARY KEY, department_name VARCHAR(50));\nINSERT INTO Departments VALUES (1, 'CSE');\nINSERT INTO Departments VALUES (2, 'ECE');\nINSERT INTO Employees VALUES (101, 'Amit', 1);\nINSERT INTO Employees VALUES (102, 'Neha', 2);\nINSERT INTO Employees VALUES (103, 'Rahul', NULL);\n"
        attempt = "-- Keep employees even when no department is assigned.\nSELECT e.employee_name, d.department_name\nFROM Employees e\nLEFT JOIN Departments d ON e.department_id = d.department_id\nORDER BY e.employee_id;\n"
        expected = "Amit CSE\nNeha ECE\nRahul NULL\n"
    elif qnum == 69:
        schema = "CREATE TABLE Employees (employee_id INT PRIMARY KEY, employee_name VARCHAR(50), manager_id INT NULL);\nINSERT INTO Employees VALUES (101, 'Amit', NULL);\nINSERT INTO Employees VALUES (102, 'Neha', 101);\nINSERT INTO Employees VALUES (103, 'Rahul', 101);\nINSERT INTO Employees VALUES (104, 'Simran', 102);\n"
        attempt = "-- Match each employee to their manager using a self join.\nSELECT e.employee_name, m.employee_name AS manager_name\nFROM Employees e\nINNER JOIN Employees m ON e.manager_id = m.employee_id\nORDER BY e.employee_id;\n"
        expected = "Neha Amit\nRahul Amit\nSimran Neha\n"
    elif qnum == 70:
        schema = "CREATE TABLE Products (product_id INT PRIMARY KEY, product_name VARCHAR(50), price INT);\nINSERT INTO Products VALUES (101, 'Keyboard', 2500);\nINSERT INTO Products VALUES (102, 'Monitor', 12000);\nINSERT INTO Products VALUES (103, 'Mouse', 1500);\nINSERT INTO Products VALUES (104, 'Webcam', 12000);\n"
        attempt = "-- Return every product whose price equals the highest price.\nSELECT product_name, price\nFROM Products\nWHERE price = (SELECT MAX(price) FROM Products)\nORDER BY product_id;\n"
        expected = "Monitor 12000\nWebcam 12000\n"
    else:
        schema = SQL_SCHEMA[qnum]
        attempt = "-- Write your SQL query here\nSELECT 1;\n"
        expected = ""
    return schema, attempt, expected


def generate_question_structure():
    if PLAYGROUND.exists():
        shutil.rmtree(PLAYGROUND)
    PLAYGROUND.mkdir(parents=True, exist_ok=True)
    (PLAYGROUND / '_solutions').mkdir(parents=True, exist_ok=True)

    source_map = build_source_map()
    for topic_dir_name, qnums in TOPIC_TO_QUESTIONS.items():
        topic_dir = PLAYGROUND / topic_dir_name
        topic_dir.mkdir(parents=True, exist_ok=True)
        for qnum in qnums:
            qdir = topic_dir / q_name(qnum)
            qdir.mkdir(parents=True, exist_ok=True)
            source_section = source_map.get(qnum, f"Problem Statement\nNo source text found for question {qnum}.")
            (qdir / 'Problem.md').write_text(build_problem_markdown(qnum, source_section), encoding='utf-8')

            if qnum <= 58:
                (qdir / 'Solution.java').write_text(build_solution_stub(qnum), encoding='utf-8')
                test_dir = qdir / 'testcases'
                test_dir.mkdir(exist_ok=True)
                # give at least one sample pair; this is only scaffolding and not the full practice set
                if qnum in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58}:
                    (test_dir / 'input1.txt').write_text('' if qnum > 58 else '', encoding='utf-8')
                    (test_dir / 'expected1.txt').write_text('', encoding='utf-8')
            else:
                schema, attempt, expected = build_sql_files(qnum)
                (qdir / 'schema.sql').write_text(schema, encoding='utf-8')
                (qdir / 'attempt.sql').write_text(attempt, encoding='utf-8')
                (qdir / 'expected_output.txt').write_text(expected, encoding='utf-8')
                (qdir / 'seed_data.sql').write_text(schema, encoding='utf-8')

            ref_topic = PLAYGROUND / '_solutions' / topic_dir_name
            ref_topic.mkdir(parents=True, exist_ok=True)
            ref_dir = ref_topic / q_name(qnum)
            ref_dir.mkdir(parents=True, exist_ok=True)
            ref_dir.joinpath('Problem.md').write_text(build_problem_markdown(qnum, source_section), encoding='utf-8')
            if qnum <= 58:
                ref_dir.joinpath('Solution.java').write_text(build_solution_stub(qnum), encoding='utf-8')
            else:
                schema, attempt, expected = build_sql_files(qnum)
                ref_dir.joinpath('schema.sql').write_text(schema, encoding='utf-8')
                ref_dir.joinpath('attempt.sql').write_text(attempt, encoding='utf-8')
                ref_dir.joinpath('expected_output.txt').write_text(expected, encoding='utf-8')
                ref_dir.joinpath('seed_data.sql').write_text(schema, encoding='utf-8')

    # Basic README
    readme = PLAYGROUND / 'README.md'
    lines = [
        '# PAUJ Practice Playground',
        '',
        'This workspace contains all 70 PAUJ exam questions extracted from `question_bank_extracted.txt`.',
        '',
        '## What Is Complete',
        '- All 70 folders and prompt statements are present.',
        '- Every Java question (Q01-Q58) has a compilable `Solution.java` starter file.',
        '- Every SQL question (Q59-Q70) has seeded tables, an `attempt.sql` query, and expected output.',
        '- Q01-Q10 have question-specific Java parsing and method scaffolds.',
        '- The remaining Java files provide category-oriented starter templates that you complete.',
        '',
        '## Important: Where Are The Solutions?',
        'The Java files are intentionally practice scaffolds, not completed answer keys. The `TODO` markers are where you write the solution. The `_solutions` directory is a generated reference mirror of the same prompt and starter artifacts; it is not a hidden set of completed Java answers.',
        '',
        'The SQL `attempt.sql` files are already filled with executable practice queries. You can first rewrite them yourself, then compare your query with the generated attempt and `expected_output.txt`.',
        '',
        '## How To Solve A Java Question',
        '1. Open a question folder and read `Problem.md` completely, including input, output, constraints, and sample.',
        '2. Open `Solution.java` and replace the TODO section with your logic.',
        '3. From that question folder, compile and run it:',
        '```powershell',
        'Set-Location .\\01-java-basics-oop\\Q01-financial-discount-and-service',
        'javac Solution.java',
        '"5000`n10.5`n5.0" | java Solution',
        '```',
        '4. Compare your output with the sample in `Problem.md`. Repeat with your own edge cases.',
        '',
        'To compile all Java starters at once from `exam-playground`:',
        '```powershell',
        'python .\\run_tests.py',
        '```',
        'This checks compilation only; it does not prove that your TODO logic is correct.',
        '',
        '## How To Run A SQL Question',
        'Each SQL folder contains:',
        '- `schema.sql`: creates the tables and inserts practice data.',
        '- `attempt.sql`: the query to study or replace with your own answer.',
        '- `expected_output.txt`: expected rows for the generated dataset.',
        '',
        'From `exam-playground`, run a SQL question with the included Python helper:',
        '```powershell',
        'python .\\run_sql.py ".\\12-sql-joins-subqueries-groupby\\Q62-department-student-count"',
        '```',
        'The helper creates an in-memory SQLite database, runs `schema.sql`, executes `attempt.sql`, and prints the result beside the expected output. Python is required; no database installation is needed for these exercises.',
        '',
        'You can also paste `schema.sql` and `attempt.sql` into MySQL Workbench or another SQL client. Run the schema first, then run the attempt query.',
        '',
        '## Folder Structure',
        '- `Problem.md`: source-backed question statement.',
        '- `Solution.java`: Java starter file for Q01-Q58.',
        '- `schema.sql`, `attempt.sql`, `expected_output.txt`: SQL practice files for Q59-Q70.',
        '- `_solutions`: generated mirror used to preserve the same source-backed structure.',
        '',
        '## Topics',
    ]
    for topic_name in TOPIC_TO_QUESTIONS:
        lines.append(f'- {topic_name}: {TOPIC_LABELS[topic_name]}')
    readme.write_text('\n'.join(lines) + '\n', encoding='utf-8')

    # Minimal test runner for Java question stubs
    run_tests_py = PLAYGROUND / 'run_tests.py'
    run_tests_py.write_text(textwrap.dedent('''\
        import subprocess
        import sys
        from pathlib import Path

        root = Path(__file__).resolve().parent
        status = 0
        for topic in sorted(p for p in root.iterdir() if p.is_dir() and not p.name.startswith('.') and p.name != '_solutions'):
            for qdir in sorted(p for p in topic.iterdir() if p.is_dir() and p.name.startswith('Q')):
                sol = qdir / 'Solution.java'
                if sol.exists():
                    r = subprocess.run(['javac', 'Solution.java'], cwd=qdir, capture_output=True, text=True)
                    if r.returncode != 0:
                        print(f'{qdir.name}: compile failed')
                        status = 1
        if status == 0:
            print(f'Validated {sum(1 for p in root.iterdir() if p.is_dir() and p.name != "_solutions") } topics with Java stubs compiling successfully.')
        raise SystemExit(status)
    '''), encoding='utf-8')

    run_sql_py = PLAYGROUND / 'run_sql.py'
    run_sql_py.write_text(textwrap.dedent('''\
        import sqlite3
        import sys
        from pathlib import Path

        if len(sys.argv) != 2:
            raise SystemExit('Usage: python run_sql.py <sql-question-folder>')

        question_dir = Path(sys.argv[1]).resolve()
        schema = question_dir / 'schema.sql'
        attempt = question_dir / 'attempt.sql'
        expected = question_dir / 'expected_output.txt'
        if not schema.exists() or not attempt.exists():
            raise SystemExit('The folder must contain schema.sql and attempt.sql')

        database = sqlite3.connect(':memory:')
        database.executescript(schema.read_text(encoding='utf-8'))
        statements = [part.strip() for part in attempt.read_text(encoding='utf-8').split(';') if part.strip()]
        cursor = database.cursor()
        for statement in statements[:-1]:
            cursor.execute(statement)
        rows = cursor.execute(statements[-1]).fetchall()

        print('Actual output:')
        for row in rows:
            print(' '.join('NULL' if value is None else str(value) for value in row))
        print()
        print('Expected output:')
        print(expected.read_text(encoding='utf-8').strip())
    '''), encoding='utf-8')

    print("Generated full question bank from extracted source text.")


generate_question_structure()
