SELECT * FROM users
SELECT * FROM products
SELECT * FROM reviews
-- List the users who registered in 2018 with a .com email address and living in China
SELECT username,email,date_of_registration FROM users
WHERE to_char(date_of_registration,'yyyy-mm-dd') like '2018%' AND email like '%.com' AND country='China'
-- How many users are there?
SELECT SUM(id) AS Total_users from users
-- How many users registered in 2019?
SELECT SUM(id) AS registration_in_2019 FROM users WHERE to_char(date_of_registration,'yyyy-mm-dd') like '2019%'
-- How many users registered in January?
SELECT SUM(id) AS registration_in_January FROM users WHERE to_char(date_of_registration,'yyyy-mm-dd') like '_____01___'
-- Which country has the most users?
SELECT COUNT(ID) as user_num, country FROM users group by country order by user_num DESC LIMIT 1;
-- What is the gender ratio?
SELECT COUNT(gender='Female' or null)*1.0 / COUNT(gender='Male' or null) AS gender_ratio FROM users
-- How many users left at least one field blank?
SELECT COUNT(*) AS have_null_field_users FROM users WHERE username is null or email is null or date_of_registration is null
or first_name is null or last_name is null or country is null or gender is null
-- Which are the 3 most expensive products?
SELECT name,price FROM products ORDER BY price DESC LIMIT 3
-- Which are the 4th and 5th cheapest products?
SELECT name,price FROM products ORDER BY price OFFSET 3 LIMIT 2
-- What is the average price for an electric product?
SELECT category,AVG(price) AS average_price FROM products WHERE category='Electronics' GROUP BY category 
-- How much would it cost me to buy all the toys?
SELECT SUM(price) AS total_cost FROM products WHERE category='Toys' GROUP BY category
-- What is the average rating?
SELECT AVG(rating) FROM reviews
-- Which product has the best average rating?
SELECT name,rating FROM products JOIN reviews ON products.id = reviews.product_id ORDER BY rating DESC LIMIT 1
-- Which product has the worst rating?
SELECT name,rating FROM products JOIN reviews ON products.id = reviews.product_id ORDER BY rating ASC LIMIT 1
-- Which products have no review?
SELECT products.name FROM products LEFT JOIN reviews ON products.id = reviews.product_id WHERE reviews.product_id is null
SELECT name FROM products WHERE products.id not in (SELECT product_id FROM reviews)
-- How many reviews are 3 or below without comment?
SELECT COUNT(*) FROM reviews WHERE rating <= 3 AND comment is null
-- Which user reviewed the most?
SELECT username,rating FROM users JOIN reviews ON users.id = reviews.user_id ORDER BY rating DESC LIMIT 1
-- List the average rating for each product
SELECT name,AVG(rating) FROM products JOIN reviews ON products.id = reviews.product_id GROUP BY products.name
-- How many days passed since the last review?
select (current_date - date) AS pass_days FROM reviews ORDER BY pass_days LIMIT 1




