SELECT Customer.name
FROM Bank.customer
JOIN Account ON Customer.ssn = Account.owner_ssn
JOIN Transaction ON Account.number = Transaction.account_num
WHERE Transaction.amount >= 1000;