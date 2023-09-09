SELECT COUNT(*) AS total_num_deposits
FROM Bank.transaction
WHERE Transaction.type = 'Deposit';