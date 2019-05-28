---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- SQL Social-Network Query Exercises

-- Q1 Find the names of all students who are friends with someone named Gabriel.
select student.name from Highschooler student
join
(select distinct
    case when friend.id1 = Highschooler.id then friend.id2
         else friend.id1
    end as friend_id
from friend
join Highschooler on Highschooler.id = friend.id1 or Highschooler.id = friend.id2
where Highschooler.name = 'Gabriel') tmp on tmp.friend_id = student.id;

-- Q2 For every student who likes someone 2 or more grades younger than themselves, return that student's name and grade, and the name and grade of the student they like.
select stu_a.name, stu_a.grade, stu_b.name, stu_b.grade from highschooler stu_a, highschooler stu_b, likes
where likes.id1 = stu_a.id and likes.id2 = stu_b.id and stu_a.grade - stu_b.grade >= 2;

-- Q3 For every pair of students who both like each other, return the name and grade of both students. Include each pair only once, with the two names in alphabetical order.
select stu_a.name, stu_a.grade, stu_b.name, stu_b.grade from highschooler stu_a, highschooler stu_b,
(select likes.id1, likes.id2 from likes
join likes b on b.id2 = likes.id1 and  b.id1 = likes.id2
where likes.id1 < likes.id2) tmp_likes
on stu_a.id = tmp_likes.id1 and stu_b.id = tmp_likes.id2;


-- Q4 Find all students who do not appear in the Likes table (as a student who likes or is liked) and return their names and grades. Sort by grade, then by name within each grade.
select name, grade from highschooler
left join likes on highschooler.id = likes.id1 or highschooler.id = likes.id2
where likes.id1 is null and likes.id2 is null
order by grade, name;

-- Q5 For every situation where student A likes student B, but we have no information about whom B likes (that is, B does not appear as an ID1 in the Likes table), return A and B's names and grades.
select stu_a.name, stu_a.grade, stu_b.name, stu_b.grade from highschooler stu_a, highschooler stu_b,
(select likes_b.id1, likes_b.id2 from likes likes_b
left join likes likes_a on likes_b.id2 = likes_a.id1
where likes_a.id1 is null) tmp_b
where stu_a.id = tmp_b.id1 and stu_b.id = tmp_b.id2;


-- Q6 Find names and grades of students who only have friends in the same grade. Return the result sorted by grade, then by name within each grade.
select distinct stu_a.name, stu_a.grade from highschooler stu_a
join friend on stu_a.id = friend.id1
where stu_a.id not in (select stu.id from highschooler stu
join friend on stu.id = friend.id1
join highschooler stu_b on stu_b.id = friend.id2
where stu_b.grade > stu.grade or stu_b.grade < stu.grade)
order by stu_a.grade, stu_a.name;

-- Q7 For each student A who likes a student B where the two are not friends, find if they have a friend C in common (who can introduce them!). For all such trios, return the name and grade of A, B, and C.
select distinct stu_a.name, stu_a.grade, stu_b.name, stu_b.grade, stu_c.name, stu_c.grade
from Highschooler stu_a, Highschooler stu_b, Highschooler stu_c, Likes L, Friend F1, Friend F2
where (stu_a.id = L.id1 and stu_b.id = L.id2) and stu_b.id not in (
  select id2
  from Friend
  where id1 = stu_a.id
) and (stu_a.id = F1.id1 and stu_c.id = F1.id2) and (stu_b.id = F2.id2 and stu_c.id = F2.id2);


-- Q8 Find the difference between the number of students in the school and the number of different first names.
select count(*) - count(distinct name) from Highschooler;

-- Q9 Find the name and grade of all students who are liked by more than one other student.
select name, grade from Highschooler
join Likes on Highschooler.id = Likes.id2
group by id2
having COUNT(*) > 1;


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- SQL Social-Network Query Exercises Extra

-- Q1 For every situation where student A likes student B, but student B likes a different student C, return the names and grades of A, B, and C. 

select stu_a.name, stu_a.grade, stu_b.name, stu_b.grade, stu_c.name, stu_c.grade from highschooler  stu_a, highschooler stu_b, highschooler stu_c, likes like_1, likes like_2
where stu_a.id = like_1.id1 and stu_b.id = like_1.id2 and (stu_b.id = like_2.id1 and stu_c.id = like_2.id2 and stu_c.id <> stu_a.id);


-- Q2 Find those students for whom all of their friends are in different grades from themselves. Return the students' names and grades. 
select name, grade from highschooler stu_a
where grade not in (
  select stu_b.grade from friend, highschooler stu_b
  where stu_a.id = friend.id1 and stu_b.id = friend.id2
)

-- Q3 What is the average number of friends per student? (Your result should be just one number.) 

select avg(count) from (
  select count(*) as count from friend
  group by id1
)

-- Q4 Find the number of students who are either friends with Cassandra or are friends of friends of Cassandra. Do not count Cassandra, even though technically she is a friend of a friend. 
select count(*) from friend 
where id1 in (
  select id2 from friend where id1 in (
    select id from highschooler where name = 'Cassandra'
  )
)

-- Q5 Find the name and grade of the student(s) with the greatest number of friends. 
  
select name, grade from highschooler
join friend on highschooler.id = friend.id1
group by id1
having count(*) = (
  select max(count) from (
    select count(*) as count from friend group by id1
  )
)


