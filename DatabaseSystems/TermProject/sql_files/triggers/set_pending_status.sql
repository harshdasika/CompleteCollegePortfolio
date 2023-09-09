DELIMITER //
CREATE TRIGGER set_pending_status
AFTER INSERT ON patient
FOR EACH ROW
BEGIN
    INSERT INTO healthrecord (record_id, patient_id, disease, date, status, description)
    VALUES (NULL, NEW.id, 'Not confirmed', DATE(NOW()), 'Pending', 'Diagnosis not available yet');
END;
//
DELIMITER ;