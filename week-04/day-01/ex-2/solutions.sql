-- List the users who registered in 2018 with a `.com` email address and living in China
  
select * from users where email like '%.com' and country='China' and date_of_registration between '2018-01-01' and '2018-12-31';
  

 -- How many users are there?
select COUNT(*) from USERS;
 
  
-- How many users registered in 2019?
select COUNT(*) from USERS where date_of_registration between '2019-01-01' and '2019-12-31';


-- How many users registered in January?
select * from USERS where to_char(date_of_registration, 'YYYY-MM') like '____-01';


-- Which country has the most users?
select country, count(*) as count_users from users group by country order by count_users desc limit 1;

-- What is the gender ratio?

 select gender,  (Count(gender)*100 / (Select Count(*) From 
 users where gender='Female')) as percentage
 From users
 Where gender = 'Male'
 group By gender;


-- How many users left at least one field blank?
select count(*) as null_field_user_counter from users where
	id is null or username is null or email is null or date_of_registration is null or first_name is null or
	last_name is null or country is null or gender is null;

-- Which are the 3 most expensive products?
select * from products order by price desc limit 3;

-- Which are the 4th and 5th cheapest products?
select * from products order by price offset 3 limit 2;


-- What is the average price for an electric product?
select category, avg(price) from products where category = 'Electronics' group by category;


-- How much would it cost me to buy all the toys?
select category, sum(price) from products where category='Toys' group by category;



-- What is the average rating?
select product_id, avg(rating) as avg_rating from reviews group by product_id;

-- Which product has the best average rating?
select * from products where id in (select product_id from reviews group by product_id order by avg(rating) desc limit 1);


-- Which product has the worst rating?
select * from products where id in (select product_id from reviews group by product_id order by avg(rating) asc limit 1);

-- Which products have no review?
select * from products left join reviews on products.id = reviews.product_id where reviews.id is null;

-- How many reviews are 3 or below without comment?
select count(*) from reviews where rating <=3 or comment is null;

-- Which user reviewed the most?
select * from users where id in (select user_id from reviews group by user_id order by count(*) DESC limit 1);

-- List the average rating for each product
select * from products 
join 
	(select product_id, avg(rating) as avg_rating from reviews group by product_id) avg_re
on products.id = avg_re.product_id

-- How many days passed since the last review?
select CURRENT_DATE - date from reviews order by date desc limit 1;
