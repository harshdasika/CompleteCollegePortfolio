SELECT Customer.name
FROM Bank.customer
WHERE Customer.ssn IN (
    SELECT Account.owner_ssn
    FROM Bank.account
    WHERE Account.number IN (
        SELECT Transaction.account_num
        FROM Bank.transaction
        WHERE Transaction.amount >= 1000
    )
);