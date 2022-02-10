SELECT DISTINCT people.name
FROM people
JOIN stars ON people.id = stars.person_id
WHERE stars.movie_id IN
    (SELECT stars.movie_id
    FROM people
    JOIN stars ON people.id = stars.person_id
    WHERE name = "Kevin Bacon" and birth = "1958")
AND people.name != "Kevin Bacon";
