CREATE VIEW patient_health_status AS
SELECT p.id AS patient_id, p.name AS patient_name, p.hosp AS hospital_name,
       hr.disease AS latest_disease, hr.status AS latest_status, hr.description AS latest_description
FROM patient p
LEFT JOIN healthrecord hr ON p.id = hr.patient_id
WHERE (hr.patient_id, hr.date) IN
    (SELECT patient_id, MAX(date) FROM healthrecord 
    GROUP BY patient_id);

