-- Create the tables by importing the necessary file source 'create-timeseries.cql';
source 'C:\Users\Angela_Shi\Desktop\angela\week5\day-02\data\create-timeseries.cql';
-- Load the file from the load-timeseries.cql
source 'C:\Users\Angela_Shi\Desktop\angela\week5\day-02\data\load-timeseries.cql';
-- Check if the tables are created
desc tables
-- Switch to the newly created keyspace
use isd_weather_data;
-- Check you tables
desc tables
-- Check the structure of the weather_station table
desc weather_station;
-- Now copy some data to the database
COPY raw_weather_data (wsid, year, month, day, hour, temperature, dewpoint, pressure, wind_direction, wind_speed, sky_condition, one_hour_precip, six_hour_precip)
                ... FROM 'C:\Users\Angela_Shi\Desktop\angela\week5\day-02\data\2014.csv';

-----------------------------------------------------------------------
SELECT hour, temperature
FROM raw_weather_data
WHERE wsid = '724940:23234'
LIMIT 5;

hour | temperature
------+-------------
   23 |        11.7
   22 |        12.2
   21 |        12.2
   20 |        11.7
   19 |        11.1

-------------------------------------------------------------------------

-- Questions

-- Q1:Where is this weather station?
select country_code from weather_station where id = '724940:23234';

 country_code
--------------
           US

-- Q1:Show the temperature for June 1st, 2008
select temperature from raw_weather_data where wsid = '724940:23234'
and year = 2008 and month = 6 and day = 1 allow filtering;

 temperature
-------------
          15
          15
        15.6
          15
          15
        14.4
        13.3
        12.2
        11.7
        10.6
          10
          10
        10.6
        11.1
        11.1
           0
        11.7
        11.7
        11.7
        11.7
        11.7
        12.2
        12.8
        13.3

(24 rows)

-- Show the temperatures for June 1st, 2008 from 9AM to 3PM.
select temperature from raw_weather_data where wsid = '724940:23234' and year = 2008 and month = 6 
and day = 1 and hour >= 9 and hour <= 15 allow filtering;

 temperature
-------------
        11.7
        10.6
          10
          10
        10.6
        11.1
        11.1

(7 rows)

-- What is the average elevation of the weather stations in Indiana?
select avg(elevation) from weather_station where state_code = 'IN' allow filtering;

 system.avg(elevation)
-----------------------
             213.85122

-- What is the latitude of the northest weather station in Texas?
SELECT max(lat) FROM weather_station WHERE state_code = 'TX' ALLOW FILTERING;

 system.max(lat)
-----------------
          36.017

-- Insert the current temperature for today.
INSERT INTO raw_weather_data (wsid, year, month, day, hour, temperature) VALUES ('shenzhen', 2019, 6, 5, 20,32);

select * from raw_weather_data where wsid = 'shenzhen';

 wsid     | year | month | day | hour | dewpoint | one_hour_precip | pressure | six_hour_precip | sky_condition | sky_condition_text | temperature | wind_direction | wind_speed
----------+------+-------+-----+------+----------+-----------------+----------+-----------------+---------------+--------------------+-------------+----------------+------------
 shenzhen | 2019 |     6 |   5 |   20 |     null |            null |     null |            null |          null |               null |          32 |           null |       null

