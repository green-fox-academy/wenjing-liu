/*
Where is this weather station?
*/
select country_code, lat, long from weather_station where id='724940:23234';


/*
Show the temperature for June 1st, 2008.
*/

select hour, temperature from raw_weather_data where wsid='724940:23234' and year=2008 and month=6 and day=1;

/*
Show the temperatures for June 1st, 2008 from 9AM to 3PM.
*/
select hour, temperature from raw_weather_data where wsid='724940:23234' and year=2008 and month=6 and day=1 and hour>= 9 and hour<=15;

/*
What is the average elevation of the weather stations in Indiana?
*/

create index state_code_ket on weather_station(state_code);
select avg(elevation) from weather_station where state_code='IN';

/*
What is the latitude of the northest weather station in Texas?
*/
select max(long) from weather_station where state_code='TX';

/*
Insert the current temperature for today.
*/

Insert into raw_weather_data(wsid, year, month, day, hour, temperature, dewpoint, pressure, wind_direction, wind_speed, sky_condition, sky_condition_text, one_hour_precip, six_hour_precip) values ('724940:23234', 2019, 6, 4, 17, 16.1, 11.1, 1012.3, 250, 3.6, 0, null, 0, 0);

/*
Fill the daily_aggregate_temperature table.
*/

select wsid, year, day, max(temperature), min(temperature), avg(temperature), avg(dewpoint) from raw_weather_data GROUP BY wsid, year, month, day;

INSERT INTO daily_aggregate_temperature
select wsid, year, month, day, max(temperature), min(temperature), avg(temperature), avg(dewpoint), avg(dewpoint) from raw_weather_data GROUP BY wsid, year, month, day;


select wsid, year, month, day, max(temperature), min(temperature), avg(temperature), avg(dewpoint), avg(dewpoint) from raw_weather_data GROUP BY wsid, year, month, day;