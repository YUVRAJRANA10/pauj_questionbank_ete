-- Calculate each customer's total spending.
SELECT customer_id, SUM(amount) AS total_spent
FROM Orders
GROUP BY customer_id
ORDER BY customer_id;
