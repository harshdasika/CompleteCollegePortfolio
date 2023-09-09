SELECT name AS patient_name
FROM patient
WHERE id IN (
    SELECT patient_id
    FROM healthrecord
    WHERE status = 'Critical'
);

