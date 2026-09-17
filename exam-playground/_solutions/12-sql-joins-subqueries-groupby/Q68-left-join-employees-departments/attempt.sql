-- Keep employees even when no department is assigned.
SELECT e.employee_name, d.department_name
FROM Employees e
LEFT JOIN Departments d ON e.department_id = d.department_id
ORDER BY e.employee_id;
