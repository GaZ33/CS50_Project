show databases;
CREATE DATABASE IF NOT EXISTS gzauto;
USE gzauto;

SELECT * FROM Account;


DELETE FROM Account WHERE Id > 0;
DELETE FROM Information WHERE Account_id > 0;

CREATE TABLE Account(
	Id INT PRIMARY KEY AUTO_INCREMENT,
    Username VARCHAR(25) NOT NULL UNIQUE,
    Password VARCHAR(80) NOT NULL
);
CREATE TABLE Information(
	Id INT PRIMARY KEY AUTO_INCREMENT,
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
    CONSTRAINT FOREIGN KEY (Account_id) REFERENCES Account(Id)
);

CREATE TABLE Employees(
	Id INT PRIMARY KEY AUTO_INCREMENT,
	Username VARCHAR(25) NOT NULL UNIQUE,
    Password VARCHAR(80) NOT NULL,
    Role VARCHAR(15) NOT NULL,
    FName VARCHAR(20) NOT NULL,
    MName VARCHAR(40),
    LName VARCHAR(30) NOT NULL,
    Email VARCHAR(50),
    Cellphone VARCHAR(16),
    Birthday DATETIME
);
CREATE TABLE Performance(
	Id INT PRIMARY KEY AUTO_INCREMENT,
	Driving FLOAT NOT NULL,
    Parking FLOAT NOT NULL,
    Parallel_parking FLOAT NOT NULL,
    Attention FLOAT NOT NULL,
    Account_id INT NOT NULL,
    Employees_id INT NOT NULL,
    FOREIGN KEY (Account_id) REFERENCES Account(Id),
    FOREIGN KEY (Employees_id) REFERENCES Employees(Id)
);
CREATE TABLE Classes(
	Id INT PRIMARY KEY AUTO_INCREMENT,
	Date DATETIME NOT NULL,
    Account_id INT NOT NULL,
    Employees_id INT NOT NULL,
    FOREIGN KEY (Account_id) REFERENCES Account(Id),
    FOREIGN KEY (Employees_id) REFERENCES Employees(Id)
);
SHOW TABLES;
DESC account;
DESC information;
DROP TABLE Account;
DROP TABLE Information;
DROP TABLE Performance;