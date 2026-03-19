-- Parking Lot*******
-- *                *
-- *                *
--- *****************

-- SETUP:
-- Connect to the server (Azure Data Studio / Database extension/psql)
-- Create a database (I recommend chinook_pg)
-- Execute the Chinook database (from the Chinook_pg.sql file) to create Chinook resources in your server (I recommend doing this from psql)

-- Comment can be done single line with --
-- Comment can be done multi line with /* */

/*
DQL - Data Query Language
Keywords:

SELECT - retrieve data, select the columns from the resulting set
FROM - the table(s) to retrieve data from
WHERE - a conditional filter of the data
GROUP BY - group the data based on one or more columns
HAVING - a conditional filter of the grouped data
ORDER BY - sort the data
*/

SELECT * FROM actor;
SELECT last_name FROM actor;
SELECT * FROM actor WHERE first_name = 'Morgan';
select * from actor where first_name = 'John';

-- BASIC CHALLENGES
-- List all customers (full name, customer id, and country) who are not in the USA
SELECT  first_name || ' ' || last_name as full_name, customer_id, country WHERE NOT country = 'USA' FROM customer;

-- List all customers from Brazil
SELECT  first_name, last_name, customer_id, country WHERE country = 'Brazil' FROM customer;

-- List all sales agents
SELECT first_name || ' ' || last_name as full_name FROM EMPLOYEE WHERE title LIKE 'Sales%';

-- Retrieve a list of all countries in billing addresses on invoices
SELECT DISTINCT billing_country FROM invoice; 

-- Retrieve how many invoices there were in 2009, and what was the sales total for that year?
SELECT COUNT(*), SUM(total) FROM invoice WHERE invoice_date >= '2009-01-01' AND invoice_date <= '2010-01-01';

-- (challenge: find the invoice count sales total for every year using one query)
SELECT COUNT(*), SUM(total) EXTRACT(YEAR FROM invoice_date) FROM invoice GROUP BY EXTRACT(YEAR FROM invoice_date);


-- how many line items were there for invoice #37
SELECT COUNT(*) FROM invoice_line WHERE invoice_id = 37;

-- how many invoices per country? BillingCountry  # of invoices -
SELECT billing_country, COUNT(*) as num_invoices FROM invoice GROUP BY billing_country;

-- Retrieve the total sales per country, ordered by the highest total sales first.
SELECT billing_country, SUM(total) FROM invoice GROUP BY billing_country ORDER BY SUM(total) DESC;


-- JOINS CHALLENGES
-- Every Album by Artist
SELECT album.title, artist.name FROM album LEFT JOIN artist ON artist.artist_id = album.artist_id;

-- (inner keyword is optional for inner join)
-- All songs of the rock genre
SELECT * FROM track LEFT JOIN genre ON track.genre_id = genre.genre_id WHERE track.genre_id = 1;

-- Show all invoices of customers from brazil (mailing address not billing)
SELECT * FROM invoice INNER JOIN customer ON invoice.customer_id = customer.customer_id WHERE country = 'Brazil';

-- Show all invoices together with the name of the sales agent for each one
SELECT * FROM invoice INNER JOIN customer ON invoice.customer_id = customer.customer_id INNER JOIN employee ON customer.support_rep_id = employee.employee_id;

-- Which sales agent made the most sales in 2009?
SELECT employee.first_name || ' ' || employee.last_name as full_name, SUM(invoice.total) as total_sales
FROM invoice
INNER JOIN customer ON invoice.customer_id = customer.customer_id
INNER JOIN employee ON customer.support_rep_id = employee.employee_id
WHERE invoice.invoice_date >= '2009-01-01' AND invoice.invoice_date < '2010-01-01'
GROUP BY employee.employee_id
ORDER BY total_sales DESC;

-- How many customers are assigned to each sales agent?
SELECT employee.first_name || ' ' || employee.last_name as full_name, COUNT(*) as num_customers
FROM employee LEFT JOIN customer ON employee.employee_id = customer.support_rep_id GROUP BY employee.employee_id;

-- Which track was purchased the most in 2010?
SELECT track.name, SUM(invoice_line.quantity) as num_purchases
FROM track INNER JOIN invoice_line ON track.track_id = invoice_line.track_id
INNER JOIN invoice ON invoice_line.invoice_id = invoice.invoice_id
WHERE EXTRACT(YEAR FROM invoice.invoice_date) = 2010
GROUP BY track.name
ORDER BY num_purchases DESC;


-- Show the top three best selling artists.
SELECT artist.name, SUM(invoice_line.quantity) as num_purchases
FROM artist
INNER JOIN album ON artist.artist_id = album.artist_id
INNER JOIN track ON album.album_id = track.album_id
INNER JOIN invoice_line ON track.track_id = invoice_line.track_id
GROUP BY artist.artist_id
ORDER BY num_purchases DESC
LIMIT 3;

-- Which customers have the same initials as at least one other customer?
SELECT c.first_name || ' ' || c.last_name as full_name, c1.first_name || ' ' || c1.last_name as other_name
FROM customer as c
INNER JOIN customer as c1 ON left(c.first_name, 1) = left(c1.first_name, 1) AND left(c.last_name, 1) = left(c1.last_name, 1)
WHERE c.customer_id <> c1.customer_id; 

-- Which countries have the most invoices?
SELECT billing_country, COUNT(*) as num_invoices
FROM invoice
GROUP BY billing_country
ORDER BY num_invoices DESC;


-- Which city has the customer with the highest sales total?
SELECT billing_city, MAX(total) as max_total
FROM invoice
GROUP BY billing_city
ORDER BY max_total DESC
LIMIT 1;


-- Who is the highest spending customer?
SELECT customer.first_name || ' ' || customer.last_name as full_name, SUM(invoice.total) as total_spent
FROM customer
INNER JOIN invoice ON customer.customer_id = invoice.customer_id
GROUP BY customer.customer_id
ORDER BY total_spent DESC
LIMIT 1;


-- Return the email and full name of of all customers who listen to Rock.
SELECT DISTINCT customer.email, customer.first_name || ' ' || customer.last_name as full_name
FROM customer
INNER JOIN invoice ON customer.customer_id = invoice.customer_id
INNER JOIN invoice_line ON invoice.invoice_id = invoice_line.invoice_id
INNER JOIN track ON invoice_line.track_id = track.track_id
INNER JOIN genre ON track.genre_id = genre.genre_id
WHERE genre.name = 'Rock';


-- Which artist has written the most Rock songs?
SELECT artist.name, COUNT(*) as num_rock_songs
FROM artist
INNER JOIN album ON artist.artist_id = album.artist_id
INNER JOIN track ON album.album_id = track.album_id
INNER JOIN genre ON track.genre_id = genre.genre_id
WHERE genre.name = 'Rock'
GROUP BY artist.artist_id
ORDER BY num_rock_songs DESC
LIMIT 1;


-- Which artist has generated the most revenue?
SELECT artist.name, SUM(invoice_line.quantity * invoice_line.unit_price) as total_revenue
FROM artist
INNER JOIN album ON artist.artist_id = album.artist_id
INNER JOIN track ON album.album_id = track.album_id
INNER JOIN invoice_line ON track.track_id = invoice_line.track_id
GROUP BY artist.artist_id
ORDER BY total_revenue DESC
LIMIT 1;


-- ADVANCED CHALLENGES
-- solve these with a mixture of joins, subqueries, CTE, and set operators.
-- solve at least one of them in two different ways, and see if the execution
-- plan for them is the same, or different.

-- 1. which artists did not make any albums at all?
SELECT name FROM artist WHERE artist_id NOT IN (SELECT artist_id FROM album);

-- 2. which artists did not record any tracks of the Latin genre?
SELECT name FROM artist WHERE artist_id NOT IN (
    SELECT artist_id FROM album
    INNER JOIN track ON album.album_id = track.album_id
    INNER JOIN genre ON track.genre_id = genre.genre_id
    WHERE genre.name = 'Latin'
);

-- 3. which video track has the longest length? (use media type table)
SELECT track.name, track.milliseconds
FROM track
INNER JOIN media_type ON track.media_type_id = media_type.media_type_id
WHERE media_type.name LIKE '%video%'
ORDER BY track.milliseconds DESC
LIMIT 1;

-- 4. boss employee (the one who reports to nobody)
SELECT first_name || ' ' || last_name as full_name FROM employee WHERE reports_to IS NULL;

-- 5. how many audio tracks were bought by German customers, and what was
--    the total price paid for them?
SELECT COUNT(*) as num_audio_tracks, SUM(invoice_line.unit_price * invoice_line.quantity) as total_price
FROM invoice_line
INNER JOIN invoice ON invoice_line.invoice_id = invoice.invoice_id
INNER JOIN customer ON invoice.customer_id = customer.customer_id
INNER JOIN track ON invoice_line.track_id = track.track_id
INNER JOIN media_type ON track.media_type_id = media_type.media_type_id
WHERE media_type.name LIKE '%audio%' AND customer.country = 'Germany';


-- 6. list the names and countries of the customers supported by an employee
--    who was hired younger than 35.
SELECT customer.first_name || ' ' || customer.last_name as full_name, customer.country
FROM customer
INNER JOIN employee ON customer.support_rep_id = employee.employee_id
WHERE employee.hire_date > (CURRENT_DATE - INTERVAL '35 years');


-- DML exercises

-- 1. insert two new records into the employee table.
INSERT INTO employee (last_name, first_name, title, reports_to, email) VALUES
('John', 'Doe', 'IT Staff', 6, 'john.doe@example.com'),
('Jane', 'Smith', 'Sales Support Agent', 2, 'jane.smith@example.com');

-- 2. insert two new records into the tracks table.
INSERT INTO track (name, album_id, media_type_id, genre_id, composer, milliseconds, bytes, unit_price) VALUES
('New Track 1', 1, 1, 1, 'Composer 1', 200000, 5000000, 0.99),
('New Track 2', 1, 1, 1, 'Composer 2', 250000, 6000000, 0.99);

-- 3. update customer Aaron Mitchell's name to Robert Walter
UPDATE customer
SET first_name = 'Robert', last_name = 'Walter'
WHERE first_name = 'Aaron' AND last_name = 'Mitchell';

-- 4. delete one of the employees you inserted.
DELETE FROM employee
WHERE first_name = 'John' AND last_name = 'Doe';

-- 5. delete customer Robert Walter.
DELETE FROM invoice_line
WHERE invoice_id IN (
    SELECT invoice_id FROM invoice
    WHERE customer_id IN (
        SELECT customer_id FROM customer
        WHERE first_name = 'Robert' AND last_name = 'Walter'
    )
);

DELETE FROM invoice
WHERE customer_id IN (
    SELECT customer_id FROM customer
    WHERE first_name = 'Robert' AND last_name = 'Walter'
);

DELETE FROM customer
WHERE first_name = 'Robert' AND last_name = 'Walter';