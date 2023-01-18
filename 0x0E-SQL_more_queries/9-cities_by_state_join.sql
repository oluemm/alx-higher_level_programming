-- script that lists all cities contained in the databASe hbtn_0d_usa.

-- Each record should display: cities.id - cities.name - states.name
SELECT cities.id, cities.name, states.name
	FROM cities
	JOIN states
	WHERE cities.state_id = states.id
-- Results must be sorted in Ascending order by cities.id
ORDER BY cities.id ASC;
