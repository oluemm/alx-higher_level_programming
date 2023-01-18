-- Each record should display: tv_shows.title - tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
	FROM tv_shows
-- If a show doesn’t have a genre, display NULL
	LEFT JOIN tv_show_genres
	ON tv_shows.id=tv_show_genres.show_id
-- lists all shows contained in hbtn_0d_tvshows without a genre linked.
	WHERE tv_show_genres.genre_id IS NULL
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
ORDER BY tv_shows.title,tv_show_genres.genre_id ASC ;
