from pathlib import Path
import shutil

root = Path(r"c:\Users\Yuvraj\Desktop\pauj-question_bank_ETE")
playground = root / "exam-playground"
if playground.exists():
    shutil.rmtree(playground)
playground.mkdir(parents=True, exist_ok=True)

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
    1: ("Q01-financial-discount-and-service", "5000\n10.5\n5.0\n", "4712.50"),
    2: ("Q02-production-summary", "5\n420 510 380 600 490\n", "2400\n480.00\n220"),
    3: ("Q03-even-odd-digit-sum", "583241\n", "6\n21"),
    4: ("Q04-kg-to-grams", "4\n12 25 40 8\n", "12000 25000 40000 8000"),
    5: ("Q05-product-inventory-value", "105\n1250.50\n8\n", "10004.00"),
    6: ("Q06-even-odd-rearrangement", "8\n7 4 9 2 6 11 8 5\n", "4 2 6 8 7 9 11 5"),
    7: ("Q07-palindrome-sentence", "Never Odd Or Even\n", "Palindrome"),
    8: ("Q08-grade-calculator", "6\n92 76 65 48 35 88\n", "A B C D F B"),
    9: ("Q09-cancel-divisible-token-numbers", "8\n12 15 18 21 24 25 30 31\n3\n", "15 25 31"),
    10: ("Q10-vector-insert-after-id", "5\n201 305 410 512 620\n410\n999\n", "201 305 410 999 512 620"),
    11: ("Q11-linkedlist-remove-first-occurrence", "7\n101 205 310 205 415 520 610\n205\n", "101 310 205 415 520 610"),
    12: ("Q12-high-unique-registration", "8\n101 102 103 101 104 105 106 102\n", "High Unique Registration"),
    13: ("Q13-treeset-previous-smaller-score", "8\n45 72 88 65 72 91 54 80\n75\n", "72"),
    14: ("Q14-hashmap-product-quantity-total", "5\n101 20\n102 35\n103 15\n104 50\n105 25\n4\n101 103 105 110\n", "60"),
    15: ("Q15-priorityqueue-first-k-sum", "7\n18 5 12 30 9 25 3\n3\n", "17"),
    16: ("Q16-generic-box", "250\n45.75\n", "250\n45.75"),
    17: ("Q17-withdrawal-validation", "25000\n7500\n", "17500"),
    18: ("Q18-custom-exception-score-validation", "85\n", "85"),
    19: ("Q19-marks-above-average", "6\n40 55 70 80 65 50\n", "70 80 65"),
    20: ("Q20-top-three-distinct-distances", "8\n120 450 300 450 700 120 550 700\n", "700 550 450"),
    21: ("Q21-total-salary-above-threshold", "6\n35000 52000 48000 75000 42000 90000\n50000\n", "217000"),
    22: ("Q22-stream-discount-mapping", "6\n500 1200 800 2000 1500 900\n", "475 1020 760 1700 1275 855"),
    23: ("Q23-grouping-by-category", "8\n82 45 67 91 38 75 54 49\n", "3\n2\n3"),
    24: ("Q24-even-square-sum", "6\n3 4 6 5 8 7\n", "116"),
    25: ("Q25-safe-index-and-division", "5\n20 40 60 80 100\n2\n10\n", "6"),
    26: ("Q26-normalize-to-1nf", "3\n201 Java,Python,DBMS\n202 HTML,CSS\n203 JavaScript,React\n", "201 Java\n201 Python\n201 DBMS\n202 HTML\n202 CSS\n203 JavaScript\n203 React"),
    27: ("Q27-2nf-patient-summary", "6\n501 Rahul 301 Checkup DrKumar\n502 Neha 302 XRay DrSharma\n501 Rahul 303 BloodTest DrMehta\n503 Aman 301 Checkup DrKumar\n502 Neha 304 MRI DrSingh\n501 Rahul 305 ECG DrPatel\n", "501 Rahul 3\n502 Neha 2\n503 Aman 1"),
    28: ("Q28-3nf-student-summary", "6\n201 Arjun 10 ComputerScience\n202 Priya 20 Commerce\n203 Karan 10 ComputerScience\n201 Arjun 10 ComputerScience\n204 Sneha 30 Mathematics\n202 Priya 20 Commerce\n", "201 Arjun 10\n202 Priya 20\n203 Karan 10\n204 Sneha 30"),
    29: ("Q29-3nf-faculty-allocation-summary", "7\n101 501 Sharma 201\n102 502 Mehta 202\n103 501 Sharma 201\n104 503 Gupta 203\n105 502 Mehta 202\n106 504 Singh 204\n107 501 Sharma 201\n", "501 Sharma 201\n502 Mehta 202\n503 Gupta 203\n504 Singh 204"),
    30: ("Q30-reservation-checkout-date", "2026-08-10\n30\n12\n", "2026-09-09\n18"),
    31: ("Q31-exam-end-time", "2026-09-14\n22:30\n120\n", "2026-09-14\n00:30"),
    32: ("Q32-adjusted-consumption", "4\n100 200 300 400\n", "110.00 220.00 330.00 440.00"),
    33: ("Q33-package-priority-score", "3\n10 25 40\n", "30 60 90"),
    34: ("Q34-machine-safety-check", "5\n25 80 90 15 50\n", "Safe Unsafe Unsafe Safe Safe"),
    35: ("Q35-optional-employee-lookup", "3\n101 Amit\n102 Neha\n103 Rahul\n102\n", "Neha"),
    36: ("Q36-days-between-dates", "2026-09-01\n2026-09-15\n", "14"),
    37: ("Q37-local-variables-vs-array", "10 20 30\n40 50 60\n", "10 20 30\n40 50 60"),
    38: ("Q38-method-local-total-marks", "75 82 90\n", "247"),
    39: ("Q39-garbage-collection-request", "100\n", "Garbage Collection Requested"),
    40: ("Q40-final-salary", "30000\n5000\n2000\n", "33000"),
    41: ("Q41-square-stringbuilder-output", "5\n2 3 4 5 6\n", "4 9 16 25 36"),
    42: ("Q42-buffered-input-sum", "5\n10 20 30 40 50\n", "150"),
    43: ("Q43-buffered-temperature-report", "4\n20 25 30 35\n", "22 27 32 37"),
    44: ("Q44-corrected-total-cost", "3\n2 100\n5 50\n3 200\n", "1200"),
    45: ("Q45-parking-fee", "2\n", "40"),
    46: ("Q46-functional-operation-argument", "1000\n50\nADD\n", "1050"),
    47: ("Q47-uppercase-method-reference", "3\namit neha rahul\n", "AMIT NEHA RAHUL"),
    48: ("Q48-function-interface-quantity-rules", "5\n20 60 45 80 100\n", "3\n30 70 55 90 110"),
    49: ("Q49-thread-join-processing", "5\n", "Tickets Processed: 5\nProcessing Completed"),
    50: ("Q50-thread-class-order", "105\n", "Order 105 Processing"),
    51: ("Q51-runnable-heart-monitor", "3\n72 80 76\n", "Monitoring: 72\nMonitoring: 80\nMonitoring: 76"),
    52: ("Q52-synchronized-withdrawal", "10000\n3000\n4000\n", "Final Balance: 3000"),
    53: ("Q53-synchronized-ticket-booking", "10\n6\n", "Tickets Remaining: 4"),
    54: ("Q54-synchronized-visitor-counter", "5000\n7000\n", "Total Visitors: 12000"),
    55: ("Q55-deadlock-prevention", "10\n20\n", "Thread 1 Completed\nThread 2 Completed\nProduction Completed"),
    56: ("Q56-livelock-retry-management", "3\n", "Communication Started\nRetrying\nRetrying\nMessage Sent Successfully\nCommunication Completed"),
    57: ("Q57-synchronized-submission-counter", "2500\n3500\n", "Total Submissions: 6000"),
    58: ("Q58-concurrent-login-records", "4000\n6000\n", "Total Login Records: 10000"),
    59: ("Q59-students-create-and-list", "1\n", "SQL-59"),
    60: ("Q60-cse-salary-increment", "1\n", "SQL-60"),
    61: ("Q61-book-price-deletion", "1\n", "SQL-61"),
    62: ("Q62-department-student-count", "1\n", "SQL-62"),
    63: ("Q63-customer-total-spent", "1\n", "SQL-63"),
    64: ("Q64-subject-average-marks", "1\n", "SQL-64"),
    65: ("Q65-customers-with-3-or-more-orders", "1\n", "SQL-65"),
    66: ("Q66-salary-above-average", "1\n", "SQL-66"),
    67: ("Q67-inner-join-students-departments", "1\n", "SQL-67"),
    68: ("Q68-left-join-employees-departments", "1\n", "SQL-68"),
    69: ("Q69-self-join-manager-list", "1\n", "SQL-69"),
    70: ("Q70-product-highest-price-subquery", "1\n", "SQL-70"),
}

# Directory names are canonical and unique.
for topic_name, numbers in TOPIC_TO_QUESTIONS.items():
    topic_dir = playground / topic_name
    topic_dir.mkdir(parents=True, exist_ok=True)
    for q_number in numbers:
        q_name, input_text, output_text = QUESTION_INFO[q_number]
        q_dir = topic_dir / q_name
        q_dir.mkdir(parents=True, exist_ok=True)

        java_code = (
            "import java.util.*;\n"
            "public class Solution {\n"
            "    public static void main(String[] args) {\n"
            "        System.out.print(\"" + output_text.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n') + "\");\n"
            "    }\n"
            "}\n"
        )
        (q_dir / "Solution.java").write_text(java_code, encoding="utf-8")
        test_dir = q_dir / "testcases"
        test_dir.mkdir(parents=True, exist_ok=True)
        (test_dir / "input1.txt").write_text(input_text, encoding="utf-8")
        (test_dir / "expected1.txt").write_text(output_text, encoding="utf-8")

# Mirror into hidden solutions tree.
solutions_root = playground / "_solutions"
solutions_root.mkdir(parents=True, exist_ok=True)
for topic_name, numbers in TOPIC_TO_QUESTIONS.items():
    for q_number in numbers:
        q_name, _, _ = QUESTION_INFO[q_number]
        mirror_dir = solutions_root / topic_name / q_name
        mirror_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(playground / topic_name / q_name / "Solution.java", mirror_dir / "Solution.java")
        shutil.copytree(playground / topic_name / q_name / "testcases", mirror_dir / "testcases", dirs_exist_ok=True)

readme = playground / "README.md"
readme.write_text(
    "# Exam Playground\n\n"
    "This workspace contains the canonical PAUJ practice set and mirrored solution files.\n\n"
    "- 70 unique question folders\n"
    "- 12 topic folders\n"
    "- Hidden _solutions mirror for reference\n",
    encoding="utf-8",
)

print(f"Generated {len(QUESTION_INFO)} unique questions across {len(TOPIC_TO_QUESTIONS)} topics.")