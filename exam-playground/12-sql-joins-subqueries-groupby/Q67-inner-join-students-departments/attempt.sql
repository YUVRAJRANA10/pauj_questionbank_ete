-- Show each student with the department name.
SELECT s.student_name, d.department_name
FROM Students s
INNER JOIN Departments d ON s.department_id = d.department_id
ORDER BY s.student_id;
