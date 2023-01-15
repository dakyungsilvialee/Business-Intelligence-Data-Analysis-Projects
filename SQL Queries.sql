USE sakila;

#Part 1
#1.What are the names of all the languages in the database (sorted alphabetically)?
SELECT name  
FROM language
ORDER BY name ASC;


#2.Return the full names (first and last) of actors with “SON” in their last name, ordered by their first name.
SELECT first_name, last_name
FROM actor
WHERE last_name LIKE '%SON%' 
ORDER BY first_name;


#3.Find all the addresses where the second address is not NULL, and return these sorted by addresses.
SELECT address
FROM address
WHERE address2 IS NOT NULL
ORDER BY address2 ASC; 



#4.How many film title contain “cat” or “dog”?
SELECT COUNT(title)
FROM film
WHERE title LIKE '%cat%' OR '%dog%';



#5.Return the first and last names of actors who played in a film containing “cat” or “dog”, along with the release year of the movie, sorted by the actors’ last names.
SELECT a.first_name, a.last_name, f.title, f.release_year
FROM actor AS a
INNER JOIN film AS f 
WHERE title LIKE '%cat%' OR '%dog%'
ORDER BY a.last_name ASC;



#6.Find all the film category names in which there are between 55 and 65 films. 
#Return the names of these categories and the number of films per category, sorted by the number of films.

#option 1
SELECT c.name AS film_category_names, COUNT(fc.film_id) AS Number_of_films
FROM category AS c
INNER JOIN film_category AS fc ON c.category_id = fc.category_id
GROUP BY c.category_id 
HAVING Number_of_films BETWEEN 55 AND 65
ORDER BY Number_of_films DESC;

#option 2
SELECT name AS film_category_names, COUNT(film_id) as Number_of_films
FROM film_category 
INNER JOIN category USING (category_id)
GROUP BY category_id 
HAVING Number_of_films BETWEEN 55 AND 65
ORDER BY Number_of_films DESC;



#7.Find all film category names with average difference between the film replacement cost and the rental rate larger than 17?
SELECT name AS category_name, (AVG(replacement_cost) - AVG(rental_rate)) AS replacement_cost_rental_rate_diff
FROM film_category 
INNER JOIN film USING (film_id)
INNER JOIN category USING (category_id)
GROUP BY category_id 
HAVING replacement_cost_rental_rate_diff > 17 ;



#8.Find the address district name(s) and smallest postal code in each district(s). Ignores empty postal codes and empty district names.
SELECT DISTINCT district, MIN(postal_code)
FROM address
WHERE district !="" AND postal_code != ""
GROUP BY district
ORDER BY district;



#9.Find the names (first and last) of all customers whose first name is the same as the first name of the actor with ID 8. You cannot use the name of the actor with ID 8 as a constant (only the ID).
SELECT role, first_name, last_name
FROM (SELECT  'customer' AS role, first_name, last_name
		FROM    customer
		UNION  
		SELECT  'actor' AS role, first_name, last_name
		FROM    actor
		WHERE actor_id != 8) AS subquery
WHERE first_name IN (SELECT first_name
					 FROM actor 
                     WHERE actor_id = 8);



#10.Pick any district and any movie, and find names (first, last) of customers that rented that selected movie and has address in that selected district.
SELECT c.first_name, c.last_name, f.title, a.district
FROM customer AS c
INNER JOIN rental AS r ON r.customer_id = c.customer_id
INNER JOIN film AS f ON f.film_id = c.customer_id
INNER JOIN address AS a 
WHERE a.district = "California" AND f.title = "Academy Dinosaur";


-- ________________________________________________________________


#Part 2
#1.Using the posts table, find out the number of posts (as num_posts), the minimum creation date (as min_date), the maximum creation date (as max_date), and average score (as avg_num_posts)
SELECT COUNT(*),
	MIN(CreationDate) AS min_date,
	MAX(CreationDate) AS max_date,
	AVG(score) as avg_score
FROM Posts;


#2.Use the badges table to show badge name (as name) and the number of people who won it (as badge_count), limiting results to badges with at least 20 winners.
SELECT Name, COUNT(userid)  
FROM Badges AS b
GROUP BY b.Name
HAVING COUNT(userid) > 20
ORDER BY COUNT(userid);


#3.Find users who report being located in 'New York, NY’ city. Report id, displayname, and location in your result set.
SELECT id, displayName, location
FROM Users
WHERE location = 'New York, NY, United States';


#4.We want to know how many posts were written each month. 
#Count the number of posts by year-month. May 2013 and May 2014 should be considered as different year-months. 
#The result table should show year, month and count and order results by year, month.
SELECT YEAR(CreationDate) AS Year, MONTH(CreationDate) AS Month, COUNT(CreationDate) AS Count
FROM Posts
GROUP BY YEAR(CreationDate), MONTH(CreationDate)
ORDER BY Year ASC, Month ASC;
