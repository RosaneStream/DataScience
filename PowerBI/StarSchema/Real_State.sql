CREATE DATABASE real_estate_db;
USE real_estate_db;

CREATE TABLE agent_dim (
    agent_id INT PRIMARY KEY AUTO_INCREMENT,
    agent_name VARCHAR(100),
    agency_name VARCHAR(100),
    contact_info VARCHAR(100),
    region VARCHAR(50)
);

CREATE TABLE property_dim (
    property_id INT PRIMARY KEY AUTO_INCREMENT,
    property_type VARCHAR(50),
    property_size INT,  -- Size in square feet
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code VARCHAR(10),
    price DECIMAL(15, 2)
);

CREATE TABLE buyer_dim (
    buyer_id INT PRIMARY KEY AUTO_INCREMENT,
    buyer_name VARCHAR(100),
    contact_info VARCHAR(100),
    buyer_income DECIMAL(15, 2),
    preferred_region VARCHAR(50)
);

CREATE TABLE date_dim (
    date_id INT PRIMARY KEY AUTO_INCREMENT,
    sale_date DATE,
    day_of_week VARCHAR(10),
    month VARCHAR(20),
    year INT,
    quarter INT
);

CREATE TABLE sales_fact (
    sale_id INT PRIMARY KEY AUTO_INCREMENT,
    property_id INT,
    agent_id INT,
    buyer_id INT,
    date_id INT,
    sale_price DECIMAL(15, 2),
    commission DECIMAL(15, 2),
    properties_sold INT,
    FOREIGN KEY (property_id) REFERENCES property_dim(property_id),
    FOREIGN KEY (agent_id) REFERENCES agent_dim(agent_id),
    FOREIGN KEY (buyer_id) REFERENCES buyer_dim(buyer_id),
    FOREIGN KEY (date_id) REFERENCES date_dim(date_id)
);

INSERT INTO agent_dim (agent_name, agency_name, contact_info, region)
VALUES 
('Alice Johnson', 'Top Realty', 'alice@toprealty.com', 'North Region'),
('Bob Smith', 'Premier Properties', 'bob@premier.com', 'South Region');

INSERT INTO property_dim (property_type, property_size, city, state, zip_code, price)
VALUES 
('Apartment', 1200, 'Los Angeles', 'CA', '90001', 500000),
('Single-family Home', 2000, 'Miami', 'FL', '33101', 750000);

INSERT INTO buyer_dim (buyer_name, contact_info, buyer_income, preferred_region)
VALUES 
('John Doe', 'john@example.com', 120000, 'West Coast'),
('Jane Smith', 'jane@example.com', 150000, 'East Coast');

INSERT INTO date_dim (sale_date, day_of_week, month, year, quarter)
VALUES 
('2024-03-15', 'Friday', 'March', 2024, 1),
('2024-03-16', 'Saturday', 'March', 2024, 1);

INSERT INTO sales_fact (property_id, agent_id, buyer_id, date_id, sale_price, commission, properties_sold)
VALUES 
(1, 1, 1, 1, 500000, 25000, 1),
(2, 2, 2, 2, 750000, 37500, 1);

SELECT 
    a.agent_name,
    COUNT(f.sale_id) AS properties_sold,
    SUM(f.sale_price) AS total_sales,
    SUM(f.commission) AS total_commission
FROM 
    sales_fact f
JOIN 
    agent_dim a ON f.agent_id = a.agent_id
JOIN 
    date_dim d ON f.date_id = d.date_id
WHERE 
    d.year = 2024
GROUP BY 
    a.agent_name;