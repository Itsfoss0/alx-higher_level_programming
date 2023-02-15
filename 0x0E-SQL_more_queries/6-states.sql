--creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);