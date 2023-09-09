SELECT Employee.fname, Employee.lname, Employee.salary, 'Harsh Dasika'
FROM Company.employee
JOIN Project ON Employee.dno = Project.dnum
JOIN Works_on ON Project.pnumber = Works_on.pno
WHERE Project.pname = 'ProductX';
