create table todo_task (
	id serial primary key,
	state VARCHAR(50),
	description VARCHAR(50)
);
insert into todo_task(id,state,description)values(1,'finished','Walk the dog');
insert into todo_task(id,state,description)values(2,'in progress','Buy milk');
insert into todo_task(id,state,description)values(3,'finished','Do homework');

SELECT * FROM todo_task