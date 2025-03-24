-- Drop all tables
DROP TABLE IF EXISTS transaction CASCADE;
DROP TABLE IF EXISTS car CASCADE;
DROP TABLE IF EXISTS manufacturer CASCADE;
DROP TABLE IF EXISTS customer CASCADE;
DROP TABLE IF EXISTS salesperson CASCADE;

-- Create Tables
CREATE TABLE manufacturer (
    name VARCHAR(100) PRIMARY KEY
);

CREATE TABLE car (
    serial_number VARCHAR(100) PRIMARY KEY,
    manufacturer VARCHAR(100),
    model_name VARCHAR(100),
    weight DECIMAL(10,2) CHECK (weight > 0),
    price DECIMAL (10,2) CHECK (price > 0),
    CONSTRAINT fk_manufacturer FOREIGN KEY (manufacturer) REFERENCES manufacturer(name) ON DELETE CASCADE
);

CREATE TABLE customer (
    customerID VARCHAR(100) PRIMARY KEY,
    name VARCHAR(100),
    phone_number VARCHAR(15), 
    CONSTRAINT unique_name UNIQUE (name),
    CONSTRAINT unique_phone_number UNIQUE (phone_number)
);

CREATE TABLE salesperson (
    salespersonID VARCHAR(100) PRIMARY KEY,
    name VARCHAR(100),
    phone_number VARCHAR(15) 
);

CREATE TABLE transaction (
    transactionID VARCHAR(100) PRIMARY KEY,
    customerID VARCHAR(100),
    salespersonID VARCHAR(100),
    car_sn VARCHAR(100),
    car_characteristics VARCHAR(150),
    CONSTRAINT fk_customerID FOREIGN KEY (customerID) REFERENCES customer(customerID) ON DELETE CASCADE,
    CONSTRAINT fk_salespersonID FOREIGN KEY (salespersonID) REFERENCES salesperson(salespersonID) ON DELETE CASCADE,
    CONSTRAINT fk_car_sn FOREIGN KEY (car_sn) REFERENCES car(serial_number) ON DELETE CASCADE
);
