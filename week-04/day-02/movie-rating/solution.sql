---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- SQL Movie-Rating Query Exercises

-- Q1 Find the titles of all movies directed by Steven Spielberg.
select title from Movie where director = 'Steven Spielberg';

-- Q2 Find all years that have a movie that received a rating of 4 or 5, and sort them in increasing order.
select distinct year from movie
join rating on movie.mid = rating.mid
where rating.stars between 4 and 5
order by year;

-- Q3 Find the titles of all movies that have no ratings.
select title from movie
left join rating on movie.mid = rating.mid
where rating.mid is null;

-- Q4 Some reviewers didn't provide a date with their rating. Find the names of all reviewers who have ratings with a NULL value for the date.
select reviewer.name from reviewer
join rating on reviewer.rid = rating.rid
where rating.ratingDate  is null;

-- Q5 Write a query to return the ratings data in a more readable format: reviewer name, movie title, stars, and ratingDate. Also, sort the data, first by reviewer name, then by movie title, and lastly by number of stars.

select reviewer.name as reviewer_name, movie.title as movie_title, rating.stars as stars, rating.ratingDate as date from
rating
join reviewer on rating.rid = reviewer.rid
join movie on rating.mid = movie.mid
order by reviewer_name, movie_title, stars;

-- Q6 For all cases where the same reviewer rated the same movie twice and gave it a higher rating the second time, return the reviewer's name and the title of the movie.
select reviewer.name, movie.title from
(select ra_a.mid, ra_a.rid from rating ra_a
join rating ra_b on ra_a.rid = ra_b.rid and ra_a.mid = ra_b.mid and ra_a.ratingDate > ra_b.ratingDate and ra_a.stars > ra_b.stars) tmp
join movie on tmp.mid = movie.mid
join reviewer on reviewer.rid = tmp.rid;

-- Q7 For each movie that has at least one rating, find the highest number of stars that movie received. Return the movie title and number of stars. Sort by movie title.
select movie.title as title, tmp_rating.stars as stars from movie
join (select rating.mID, max(stars) as stars from rating group by rating.mID ) tmp_rating on movie.mID  = tmp_rating.mID
order by title;

-- Q8 For each movie, return the title and the 'rating spread', that is, the difference between highest and lowest ratings given to that movie. Sort by rating spread from highest to lowest, then by movie title.
select movie.title as title, max_rating.stars - min_rating.stars as rating_spread from
    (select mid, max(stars) as stars from rating group by mid) max_rating
join (select mid, min(stars) as stars from rating group by mid) min_rating
on max_rating.mid = min_rating.mid
join movie on max_rating.mid = movie.mid
order by rating_spread desc, title;


-- Q9 Find the difference between the average rating of movies released before 1980 and the average rating of movies released after 1980. (Make sure to calculate the average rating for each movie, then the average of those averages for movies before 1980 and movies after. Don't just calculate the overall average rating before and after 1980.)

select
(select sum(stars)/count(*) from (select movie.mid, movie.year, tmp_rating.stars as stars from movie
join (select mid, avg(stars) as stars from rating group by mid) tmp_rating on tmp_rating.mid = movie.mid) tmp_movie
where tmp_movie.year < 1980)
-
(select sum(stars)/count(*) from (select movie.mid, movie.year, tmp_rating.stars as stars from movie
join (select mid, avg(stars) as stars from rating group by mid) tmp_rating on tmp_rating.mid = movie.mid) tmp_movie
where tmp_movie.year >= 1980);



------------------------------------------------------------------------------------------------
-- SQL Movie-Rating Query Exercises extra


-- Q1 Find the names of all reviewers who rated Gone with the Wind. 
select name from reviewer
join rating on rating.rid = reviewer.rid
join movie on rating.mid = movie.mid
where movie.title = 'Gone with the Wind';

-- Q2 For any rating where the reviewer is the same as the director of the movie, return the reviewer name, movie title, and number of stars. 
select reviewer.name, movie.title, rating.stars from reviewer
join rating on reviewer.rid = rating.rid
join movie on rating.mid = movie.mid
where reviewer.name = movie.director;

-- Q3 Return all reviewer names and movie names together in a single list, alphabetized. (Sorting by the first name of the reviewer and first word in the title is fine; no need for special processing on last names or removing "The".) 
select reviewer.name as reviewer_name, movie.title as moive_title from reviewer
full join rating on reviewer.rid = rating.rid
full join movie on rating.mid = movie.mid
order by reviewer.name asc, movie.title asc;


-- Q4 Find the titles of all movies not reviewed by Chris Jackson. 
select distinct movie.title from movie
left join rating on movie.mid = rating.mid
left join reviewer on reviewer.rid = rating.rid
where reviewer.name != 'Chris Jackson';

-- Q5 For all pairs of reviewers such that both reviewers gave a rating to the same movie, return the names of both reviewers. Eliminate duplicates, don't pair reviewers with themselves, and include each pair only once. For each pair, return the names in the pair in alphabetical order. 
select distinct concat(rating.rid, '_', secound_rating.rid) as pair_ids, first_reviewer.name as first_reviewer, second_reviewer.name as second_reviewer from rating 
join rating as secound_rating on rating.mid = secound_rating.mid
join reviewer as first_reviewer on first_reviewer.rid = rating.rid
join reviewer as second_reviewer on second_reviewer.rid = secound_rating.rid
where rating.rid != secound_rating.rid and rating.rid < secound_rating.rid;


-- Q6 For each rating that is the lowest (fewest stars) currently in the database, return the reviewer name, movie title, and number of stars. 
select reviewer.name, movie.title, rating.stars from rating
join reviewer on reviewer.rid = rating.rid
join movie on movie.mid = rating.mid
order by rating.stars asc limit 1;

-- Q7 List movie titles and average ratings, from highest-rated to lowest-rated. If two or more movies have the same average rating, list them in alphabetical order.
select movie.title, avg_table.avg_star from movie
join (select rating.mid, avg(rating.stars) as avg_star from rating
join movie on movie.mid = rating.mid
group by rating.mid) avg_table on avg_table.mid = movie.mid
order by avg_table.avg_star desc, movie.title;


-- Q8 Find the names of all reviewers who have contributed three or more ratings. (As an extra challenge, try writing the query without HAVING or without COUNT.) 
select reviewer.name from reviewer
join rating on reviewer.rid = rating.rid
group by reviewer.name
having count(reviewer.name) < 3;

-- Q9 Some directors directed more than one movie. For all such directors, return the titles of all movies directed by them, along with the director name. Sort by director name, then movie title. (As an extra challenge, try writing the query both with and without COUNT.) 
select movie.title, director.director from movie
join movie director on movie.director = director.director and movie.mid !=director.mid
order by director.director, movie.title;

-- Q10 Find the movie(s) with the highest average rating. Return the movie title(s) and average rating. (Hint: This query is more difficult to write in SQLite than other systems; you might think of it as finding the highest average rating and then choosing the movie(s) with that average rating.) 
select movie.title, avg_table.avg_rating from movie
join (select mid, avg(stars) as avg_rating from rating group by mid) avg_table on movie.mid = avg_table.mid
order by avg_table.avg_rating desc limit 1;


-- Q11 Find the movie(s) with the lowest average rating. Return the movie title(s) and average rating. (Hint: This query may be more difficult to write in SQLite than other systems; you might think of it as finding the lowest average rating and then choosing the movie(s) with that average rating.) 
select movie.title, avg_table.avg_rating from movie
join (select mid, avg(stars) as avg_rating from rating group by mid) avg_table on movie.mid = avg_table.mid
order by avg_table.avg_rating asc limit 1;

-- Q12 For each director, return the director's name together with the title(s) of the movie(s) they directed that received the highest rating among all of their movies, and the value of that rating. Ignore movies whose director is NULL. 
(select movie.mid, movie.title, movie.director, avg_tmp.avg from movie 
left join (select mid, avg(stars) from rating group by mid) avg_tmp on movie.mid = avg_tmp.mid
where movie.director is not null)  a
join (select director, max(avg) as avg from (select movie.mid, movie.title, movie.director, avg_tmp.avg from movie 
left join (select mid, avg(stars) from rating group by mid) avg_tmp on movie.mid = avg_tmp.mid
where movie.director is not null)  tmp group by director) b on a.director = b.director and a.avg = b.avg;


-- Create a view where you display the reviewer's name and the amount of their review
create view review_counter as 
(select reviewer.name, tmp.count from reviewer
  join (select rating.rid, count(rating.rid) from rating group by rating.rid) tmp
  on reviewer.rid = tmp.rid);
-- Create a view where you display the movies which have no review
create view no_review_movie as
select * from movie where movie.mid not in (select rating.mid from rating group by mid);

-- Create a view where you display all the directors (do not include null values)
create view all_directors as
select distinct director from movie where director is not null;

-- Create a view where you display the movie title and the average rating
create view avg_rating_movie as select movie.title, tmp.avg from movie 
join (select rating.mid, avg(rating.stars) from rating
group by rating.mid) tmp on movie.mid = tmp.mid;





