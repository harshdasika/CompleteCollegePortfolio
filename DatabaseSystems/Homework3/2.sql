SELECT Transaction.id, Transaction.amount, Transaction.tdate, Transaction.type, Transaction.account_num
FROM Bank.transaction
WHERE Transaction.account_num = '1111222233331441'
AND Transaction.tdate >= '2019-09-01' AND Transaction.tdate <= '2019-09-30';