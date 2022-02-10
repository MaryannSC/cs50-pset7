SELECT AVG(rating) FROM
    (SELECT year, rating
    FROM movies
    INNER JOIN ratings
    ON movies.id = ratings.movie_id)
WHERE year = "2012";
