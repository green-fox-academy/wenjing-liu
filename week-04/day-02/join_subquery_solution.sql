
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- Joins and subqueries - PostgreSQL Exercises

-- How can you produce a list of the start times for bookings by members named 'David Farrell'?

select starttime from cd.bookings
join cd.members on cd.bookings.memid = cd.members.memid
where concat(cd.members.firstname, ' ',cd.members.surname) = 'David Farrell';


-- How can you produce a list of the start times for bookings for tennis courts, for the date '2012-09-21'? Return a list of start time and facility name pairings, ordered by the time.
select bks.starttime as start, facs.name as name from cd.facilities facs
join cd.bookings bks on facs.facid = bks.facid
where facs.facid in (0,1) and bks.starttime between '2012-09-21' and '2012-09-22'
order by bks.starttime;


-- How can you output a list of all members who have recommended another member? Ensure that there are no duplicates in the list, and that results are ordered by (surname, firstname).

select distinct cd.members.firstname, cd.members.surname from cd.members
join cd.members re_m on cd.members.memid = re_m.recommendedby
order by cd.members.surname, cd.members.firstname;

-- How can you output a list of all members, including the individual who recommended them (if any)? Ensure that results are ordered by (surname, firstname).
select cd.members.firstname as memfname, cd.members.surname as memsname, rem.firstname as recfname, rem.surname as recsname from cd.members
left join cd.members rem on rem.memid = cd.members.recommendedby
order by memsname, memfname;


-- How can you produce a list of all members who have used a tennis court? Include in your output the name of the court, and the name of the member formatted as a single column. Ensure no duplicate data, and order by the member name.

select distinct concat(members.firstname, ' ', members.surname) as member, facilities.name as facility from cd.members members
join cd.bookings bookings on members.memid = bookings.memid
join cd.facilities facilities on bookings.facid = facilities.facid
where bookings.facid in (0, 1)
order by member;

-- How can you produce a list of bookings on the day of 2012-09-14 which will cost the member (or guest) more than $30? Remember that guests have different costs to members (the listed costs are per half-hour 'slot'), and the guest user is always ID 0. Include in your output the name of the facility, the name of the member formatted as a single column, and the cost. Order by descending cost, and do not use any subqueries.

select concat(mems.firstname, ' ', mems.surname) as member, facs.name as facility,
	case when mems.memid = 0 then bks.slots*facs.guestcost
		  else bks.slots*facs.membercost
	end as cost
from cd.members mems
join cd.bookings bks on mems.memid = bks.memid
join cd.facilities facs on bks.facid = facs.facid
where bks.starttime between '2012-09-14' and '2012-09-15' and (
			(mems.memid = 0 and bks.slots*facs.guestcost > 30) or (mems.memid != 0 and bks.slots*facs.membercost > 30))
order by cost desc;


-- How can you output a list of all members, including the individual who recommended them (if any), without using any joins? Ensure that there are no duplicates in the list, and that each firstname + surname pairing is formatted as a column and ordered.

select distinct concat(mem_a.firstname, ' ', mem_a.surname) as member,
	(select concat(mem_b.firstname, ' ', mem_b.surname) as recommender from cd.members mem_b
		where mem_b.memid = mem_a.recommendedby)
from cd.members mem_a
order by member;


-- The Produce a list of costly bookings exercise contained some messy logic: we had to calculate the booking cost in both the WHERE clause and the CASE statement. Try to simplify this calculation using subqueries. For reference, the question was:
-- How can you produce a list of bookings on the day of 2012-09-14 which will cost the member (or guest) more than $30? Remember that guests have different costs to members (the listed costs are per half-hour 'slot'), and the guest user is always ID 0. Include in your output the name of the facility, the name of the member formatted as a single column, and the cost. Order by descending cost.

select member, facility, cost from
  (select concat(mems.firstname, ' ', mems.surname) as member, facs.name as facility,
    case when mems.memid = 0 then bks.slots*facs.guestcost
        else bks.slots*facs.membercost
    end as cost
  from cd.members mems
  join cd.bookings bks on mems.memid = bks.memid
  join cd.facilities facs on bks.facid = facs.facid
  where bks.starttime between '2012-09-14' and '2012-09-15') book_info
where cost > 30
order by cost desc;