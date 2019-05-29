create table cars (
	id serial primary key,
	brand VARCHAR(50),
	model VARCHAR(50),
	year int,
	condition VARCHAR(50),
	price int,
	count int
);
SELECT * FROM cars