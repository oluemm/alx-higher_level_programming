-- script that lists all cities contained in the databASe hbtn_0d_usa.
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in AScending order by cities.id
-- You can use only one SELECT statement
SELECT c.id,c.name,s.name
FROM cities AS c left join states AS s 
ON c.state_id=s.id
ORDER BY c.id;
