-- DRAFT Etsy Crepe Paper Flower Market Analysis

-- 1. Create a view of all crepe paper flower arrangement product listings
CREATE VIEW pflistings AS
SELECT *
FROM july2020_2_active_listings as pf
WHERE LOWER(pf.title) NOT LIKE '%roll%'
  AND LOWER(pf.title) NOT LIKE '%wrapping paper%'
  AND (LOWER(pf.title) LIKE '%paper flower%'
  OR LOWER(pf.title) LIKE '%paper bouquet%'
	OR LOWER(pf.title) LIKE '%paper arrangement%');


-- 2. List the top five products on Etsy with the most number of views.
SELECT *
FROM pflistings pf
WHERE pf.currency_code = 'USD'
ORDER BY pf.views DESC
LIMIT 5;


-- 2. List the top five produces on Etsy with the most number of favorers
SELECT *
FROM pflistings pf
WHERE pf.currency_code = 'USD'
ORDER BY pf.num_favorers DESC
LIMIT 5;


-- 4. What is the average price of a paper flower bouquet?
SELECT AVG(pf.price)
FROM pflistings pf
WHERE pf.currency_code = 'USD';
-- $57.83

-- Maximum Price: $2,050
SELECT MAX(pf.price)
FROM pflistings pf
WHERE pf.currency_code = 'USD';


-- Minimum Price: $0.99
SELECT MIN(pf.price)
FROM pflistings pf
WHERE pf.currency_code = 'USD';


-- Price distribution:
SELECT sub1.price_category, COUNT(sub1.listing_id)
FROM
(SELECT pf.listing_id, pf.title, pf.price,
	CASE
		WHEN pf.price <= 10 THEN 'Less than or equal to $10'
		WHEN pf.price > 10 AND pf.price <= 15 THEN '$10 to $15'
		WHEN pf.price > 15 AND pf.price <= 25 THEN '$15 to $25'
		WHEN pf.price > 25 AND pf.price <= 50 THEN '$25 to $50'
		WHEN pf.price > 50 AND pf.price <= 100 THEN '$50 to $100'
		WHEN pf.price > 100 AND pf.price <= 200 THEN '$100 to $200'
		WHEN pf.price > 200 THEN 'Greater than $200'
		ELSE 'No Price Data'
	END AS price_category
FROM pflistings pf
WHERE pf.currency_code = 'USD') AS sub1
GROUP BY sub1.price_category;


-- 5. What are the most popular tags to use for products, ranked in order?
--    (Choose number of tags by maximum number of tags)
SELECT sub1.tags tag, COUNT(sub1.listing_ID)
FROM
(SELECT tags.listing_id, tags.tags
FROM july2020_2_active_listings_tags AS tags
JOIN pflistings pf
ON pf.listing_id = tags.listing_id) AS sub1
GROUP BY 1
ORDER BY 2 DESC
LIMIT 13;

-- 6. What are the most popular occasions?
SELECT sub1.occasion occasion, COUNT(sub1.listing_ID)
FROM
(SELECT occasions.listing_id, occasions.occasion
FROM july2020_2_active_listings_occasion AS occasions
JOIN pflistings pf
ON pf.listing_id = occasions.listing_id) AS sub1
GROUP BY 1
ORDER BY 2 DESC
LIMIT 5;


-- 7. What are the most popular flowers?
WITH flowerwords AS (
	SELECT dw.listing_id, fl.flower
	FROM july2020_2_active_listings_descwords dw
	JOIN july2020_flowerlist fl
	ON dw.description = fl.flower
	)

SELECT fl.flower, COUNT(*)
FROM flowerwords fl
JOIN pflistings pf
ON fl.listing_id = pf.listing_id
GROUP BY 1
ORDER BY 2 DESC;



-- 8. Are more products made to order or sold-as is?
SELECT pf.when_made, COUNT(*)
FROM pflistings pf
GROUP BY 1;
