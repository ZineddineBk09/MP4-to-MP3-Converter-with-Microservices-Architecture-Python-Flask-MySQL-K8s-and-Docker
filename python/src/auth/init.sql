-- this file will handle initialising database and create a mock user to test the authentication
CREATE USER IF NOT EXISTS 'auth' @'localhost' IDENTIFIED BY 'auth1234';
CREATE DATABASE IF NOT EXISTS auth;
GRANT ALL PRIVILEGES ON auth.* TO 'auth' @'localhost';
USE auth;
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL
);
INSERT INTO users (username, password)
VALUES ('test', 'test1234');