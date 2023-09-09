SELECT SUM(Works_on.hours) AS total_PX_worked_hours, 'Harsh Dasika'
FROM Company.Works_on
JOIN Project ON Works_on.pno = Project.pnumber
WHERE Project.pname = 'ProductX';
