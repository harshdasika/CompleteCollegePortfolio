CREATE VIEW patient_info AS
SELECT p.id AS patient_id, p.name AS patient_name, p.address AS patient_address, p.p_number AS patient_phone,
       h.name AS hospital_name,
       ph.name AS physician_name, ph.expertise AS physician_expertise,
       n.name AS nurse_name
FROM patient p
JOIN hospital h ON p.hosp = h.name
LEFT JOIN physician ph ON p.hosp = ph.hosp
LEFT JOIN nurse n ON p.hosp = n.hosp;