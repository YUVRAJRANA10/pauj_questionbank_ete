# PAUJ Practice Playground

This workspace contains all 70 PAUJ exam questions extracted from `question_bank_extracted.txt`.

## What Is Complete
- All 70 folders and prompt statements are present.
- Every Java question (Q01-Q58) has a compilable `Solution.java` starter file.
- Every Java question (Q01-Q58) now has a completed reference answer in `_solutions`.
- Every SQL question (Q59-Q70) has seeded tables, an `attempt.sql` query, and expected output.
- Q01-Q10 have question-specific Java parsing and method scaffolds.
- Q11-Q58 provide category-oriented starter templates that you complete.

## Important: Where Are The Solutions?
The main question folders are your practice area. The `TODO` markers are where you write your solution. The completed Java answer for a question is in the matching path under `_solutions`, for example:

```text
Your file:
01-java-basics-oop/Q04-kg-to-grams/Solution.java

Reference answer:
_solutions/01-java-basics-oop/Q04-kg-to-grams/Solution.java
```

Do not copy the reference answer before attempting the question. Use it only to compare your approach after trying the sample and edge cases.

The SQL `attempt.sql` files are already filled with executable practice queries. You can first rewrite them yourself, then compare your query with the generated attempt and `expected_output.txt`.

## How To Solve A Java Question
1. Open a question folder and read `Problem.md` completely, including input, output, constraints, and sample.
2. Open `Solution.java` and replace the TODO section with your logic.
3. From that question folder, compile and run it:
```powershell
Set-Location .\01-java-basics-oop\Q01-financial-discount-and-service
javac Solution.java
"5000`n10.5`n5.0" | java Solution
```
4. Compare your output with the sample in `Problem.md`. Repeat with your own edge cases.

To compile all Java starters at once from `exam-playground`:
```powershell
python .\run_tests.py
```
This checks compilation only; it does not prove that your TODO logic is correct.

To run every completed reference answer against its sample testcase:
```powershell
python .\run_reference_tests.py
```
The command reports the total, passed, and failed count. Four source prompts currently have inconsistent sample outputs: Q01, Q03, Q09, and Q44. Their reference answers follow the written formula/rules, so those four may be reported as failed against the printed sample output.

## How To Run A SQL Question
Each SQL folder contains:
- `schema.sql`: creates the tables and inserts practice data.
- `attempt.sql`: the query to study or replace with your own answer.
- `expected_output.txt`: expected rows for the generated dataset.

From `exam-playground`, run a SQL question with the included Python helper:
```powershell
python .\run_sql.py ".\12-sql-joins-subqueries-groupby\Q62-department-student-count"
```
The helper creates an in-memory SQLite database, runs `schema.sql`, executes `attempt.sql`, and prints the result beside the expected output. Python is required; no database installation is needed for these exercises.

You can also paste `schema.sql` and `attempt.sql` into MySQL Workbench or another SQL client. Run the schema first, then run the attempt query.

## Folder Structure
- `Problem.md`: source-backed question statement.
- `Solution.java`: Java starter file for Q01-Q58.
- `schema.sql`, `attempt.sql`, `expected_output.txt`: SQL practice files for Q59-Q70.
- `_solutions`: generated mirror used to preserve the same source-backed structure.

## Topics
- 01-java-basics-oop: Java basics and OOP
- 02-arrays-strings: Arrays and strings
- 03-collections-stl: Collections and STL
- 04-exceptions-filehandling: Exceptions and file handling
- 05-streams: Streams
- 06-lambdas-functional-interfaces: Lambdas and functional interfaces
- 07-jvm-memory-io: JVM, memory, and I/O
- 08-datetime-api: Date-Time API
- 09-multithreading-concurrency: Multithreading and concurrency
- 10-normalization-java-logic: Normalization and Java logic
- 11-sql-ddl-dml-constraints: SQL DDL, DML, and constraints
- 12-sql-joins-subqueries-groupby: SQL joins, subqueries, and grouping
