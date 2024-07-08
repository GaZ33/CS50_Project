show databases;
CREATE DATABASE IF NOT EXISTS gzauto;
USE gzauto;

CREATE TABLE Account(
	Id INT PRIMARY KEY,
    Username VARCHAR(25) NOT NULL,
    Password VARCHAR(80) NOT NULL
);
CREATE TABLE Information(
	Id INT PRIMARY KEY,
    FName VARCHAR(20) NOT NULL,
    MName VARCHAR(40),
    LName VARCHAR(30) NOT NULL,
    Email VARCHAR(50),
    City VARCHAR(20),
    Street VARCHAR(30),
    Neighborhood VARCHAR(30),
    Category VARCHAR(3) NOT NULL,
    Cellphone VARCHAR(16),
    Birthday DATETIME,
    Account_id INT,
    CONSTRAINT FOREIGN KEY (Account_id) REFERENCES Account(id)
);
SHOW TABLES;
DESC account;
DESC information;