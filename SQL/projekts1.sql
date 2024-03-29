CREATE TABLE nomnom (
    name TEXT,
    neighbourhood TEXT,
    cuisine TEXT,
    review REAL,
    price INTEGER,
    health TEXT
);

-- We'll use a WITH clause to generate our random data
WITH RECURSIVE random_data AS (
    SELECT 1 AS id,
        'Restaurant' || (ABS(RANDOM()) % 1000 + 1) AS name, -- Generates names like 'Restaurant1', 'Restaurant2', etc.
        CASE ABS(RANDOM()) % 5 
            WHEN 0 THEN 'Midtown' 
            WHEN 1 THEN 'Downtown'
            WHEN 2 THEN 'Chinatown'
            WHEN 3 THEN 'Uptown'
            ELSE 'Brooklyn' END AS neighbourhood,
        CASE ABS(RANDOM()) % 5 
            WHEN 0 THEN 'Chinese' 
            WHEN 1 THEN 'Italian'
            WHEN 2 THEN 'Indian'
            WHEN 3 THEN 'Mexican'
            ELSE 'French' END AS cuisine,
        (ABS(RANDOM()) % 10 + 1) AS review,  -- Generates numbers between 1 and 10
        (ABS(RANDOM()) % 200 + 1) AS price,  -- Generates numbers between 1 and 200
        CASE ABS(RANDOM()) % 6
            WHEN 0 THEN 'A'
            WHEN 1 THEN 'B'
            WHEN 2 THEN 'C'
            WHEN 3 THEN 'D'
            WHEN 4 THEN 'E'
            ELSE 'F' END AS health
    UNION ALL
    SELECT id + 1,
        'Restaurant' || (ABS(RANDOM()) % 1000 + 1),
        CASE ABS(RANDOM()) % 5 
            WHEN 0 THEN 'Midtown' 
            WHEN 1 THEN 'Downtown'
            WHEN 2 THEN 'Chinatown'
            WHEN 3 THEN 'Uptown'
            ELSE 'Brooklyn' END,
        CASE ABS(RANDOM()) % 5 
            WHEN 0 THEN 'Chinese' 
            WHEN 1 THEN 'Italian'
            WHEN 2 THEN 'Indian'
            WHEN 3 THEN 'Mexican'
            ELSE 'French' END,
        (ABS(RANDOM()) % 10 + 1),
        (ABS(RANDOM()) % 200 + 1),
        CASE ABS(RANDOM()) % 6
            WHEN 0 THEN 'A'
            WHEN 1 THEN 'B'
            WHEN 2 THEN 'C'
            WHEN 3 THEN 'D'
            WHEN 4 THEN 'E'
            ELSE 'F' END
    FROM random_data
    WHERE id < 100
)

-- Inserting the generated data into the nomnom table
INSERT INTO nomnom (name, neighbourhood, cuisine, review, price, health)
SELECT name, neighbourhood, cuisine, review, price, health
FROM random_data;

SELECT * FROM nomnom;

SELECT *
FROM nomnom;

SELECT DISTINCT neighbourhood
FROM nomnom

SELECT DISTINCT cuisine
FROM nomnom

SELECT name, neighbourhood, review, price, health
FROM nomnom
WHERE cuisine = 'Chinese';

SELECT *
FROM nomnom
WHERE review > 4

SELECT *
FROM nomnom
WHERE cuisine = "Italian" AND price > 99

SELECT *
FROM nomnom
WHERE name LIKE '%7';

SELECT *
FROM nomnom
WHERE neighbourhood IN ('Midtown', 'Downtown', 'Chinatown');

SELECT *
FROM nomnom
WHERE health = '';

SELECT name, review
FROM nomnom
ORDER BY review DESC
LIMIT 10;

SELECT name,
    CASE 
        WHEN review > 4.5 THEN 'Extraordinary'
        WHEN review > 4 THEN 'Excellent'
        WHEN review > 3 THEN 'Good'
        WHEN review > 2 THEN 'Fair'
        ELSE 'Poor'
    END AS "Socre"
FROM nomnom;
