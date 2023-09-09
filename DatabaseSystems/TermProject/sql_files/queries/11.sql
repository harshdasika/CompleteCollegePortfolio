SELECT DISTINCT p.name AS patient_name, hr.disease AS treated_disease
FROM patient p
JOIN healthrecord hr ON p.id = hr.patient_id
JOIN physician ph ON p.hosp = ph.hosp
GROUP BY p.id, hr.disease
HAVING COUNT(DISTINCT ph.phys_id) > 1;

