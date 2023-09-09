SELECT DISTINCT p.name AS patient_name, r.room_no, r.fee
FROM patient p
JOIN invoice i ON p.id = i.patient_id
JOIN room r ON i.room = r.room_no
WHERE r.fee > 300 AND r.fee < 1300;