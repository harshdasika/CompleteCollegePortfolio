SELECT p.name AS patient_name, h.disease
FROM patient p
JOIN healthrecord h ON p.id = h.patient_id;