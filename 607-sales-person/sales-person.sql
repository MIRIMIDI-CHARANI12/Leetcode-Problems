# Write your MySQL query statement below
SELECT s.name
FROM SalesPerson s
left join Orders as o 
on s.sales_id=o.sales_id
left join Company as c
on o.com_id=c.com_id
group by s.name
having sum(c.name="RED")=0
or sum(c.name="RED") is null;