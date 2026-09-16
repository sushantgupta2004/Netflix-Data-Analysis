-- Netflix Data Analysis - MySQL
-- Load the CSV into a table named netflix before running these queries.

CREATE DATABASE IF NOT EXISTS netflix_analysis;
USE netflix_analysis;

-- Example table structure
CREATE TABLE IF NOT EXISTS netflix (
    show_id VARCHAR(20),
    type VARCHAR(20),
    title VARCHAR(255),
    director TEXT,
    cast TEXT,
    country TEXT,
    date_added VARCHAR(50),
    release_year INT,
    rating VARCHAR(30),
    duration VARCHAR(30),
    listed_in TEXT,
    description TEXT
);

-- 1. Movies vs TV Shows
SELECT type, COUNT(*) AS total_titles
FROM netflix
GROUP BY type
ORDER BY total_titles DESC;

-- 2. Titles by release year
SELECT release_year, COUNT(*) AS total_titles
FROM netflix
GROUP BY release_year
ORDER BY release_year;

-- 3. Top countries
SELECT country, COUNT(*) AS total_titles
FROM netflix
WHERE country IS NOT NULL AND TRIM(country) <> ''
GROUP BY country
ORDER BY total_titles DESC
LIMIT 10;

-- 4. Most common ratings
SELECT rating, COUNT(*) AS total_titles
FROM netflix
WHERE rating IS NOT NULL AND TRIM(rating) <> ''
GROUP BY rating
ORDER BY total_titles DESC;

-- 5. Longest movies
SELECT title, duration
FROM netflix
WHERE type = 'Movie'
ORDER BY CAST(SUBSTRING_INDEX(duration, ' ', 1) AS UNSIGNED) DESC
LIMIT 10;

-- 6. Multi-season TV shows
SELECT title, duration
FROM netflix
WHERE type = 'TV Show'
  AND CAST(SUBSTRING_INDEX(duration, ' ', 1) AS UNSIGNED) >= 3
ORDER BY CAST(SUBSTRING_INDEX(duration, ' ', 1) AS UNSIGNED) DESC;

-- 7. Titles added by year
SELECT
    YEAR(STR_TO_DATE(date_added, '%M %d, %Y')) AS added_year,
    COUNT(*) AS total_added
FROM netflix
WHERE date_added IS NOT NULL AND TRIM(date_added) <> ''
GROUP BY added_year
ORDER BY added_year;

-- 8. Titles by content type and rating
SELECT type, rating, COUNT(*) AS total_titles
FROM netflix
GROUP BY type, rating
ORDER BY type, total_titles DESC;

-- 9. Recent releases
SELECT title, type, release_year
FROM netflix
WHERE release_year >= 2018
ORDER BY release_year DESC, title;

-- 10. Missing-value audit
SELECT
    SUM(CASE WHEN director IS NULL OR TRIM(director) = '' THEN 1 ELSE 0 END) AS missing_director,
    SUM(CASE WHEN cast IS NULL OR TRIM(cast) = '' THEN 1 ELSE 0 END) AS missing_cast,
    SUM(CASE WHEN country IS NULL OR TRIM(country) = '' THEN 1 ELSE 0 END) AS missing_country,
    SUM(CASE WHEN rating IS NULL OR TRIM(rating) = '' THEN 1 ELSE 0 END) AS missing_rating
FROM netflix;
