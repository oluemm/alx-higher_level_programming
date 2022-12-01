-- script that creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
-- DROP TABLE IF EXISTS cities;
-- and the table cities (in the database hbtn_0d_usa) on your MySQL server.
CREATE TABLE IF NOT EXISTS cities (
	-- id INT unique, auto generated, can’t be null and is a primary key
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	-- state_id INT, can’t be null
	state_id INT NOT NULL,
	-- name VARCHAR(256) can’t be null
	name VARCHAR(256) NOT NULL,
	-- and must be a FOREIGN KEY that references to id of the states table
	FOREIGN KEY (state_id) REFERENCES states(id)
);
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table cities already exists, your script should not fail
