-- Count students in each department.
SELECT department, COUNT(*) AS student_count
FROM Students
GROUP BY department
ORDER BY department;
