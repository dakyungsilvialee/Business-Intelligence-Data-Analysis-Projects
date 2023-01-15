#2. Assuming you are owner of the business (my_guitar_shop) and are interested in sending a loyalty promotion email to customers. 
#Answer the following questions using my_guitar_shop database provided on canvas: 


#2.1. [2 points] Write an SQL statement that uses my_guitar_shop database 
USE my_guitar_shop;
#(provided for mySQL) and selects customer name, email, number of products purchased, total purchase amount, and average discount_amount. 
#[hint: you will need customer table, orders table, and order_items table] 
SELECT CONCAT(c.first_name, ' ', c.last_name) AS customer_name, c.email_address, COUNT(oi.quantity), SUM(oi.item_price * oi.quantity - oi.discount_amount) AS total_purchase_amount, AVG(oi.discount_amount)
FROM customers AS c, order_items AS oi
GROUP BY customer_name;


#2.2. [2 points] Write an SQL statement that selects product_id, category_id, product_name, product_brand, 
#total revenue (price - (discount * quantity), and total discount amount. 
SELECT p.product_id, p.category_id, 
SUBSTRING_INDEX(p.product_name, ' ', 1 ) AS product_brand, 
SUM(oi.discount_amount) AS total_discount_amount,
SUM(oi.item_price - oi.quantity * oi.discount_amount) AS total_revenue
FROM products AS p, order_items AS oi
GROUP BY p.product_id, p.category_id;




