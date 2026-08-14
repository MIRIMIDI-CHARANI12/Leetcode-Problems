# Write your MySQL query statement below
select e.employee_id
from Employees as e
left join Salaries as s
on e.employee_id=s.employee_id
where s.salary is null
UNION
select s.employee_id
from Employees as e
right join Salaries as s
on e.employee_id=s.employee_id
where e.name is null
order by employee_id;