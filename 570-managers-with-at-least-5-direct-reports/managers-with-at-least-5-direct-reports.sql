# Write your MySQL query statement below
SELECT e.name
FROM employee AS e JOIN
employee AS m
ON e.id = m.managerId
GROUP BY e.id
HAVING COUNT(m.managerId) >= 5;