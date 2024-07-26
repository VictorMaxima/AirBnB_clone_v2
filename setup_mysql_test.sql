CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXITS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db .* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performace_schema .* TO 'hbng_test'@'localhost';