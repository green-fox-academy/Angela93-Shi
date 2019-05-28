SELECT * FROM rating
SELECT * FROM movie
SELECT * FROM reviewer
-- Find the titles of all movies directed by Steven Spielberg. 
SELECT title,director FROM movie WHERE director = 'Steven Spielberg'
-- Find all years that have a movie that received a rating of 4 or 5, and sort them in increasing order. 
SELECT title,year,stars FROM Movie JOIN Rating ON movie.mID=Rating.mID  WHERE stars = 4 OR stars =5 ORDER BY stars ASC
-- Find the titles of all movies that have no ratings. 
SELECT mID,title FROM Movie WHERE mID NOT IN (SELECT mID FROM Rating)
-- Some reviewers didn't provide a date with their rating. Find the names of all reviewers who have ratings with a NULL value for the date. 
SELECT name FROM Reviewer JOIN Rating ON Reviewer.rID = Rating.rID WHERE ratingDate IS NULL
-- Write a query to return the ratings data in a more readable format: reviewer name, movie title, stars, and ratingDate.
-- Also, sort the data, first by reviewer name, then by movie title, and lastly by number of stars.
SELECT name,title,stars,ratingDate FROM rating 
JOIN movie ON rating.mID = movie.mID
JOIN reviewer ON rating.rID = reviewer.rID
ORDER BY name,title,stars
-- Find the names of all reviewers who rated Gone with the Wind. 
SELECT DISTINCT name FROM Rating
JOIN Reviewer ON Rating.rID = Reviewer.rID
JOIN movie ON rating.mID = movie.mID
WHERE rating.mID = 101
-- For any rating where the reviewer is the same as the director of the movie, return the reviewer name, movie title, and number of stars.
SELECT name,title,stars FROM rating 
JOIN movie ON rating.mID = movie.mID
JOIN reviewer ON rating.rID = reviewer.rID
WHERE reviewer.name = movie.director
-- Create a view where you display the reviewer's name and the amount of their review
CREATE VIEW amount_of_reviews AS SELECT name,COUNT(Mid) FROM rating JOIN reviewer ON rating.rID= reviewer.rID GROUP BY reviewer.name
SELECT * FROM amount_of_reviews
-- Create a view where you display the movies which have no review
CREATE VIEW movies_without_review AS SELECT movie.mID,title FROM movie LEFT JOIN rating ON movie.mID = rating.mID WHERE rating.stars IS NULL
SELECT * FROM movies_without_review
-- Create a view where you display all the directors (do not include null values)
CREATE VIEW director_view AS SELECT DISTINCT director FROM movie WHERE director IS NOT NULL
SELECT * FROM director_view
-- Create a view where you display the movie title and the average rating
CREATE VIEW movie_average_rating AS SELECT title,AVG(stars) AS average_rating FROM movie JOIN rating ON movie.mID = rating.mID GROUP BY movie.title
SELECT * FROM movie_average_rating
---------------------------------------------------------------------------------------------------------------------------------
-- Joins and subqueries - PostgreSQL Exercises
-- How can you produce a list of the start times for bookings by members named 'David Farrell'? 
SELECT starttime FROM cd.bookings INNER JOIN cd.members ON cd.bookings.memid=cd.members.memid
WHERE cd.members.surname='Farrell' AND cd.members.firstname='David'
-- How can you produce a list of the start times for bookings for tennis courts, for the date '2012-09-21'? Return a list of start time and facility name pairings, ordered by the time. 
SELECT starttime AS start,name FROM cd.bookings INNER JOIN cd.facilities 
ON cd.bookings.facid=cd.facilities.facid WHERE cd.bookings.starttime > '2012-09-21' 
AND cd.bookings.starttime < '2012-09-22'
AND cd.facilities.name LIKE'Tennis Court%' 
ORDER BY starttime
-- How can you output a list of all members who have recommended another member? Ensure that there are no duplicates in the list, and that results are ordered by (surname, firstname). 
SELECT DISTINCT recs.firstname AS firstname,recs.surname AS surname FROM cd.members
INNER JOIN cd.members recs
ON recs.memid = cd.members.recommendedby
ORDER BY surname,firstname
-- How can you output a list of all members, including the individual who recommended them (if any)? Ensure that results are ordered by (surname, firstname). 
SELECT mem.firstname AS memfname,mem.surname AS memsname,rec.firstname AS recfname,rec.surname AS recsname 
FROM cd.members mem 
LEFT OUTER JOIN cd.members rec ON rec.memid = mem.recommendedby 
ORDER BY memsname,memfname
-- How can you produce a list of all members who have used a tennis court? Include in your output the name of the court, and the name of the member formatted as a single column. 
-- Ensure no duplicate data, and order by the member name. 
SELECT DISTINCT CONCAT(firstname,' ',surname) AS member,cd.facilities.name FROM cd.members
INNER JOIN cd.bookings ON cd.members.memid = cd.bookings.memid
INNER JOIN cd.facilities ON cd.bookings.facid = cd.facilities.facid
WHERE cd.facilities.name LIKE 'Tennis Court%'
ORDER BY member
-- How can you produce a list of bookings on the day of 2012-09-14 which will cost the member (or guest) more than $30? Remember that guests have different costs to members 
-- (the listed costs are per half-hour 'slot'), and the guest user is always ID 0. Include in your output the name of the facility, 
-- the name of the member formatted as a single column, and the cost. Order by descending cost, and do not use any subqueries. 
SELECT CONCAT(cd.members.firstname,' ',cd.members.surname) AS member,
	cd.facilities.name AS facility,
	CASE
		WHEN cd.members.memid = 0 THEN
			cd.bookings.slots * cd.facilities.guestcost
		
		ELSE 
			cd.bookings.slots * cd.facilities.membercost
	END AS cost
	
	FROM cd.members
	  INNER JOIN cd.bookings ON cd.members.memid = cd.bookings.memid
	  INNER JOIN cd.facilities ON cd.bookings.facid = cd.facilities.facid
	  
	  WHERE cd.bookings.starttime >= '2012-09-14'
	  AND cd.bookings.starttime < '2012-09-15'
	  AND (
			(cd.members.memid = 0 AND cd.bookings.slots * cd.facilities.guestcost > 30)
		  	or (cd.members.memid != 0 AND cd.bookings.slots * cd.facilities.membercost > 30)
		  )
ORDER BY cost DESC;
-- How can you output a list of all members, including the individual who recommended them (if any), 
-- without using any joins? Ensure that there are no duplicates in the list, and that each firstname + surname 
-- pairing is formatted as a column and ordered. 
SELECT DISTINCT CONCAT(mem.firstname,' ',mem.surname) AS member,
	(SELECT CONCAT(rec.firstname,' ',rec.surname) AS recommender FROM cd.members rec
		WHERE rec.memid = mem.recommendedby)
FROM cd.members mem
ORDER BY member
-- The Produce a list of costly bookings exercise contained some messy logic: we had to calculate the booking 
-- cost in both the WHERE clause and the CASE statement. Try to simplify this calculation using subqueries. 
-- For reference, the question was:
SELECT member,facility,cost FROM(
  SELECT CONCAT(cd.members.firstname,' ',cd.members.surname) AS member,
	cd.facilities.name AS facility,
	CASE
		WHEN cd.members.memid = 0 THEN
			cd.bookings.slots * cd.facilities.guestcost
		
		ELSE 
			cd.bookings.slots * cd.facilities.membercost
	END AS cost
	
	FROM cd.members
	  INNER JOIN cd.bookings ON cd.members.memid = cd.bookings.memid
	  INNER JOIN cd.facilities ON cd.bookings.facid = cd.facilities.facid
	  
	  WHERE cd.bookings.starttime >= '2012-09-14'
	  AND cd.bookings.starttime < '2012-09-15'
	  AND (
			(cd.members.memid = 0 AND cd.bookings.slots * cd.facilities.guestcost > 30)
		  	or (cd.members.memid != 0 AND cd.bookings.slots * cd.facilities.membercost > 30)
		  )
 )AS new_table
 ORDER BY cost DESC