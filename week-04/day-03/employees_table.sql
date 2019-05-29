
create table employees_table (
	id serial primary key,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	gender VARCHAR(50),
	monthly_salary int,
	birth_date date
);
SELECT * FROM employees_table