SELECT SUM(Transaction.amount) AS balance
FROM Bank.transaction
WHERE Transaction.account_num = '1111222233331441'
AND Transaction.tdate < '2019-09-01';