SELECT patient_name, SUM(total_amount) * 0.8 AS patient_amount_to_pay
FROM invoice_info
GROUP BY patient_name;