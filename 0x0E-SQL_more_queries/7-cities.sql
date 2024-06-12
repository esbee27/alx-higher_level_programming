-- Creates database
-- Creates table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_us
a;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT UNIQUE PRIMARY KEY AUTO_INCREMENT NOT NULL,
	state_id NOT NULL INT,
	name VARCHAR(256)) NOT NULL,
	FOREIGN KEY (states_id),
	REFERENCES states(id));
