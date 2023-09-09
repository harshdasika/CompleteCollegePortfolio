SELECT h.name AS hospital_name, COUNT(*) AS num_cardiologists
FROM hospital h
JOIN physician p ON h.name = p.hosp
WHERE p.expertise = 'Cardiology'
GROUP BY h.name;