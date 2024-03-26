CREATE DATABASE BankSystem;
USE BankSystem;

-- Customers table
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    DOB DATE,
    email VARCHAR(100),
    phone_number VARCHAR(20),
    address VARCHAR(255)
);

-- Accounts table
CREATE TABLE Accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    account_type VARCHAR(20),
    balance FLOAT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
) AUTO_INCREMENT = 1001;

-- Transactions table
CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY,
    account_id INT,
    transaction_type VARCHAR(20),
    amount FLOAT,
    transaction_date DATE,
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id)
);

SELECT * FROM Customers;
SELECT * FROM Accounts;
SELECT * FROM Transactions;

-- Inserting into Customers table
INSERT INTO Customers (customer_id, first_name, last_name, DOB, email, phone_number, address)
VALUES
(1, 'Ramesh', 'Kumar', '1990-05-15', 'ramesh@gmail.com', '9876543210', '12, NGB Street, Mumbai, Maharastra, India'),
(2, 'Sunita', 'Patil', '1985-10-25', 'sunita@gmail.com', '8876543211', '45, Nehru Street, Surat, Gujarat, India');

-- Inserting into Accounts table
INSERT INTO Accounts (customer_id, account_type, balance)
VALUES
(1, 'savings', 5000.00),
(2, 'current', 10000.00);

-- Inserting into Transactions table
INSERT INTO Transactions (transaction_id, account_id, transaction_type, amount, transaction_date)
VALUES
(101, 1001, 'deposit', 3000.00, '2024-03-15'),
(102, 1002, 'withdrawal', 500.00, '2024-03-20');

