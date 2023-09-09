SELECT Customer.name
FROM Bank.customer
JOIN Account ON Customer.ssn = Account.owner_ssn
WHERE Customer.sex = 'M' AND Account.type = 'Checking';