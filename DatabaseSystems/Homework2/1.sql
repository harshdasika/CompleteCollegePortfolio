SELECT Employee.fname, Employee.lname, 'Harsh Dasika'
FROM Company.employee
WHERE Employee.fname LIKE 'A%' AND Employee.lname LIKE 'J%'