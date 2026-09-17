-- Match each employee to their manager using a self join.
SELECT e.employee_name, m.employee_name AS manager_name
FROM Employees e
INNER JOIN Employees m ON e.manager_id = m.employee_id
ORDER BY e.employee_id;
