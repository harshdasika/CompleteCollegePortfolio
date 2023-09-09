SELECT hosp.name AS hospital_name, SUM(inv.instructions) AS total_fees
FROM hospital hosp
LEFT JOIN patient p ON hosp.name = p.hosp
LEFT JOIN (
    SELECT patient_id, SUM(fee) AS instructions
    FROM instruction
    GROUP BY patient_id
) inv ON p.id = inv.patient_id
GROUP BY hosp.name
ORDER BY total_fees DESC
LIMIT 1;