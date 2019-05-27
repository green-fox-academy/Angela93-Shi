-- Create the necessary tables and maybe add the necessary fields
create table employees (

	id INT,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	username VARCHAR(50),
	date_of_employment DATE,
	date_of_exit DATE,
	role VARCHAR(50),
	salary VARCHAR(50)
);
SELECT * FROM employees
insert into employees (id, first_name, last_name, username,date_of_employment, date_of_exit, role,salary) values (1, 'Paola', 'Heathwood','pheathwood0', '2018-11-13', '2019-11-13', 'Engineer','10000');
-- Alter the existing tables so that an employee belongs to a department as well
ALTER TABLE employees
	ADD COLUMN dapartment VARCHAR DEFAULT 'IT'
-- Remove the username field from the table
ALTER TABLE employees
	DROP COLUMN "username"
-- Rename a column
UPDATE employees
SET date_of_exit ='2019-11-12'
WHERE id=1