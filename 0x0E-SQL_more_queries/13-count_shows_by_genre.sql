-- script that lists all genres from hbtn_0d_tvshows and
-- displays the number of shows linked to each.

-- First column must be called genre
-- Second column must be called number_of_shows

SELECT tv_genres.name AS 'genre', COUNT(*) AS 'number_of_shows'
	FROM tv_genres
-- Don’t display a genre that doesn’t have any shows linked
INNER JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
-- Results must be sorted in descending order by the number of shows linked
ORDER BY number_of_shows DESC;
