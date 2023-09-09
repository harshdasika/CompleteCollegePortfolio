SELECT Customer.name
FROM Bank.customer
JOIN Account on Customer.ssn = Account.owner_ssn
JOIN Transaction on Account.number = Transaction.account_num
WHERE Transaction.type = "Deposit"
ORDER BY Transaction.amount DESC
LIMIT 1;