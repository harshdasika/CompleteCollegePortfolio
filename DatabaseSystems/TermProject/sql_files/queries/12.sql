SELECT p.name AS patient_name, r.room_no, COUNT(inv.invoice_id) AS stays_count
FROM patient p
JOIN invoice inv ON p.id = inv.patient_id
JOIN room r ON inv.room = r.room_no
GROUP BY p.name, r.room_no
HAVING COUNT(inv.invoice_id) > 1;