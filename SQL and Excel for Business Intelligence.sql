use `coffee-shop`;
## Inventory management and product pricing
# Identify products that should be discontinued and products that should be purchased more. 
SELECT DISTINCT product_id, product_category, product, profitability, retail_price 
FROM( 
SELECT p.product, (sr.quantity * (sr.unit_price - p.current_wholesale_price)) AS profitability, CAST(REPLACE(p.current_retail_price, '$', '') AS DECIMAL(5,2)) AS retail_price, p.product_id, p.product_category  
FROM sales_targets AS st, sales_receipts AS sr  
INNER JOIN product AS p ON p.product_id = sr.product_id  
INNER JOIN sales_outlet AS so ON so.sales_outlet_id = sr.sales_outlet_id) 
AS A 
WHERE profitability > retail_price 
ORDER BY profitability DESC 
LIMIT 10;  

SELECT DISTINCT product_id, product_category, product, profitability, retail_price 
FROM( 
SELECT p.product, (sr.quantity * (sr.unit_price - p.current_wholesale_price)) AS profitability, CAST(REPLACE(p.current_retail_price, '$', '') AS DECIMAL(5,2)) AS retail_price, p.product_id, p.product_category  
FROM sales_targets AS st, sales_receipts AS sr  
INNER JOIN product AS p ON p.product_id = sr.product_id  
INNER JOIN sales_outlet AS so ON so.sales_outlet_id = sr.sales_outlet_id) 
AS A 
WHERE profitability < retail_price 
ORDER BY profitability 
LIMIT 10; 

# Identify pastry products that have high waste. To move these products faster, identify promotional pricing to minimize losses. 
SELECT p.product_id, p.product, pi.waste, CAST(REPLACE(p.current_retail_price, '$', '') AS DECIMAL(5,2)) AS retail_price,
pi.`% waste`, p.current_wholesale_price, (p.current_wholesale_price * 1.2) AS new_price
FROM sales_receipts AS sr
INNER JOIN product AS p ON p.product_id = sr.product_id
INNER JOIN pastry_inventory AS pi ON p.product_id = pi.product_id
GROUP BY p.product_id
ORDER BY pi.`% waste` DESC;

# Identify top 5 products, for each store, that are most frequently purchased in higher quantities (>1).
SELECT * FROM 
(SELECT p.product, CAST(s.sales_outlet_id AS CHAR) AS outlet_id, SUM(s.quantity) AS total_quantity 
FROM product AS p 
INNER JOIN sales_receipts s ON p.product_id = s.product_id 
WHERE CAST(s.sales_outlet_id AS CHAR) = '3' AND s.quantity > 1 
GROUP BY p.product 
HAVING SUM(s.quantity) > 1 
ORDER BY SUM(s.quantity) DESC 
LIMIT 5) AS A  
UNION 
SELECT * FROM 
(SELECT p.product, CAST(s.sales_outlet_id AS CHAR) AS outlet_id, SUM(s.quantity) AS total_quantity 
FROM product AS p 
INNER JOIN sales_receipts s ON p.product_id = s.product_id 
WHERE CAST(s.sales_outlet_id AS CHAR) = '5' AND s.quantity > 1 
GROUP BY p.product 
HAVING SUM(s.quantity) > 1 
ORDER BY SUM(s.quantity) DESC 
LIMIT 5) AS B 
UNION  
SELECT * FROM 
(SELECT p.product, CAST(s.sales_outlet_id AS CHAR) AS outlet_id, SUM(s.quantity) AS total_quantity 
FROM product AS p 
INNER JOIN sales_receipts s ON p.product_id = s.product_id 
WHERE CAST(s.sales_outlet_id AS CHAR) = '8' AND s.quantity > 1 
GROUP BY p.product 
HAVING SUM(s.quantity) > 1 
ORDER BY SUM(s.quantity) DESC 
LIMIT 5) AS C; 

# Identify top 1 product in each category that is most frequently purchased in higher quantities > 1.
SELECT product, product_category, sum_quantity
FROM 
(SELECT p.product, p.product_category, SUM(sr.quantity) AS sum_quantity
FROM product AS p
INNER JOIN sales_receipts AS sr ON p.product_id = sr.product_id
WHERE sr.quantity > 1
GROUP BY p.product
ORDER BY SUM(sr.quantity) DESC) AS t
GROUP BY product_category
HAVING MAX(sum_quantity);

## Customer Segmentation
# Identify top 10 most loyal customers by total sales and top 10 by total sales/week
SELECT c.customer_id, c.`customer_first-name`, SUM(sr.quantity * sr.unit_price) AS sales 
FROM customer AS c 
INNER JOIN sales_receipts AS sr ON c.customer_id = sr.customer_id 
GROUP BY c.customer_id 
ORDER BY sales DESC 
LIMIT 10; 

SELECT c.customer_id, c.`customer_first-name`, WEEK(CONVERT(transaction_date, DATE)) AS sales_week, SUM(sr.quantity * sr.unit_price) AS sales_per_week 
FROM customer AS c  
INNER JOIN sales_receipts AS sr ON c.customer_id = sr.customer_id  
WHERE WEEK(CONVERT(transaction_date, DATE)) = 13
GROUP BY c.customer_id, sales_week 
ORDER BY sales_per_week DESC 
LIMIT 10; 

SELECT c.customer_id, c.`customer_first-name`, WEEK(CONVERT(transaction_date, DATE)) AS sales_week, SUM(sr.quantity * sr.unit_price) AS sales_per_week 
FROM customer AS c  
INNER JOIN sales_receipts AS sr ON c.customer_id = sr.customer_id  
WHERE WEEK(CONVERT(transaction_date, DATE)) = 14
GROUP BY c.customer_id, sales_week 
ORDER BY sales_per_week DESC 
LIMIT 10; 
SELECT c.customer_id, c.`customer_first-name`, WEEK(CONVERT(transaction_date, DATE)) AS sales_week, SUM(sr.quantity * sr.unit_price) AS sales_per_week 
FROM customer AS c  
INNER JOIN sales_receipts AS sr ON c.customer_id = sr.customer_id  
WHERE WEEK(CONVERT(transaction_date, DATE)) = 15
GROUP BY c.customer_id, sales_week 
ORDER BY sales_per_week DESC 
LIMIT 10; 
SELECT c.customer_id, c.`customer_first-name`, WEEK(CONVERT(transaction_date, DATE)) AS sales_week, SUM(sr.quantity * sr.unit_price) AS sales_per_week 
FROM customer AS c  
INNER JOIN sales_receipts AS sr ON c.customer_id = sr.customer_id  
WHERE WEEK(CONVERT(transaction_date, DATE)) = 16
GROUP BY c.customer_id, sales_week 
ORDER BY sales_per_week DESC 
LIMIT 10; 
SELECT c.customer_id, c.`customer_first-name`, WEEK(CONVERT(transaction_date, DATE)) AS sales_week, SUM(sr.quantity * sr.unit_price) AS sales_per_week 
FROM customer AS c  
INNER JOIN sales_receipts AS sr ON c.customer_id = sr.customer_id  
WHERE WEEK(CONVERT(transaction_date, DATE)) = 17
GROUP BY c.customer_id, sales_week 
ORDER BY sales_per_week DESC 
LIMIT 10; 

# Identify top 5 customers by total sales in each age bracket (pick five age brackets)
SELECT c.`customer_first-name`, c.birth_year, SUM(sr.quantity*sr.unit_price) AS sales
FROM customer AS c
INNER JOIN sales_receipts AS sr ON c.customer_id = sr.customer_id
GROUP BY c.`customer_first-name`
HAVING c.birth_year BETWEEN 1950 AND 1959
ORDER BY sales DESC
LIMIT 5;

SELECT c.`customer_first-name`, c.birth_year, SUM(sr.quantity*sr.unit_price) AS sales
FROM customer AS c
INNER JOIN sales_receipts AS sr ON c.customer_id = sr.customer_id
GROUP BY c.`customer_first-name`
HAVING c.birth_year BETWEEN 1960 AND 1969
ORDER BY sales DESC
LIMIT 5;

SELECT c.`customer_first-name`, c.birth_year, SUM(sr.quantity*sr.unit_price) AS sales
FROM customer AS c
INNER JOIN sales_receipts AS sr ON c.customer_id = sr.customer_id
GROUP BY c.`customer_first-name`
HAVING c.birth_year BETWEEN 1970 AND 1979
ORDER BY sales DESC
LIMIT 5;

SELECT c.`customer_first-name`, c.birth_year, SUM(sr.quantity*sr.unit_price) AS sales
FROM customer AS c
INNER JOIN sales_receipts AS sr ON c.customer_id = sr.customer_id
GROUP BY c.`customer_first-name`
HAVING c.birth_year BETWEEN 1980 AND 1989
ORDER BY sales DESC
LIMIT 5;

SELECT c.`customer_first-name`, c.birth_year, SUM(sr.quantity*sr.unit_price) AS sales
FROM customer AS c
INNER JOIN sales_receipts AS sr ON c.customer_id = sr.customer_id
GROUP BY c.`customer_first-name`
HAVING c.birth_year BETWEEN 1990 AND 2001
ORDER BY sales DESC
LIMIT 5;

# Identify top 5 customers by total sales in each gender
SELECT `customer_first-name`, customer_id, gender, sales 
FROM 
(SELECT c.`customer_first-name`, c.customer_id, c.gender, SUM(sr.quantity*sr.unit_price) AS sales 
FROM sales_receipts as sr 
INNER JOIN customer c ON sr.customer_id = c.customer_id 
GROUP BY c.customer_id 
ORDER BY sales DESC) AS t 
WHERE gender = "F" 
LIMIT 5; 

SELECT `customer_first-name`, customer_id, gender, sales 
FROM 
(SELECT c.`customer_first-name`, c.customer_id, c.gender, SUM(sr.quantity*sr.unit_price) AS sales 
FROM sales_receipts as sr 
INNER JOIN customer c ON sr.customer_id = c.customer_id 
GROUP BY c.customer_id 
ORDER BY sales DESC) AS t 
WHERE gender = "M" 
LIMIT 5; 

SELECT `customer_first-name`, customer_id, gender, sales 
FROM 
(SELECT c.`customer_first-name`, c.customer_id, c.gender, SUM(sr.quantity*sr.unit_price) AS sales 
FROM sales_receipts as sr 
INNER JOIN customer c ON sr.customer_id = c.customer_id 
GROUP BY c.customer_id 
ORDER BY sales DESC) AS t 
WHERE gender = "N" 
LIMIT 5; 

# Identify revenue by location and by product type
SELECT so.store_address, p.product_type, SUM(sr.`order` * sr.unit_price) AS revenue
FROM sales_outlet AS so
INNER JOIN sales_receipts sr ON sr.sales_outlet_id = so.sales_outlet_id
INNER JOIN product p ON p.product_id = sr.product_id
GROUP BY so.store_address, p.product_type
ORDER BY revenue DESC;

# Identify employee of the week for each week
SELECT WEEK(CONVERT(sr.transaction_date, DATE)) AS sales_week, sr.staff_id, s.`position`, s.start_date, SUM(sr.line_item_amount) AS sales 
FROM sales_receipts AS sr 
INNER JOIN staff s ON s.staff_id = sr.staff_id 
WHERE WEEK(CONVERT(transaction_date, DATE)) = 13 
GROUP BY sales_week, staff_id 
ORDER BY sales_week ASC, sales DESC; 

SELECT WEEK(CONVERT(sr.transaction_date, DATE)) AS sales_week, sr.staff_id, s.`position`, s.start_date, SUM(sr.line_item_amount) AS sales 
FROM sales_receipts AS sr 
INNER JOIN staff s ON s.staff_id = sr.staff_id 
WHERE WEEK(CONVERT(transaction_date, DATE)) = 14
GROUP BY sales_week, staff_id 
ORDER BY sales_week ASC, sales DESC; 

SELECT WEEK(CONVERT(sr.transaction_date, DATE)) AS sales_week, sr.staff_id, s.`position`, s.start_date, SUM(sr.line_item_amount) AS sales 
FROM sales_receipts AS sr 
INNER JOIN staff s ON s.staff_id = sr.staff_id 
WHERE WEEK(CONVERT(transaction_date, DATE)) = 15
GROUP BY sales_week, staff_id 
ORDER BY sales_week ASC, sales DESC; 

SELECT WEEK(CONVERT(sr.transaction_date, DATE)) AS sales_week, sr.staff_id, s.`position`, s.start_date, SUM(sr.line_item_amount) AS sales 
FROM sales_receipts AS sr 
INNER JOIN staff s ON s.staff_id = sr.staff_id 
WHERE WEEK(CONVERT(transaction_date, DATE)) = 16 
GROUP BY sales_week, staff_id 
ORDER BY sales_week ASC, sales DESC; 

SELECT WEEK(CONVERT(sr.transaction_date, DATE)) AS sales_week, sr.staff_id, s.`position`, s.start_date, SUM(sr.line_item_amount) AS sales 
FROM sales_receipts AS sr 
INNER JOIN staff s ON s.staff_id = sr.staff_id 
WHERE WEEK(CONVERT(transaction_date, DATE)) = 17
GROUP BY sales_week, staff_id 
ORDER BY sales_week ASC, sales DESC; 