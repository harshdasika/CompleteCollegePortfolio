START TRANSACTION;

INSERT INTO patient (id, name, address, p_number, hosp)
VALUES (6, 'Isabella Garcia', '123 Main St, Chicago', '312-555-7890', 'UChicago Medicine');

INSERT INTO healthrecord (record_id, patient_id, disease, date, status, description)
VALUES (8, 6, 'Asthma', '2023-07-28', 'Stable', 'Diagnosed with asthma');

COMMIT;