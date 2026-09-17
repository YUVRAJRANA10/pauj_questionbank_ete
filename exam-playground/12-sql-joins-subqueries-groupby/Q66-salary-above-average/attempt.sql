-- Find employees earning above the average salary.
SELECT employee_name, salary
FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees)
ORDER BY salary;
