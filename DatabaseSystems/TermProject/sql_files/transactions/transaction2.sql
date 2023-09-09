START TRANSACTION;

UPDATE patient
SET p_number = '312-555-1234'
WHERE id = 3;

INSERT INTO payments (patient_id, date, amount)
VALUES (3, '2023-07-28', 1500);

COMMIT;

