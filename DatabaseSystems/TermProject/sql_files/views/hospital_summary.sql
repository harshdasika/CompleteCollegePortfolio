CREATE VIEW hospital_summary AS
SELECT h.name AS hospital_name,
       COUNT(DISTINCT ph.phys_id) AS total_physicians,
       COUNT(DISTINCT n.nurse_id) AS total_nurses,
       COUNT(DISTINCT p.id) AS total_patients
FROM hospital h
LEFT JOIN physician ph ON h.name = ph.hosp
LEFT JOIN nurse n ON h.name = n.hosp
LEFT JOIN patient p ON h.name = p.hosp
GROUP BY h.name;

