SELECT Employee.fname, Employee.lname, Employee.salary, 'Harsh Dasika'
FROM Company.employee
JOIN Department ON Employee.dno = Department.dnumber
WHERE Department.dname = 'Hardware';