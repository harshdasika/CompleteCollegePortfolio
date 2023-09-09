DROP DATABASE IF EXISTS hospital;
CREATE DATABASE hospital;
USE hospital;

DROP TABLE IF EXISTS hospital CASCADE;
DROP TABLE IF EXISTS physician CASCADE;
DROP TABLE IF EXISTS nurse CASCADE;
DROP TABLE IF EXISTS patient CASCADE; 
DROP TABLE IF EXISTS room CASCADE; 
DROP TABLE IF EXISTS healthrecord CASCADE; 
DROP TABLE IF EXISTS instruction CASCADE; 
DROP TABLE IF EXISTS invoice CASCADE; 
DROP TABLE IF EXISTS payments CASCADE; 

CREATE TABLE hospital (
    name VARCHAR(30) NOT NULL,
	address VARCHAR(50) NOT NULL,
	PRIMARY KEY (name)
);

CREATE TABLE physician (
	phys_id INT NOT NULL,
    name VARCHAR(30) NOT NULL,
	cert_num INT NOT NULL,
	expertise VARCHAR(30) NOT NULL,
    address VARCHAR(50) NOT NULL,
    p_number VARCHAR(12) NOT NULL,
    hosp VARCHAR(30) NOT NULL,
    FOREIGN KEY (hosp) REFERENCES hospital(name),
	PRIMARY KEY (phys_id)
);

CREATE TABLE nurse (
	nurse_id INT NOT NULL,
    name VARCHAR(30) NOT NULL,
	cert_num INT NOT NULL,
    address VARCHAR(50) NOT NULL,
    p_number VARCHAR(12) NOT NULL,
    hosp VARCHAR(30) NOT NULL,
    FOREIGN KEY (hosp) REFERENCES hospital(name),
	PRIMARY KEY (nurse_id)
);

CREATE TABLE patient (
	id INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    address VARCHAR(50) NOT NULL,
    p_number VARCHAR(12) NOT NULL,
    hosp VARCHAR(30) NOT NULL,
    FOREIGN KEY (hosp) REFERENCES hospital(name),
	PRIMARY KEY (id)
);

CREATE TABLE room (
	room_no INT NOT NULL,
	capacity INT NOT NULL,
	fee INT NOT NULL,
	PRIMARY KEY (room_no)
);

CREATE TABLE healthrecord (
	record_id INT NOT NULL,
	patient_id INT NOT NULL,
	disease VARCHAR(30) NOT NULL,
    date VARCHAR(30) NOT NULL,
    status VARCHAR(20) NOT NULL,
    description VARCHAR(50) NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES patient(id),
	PRIMARY KEY (record_id)
);

CREATE TABLE instruction (
    code INT NOT NULL,
    fee INT NOT NULL,
    patient_id INT NOT NULL,
    description VARCHAR(50) NOT NULL,
    PRIMARY KEY (code),
    FOREIGN KEY (patient_id) REFERENCES patient(id)
);

CREATE TABLE invoice (
	invoice_id INT NOT NULL,
	patient_id INT NOT NULL,
	room INT NOT NULL,
    instructions INT NOT NULL,
    PRIMARY KEY(invoice_id),
    FOREIGN KEY (patient_id) REFERENCES patient(id),
    FOREIGN KEY (room) REFERENCES room(room_no),
    FOREIGN KEY (instructions) REFERENCES instruction(code)
);

CREATE TABLE payments (
	patient_id INT NOT NULL,
	date VARCHAR(30) NOT NULL,
	amount INT NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES patient(id)
);

CREATE TABLE medication (
	patient_id INT NOT NULL,
    amount VARCHAR(30) NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES patient(id)
)




