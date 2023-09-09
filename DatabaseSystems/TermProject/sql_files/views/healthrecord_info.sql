CREATE VIEW healthrecord_info AS
SELECT h.record_id, p.name AS patient_name, h.disease, h.date, h.status, h.description
FROM healthrecord h
JOIN patient p ON h.patient_id = p.id;

