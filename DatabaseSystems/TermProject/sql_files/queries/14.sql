SELECT patient_name, SUM(total_amount) AS total_amount_for_patient
FROM invoice_info
GROUP BY patient_name;

