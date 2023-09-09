SELECT p.name AS patient_name, SUM(amount) AS total_payment
FROM patient p
JOIN payments pm ON p.id = pm.patient_id
GROUP BY p.name
ORDER BY total_payment DESC
LIMIT 1;