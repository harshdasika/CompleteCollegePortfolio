SELECT Employee.fname, Employee.lname, Department.dname, Employee.salary, 'Harsh Dasika'
FROM Company.Employee
JOIN Department ON Employee.dno = Department.dnumber
WHERE Employee.salary = (SELECT MAX(Employee.salary) FROM Employee WHERE Employee.sex = 'F')
AND Employee.sex = 'F';