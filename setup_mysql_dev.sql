-- SETUP FILE FOR THE DATABASE
CREATE DATABASE IF NOT EXISTS regexpress_cars;
USE regexpress_cars;
CREATE USER IF NOT EXISTS 'sanmi'@'localhost' IDENTIFIED BY 'April301989/';
GRANT ALL  ON * TO 'sanmi'@'localhost';
GRANT SELECT ON performance_schema.* TO 'sanmi'@'localhost' WITH GRANT OPTION;

