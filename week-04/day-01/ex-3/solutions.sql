-- Create the necessary tables and maybe add the necessary fields
create table employees (
 id  serial primary key,
 username char(50) not null,
 first_name varchar(50),
 last_name varchar(50),
 date_of_employment date not null,
 date_of_exit date,
 role char(50),
 salary float
);

-- Alter the existing tables so that an employee belongs to a department as well
alter table employees
add column department varchar(100);

-- Remove the username field from the table
alter table employees
drop column username;

-- Rename a column
alter table employees
rename first_name to nik_name;