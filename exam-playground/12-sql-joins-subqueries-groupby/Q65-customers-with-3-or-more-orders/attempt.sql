-- List customers who placed at least three orders.
SELECT customer_id, COUNT(*) AS order_count
FROM Orders
GROUP BY customer_id
HAVING COUNT(*) >= 3
ORDER BY customer_id;
