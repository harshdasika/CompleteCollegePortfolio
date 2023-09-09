SELECT Account.number, Account.open_date, Account.type
FROM Bank.account
JOIN Customer ON Account.owner_ssn = Customer.ssn
WHERE Customer.name = 'Alexander Felix';