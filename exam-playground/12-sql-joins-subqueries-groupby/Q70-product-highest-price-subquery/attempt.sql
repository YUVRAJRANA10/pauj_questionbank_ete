-- Return every product whose price equals the highest price.
SELECT product_name, price
FROM Products
WHERE price = (SELECT MAX(price) FROM Products)
ORDER BY product_id;
