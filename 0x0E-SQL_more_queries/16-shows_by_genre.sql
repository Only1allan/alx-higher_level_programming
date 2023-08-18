-- Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT tv_show.title, tv_genres.name
FROM tv_shows 
LEFT JOIN tv_show_genres 
ON tv_show_genres.show_id = tv_show.id
LEFT JOIN tv_genres 
ON tv_genres.id = tv_show_genres_id ORDER BY tv_shows.title, tv_genres.name;