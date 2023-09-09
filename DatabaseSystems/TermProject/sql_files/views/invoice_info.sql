CREATE VIEW invoice_info AS
SELECT i.invoice_id, p.name AS patient_name, r.room_no, instr.code AS instruction_code, i.instructions,
       (r.fee + instr.fee) AS total_amount
FROM invoice i
JOIN patient p ON i.patient_id = p.id
JOIN room r ON i.room = r.room_no
JOIN instruction instr ON i.instructions = instr.code;