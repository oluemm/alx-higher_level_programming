CREATE DATABASE IF NOT EXISTS `hbtn_0d_tvshows`;
-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download
-- $ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows

-- Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
	FROM tv_shows
	JOIN tv_show_genres
	ON tv_shows.id=tv_show_genres.show_id 
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
ORDER BY tv_shows.title,tv_show_genres.genre_id ASC ;
