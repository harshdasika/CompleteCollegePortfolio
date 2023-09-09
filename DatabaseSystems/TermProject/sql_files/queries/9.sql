SELECT AVG(avg_payment) AS average_payment_multiple_records
FROM (
    SELECT patient_id, AVG(amount) AS avg_payment
    FROM payments
    WHERE patient_id IN (
        SELECT patient_id
        FROM healthrecord
        GROUP BY patient_id
        HAVING COUNT(*) > 1
    )
    GROUP BY patient_id
) AS multiple_records_payments;

