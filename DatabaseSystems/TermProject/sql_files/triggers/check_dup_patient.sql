DELIMITER //
CREATE TRIGGER check_dup_patient
BEFORE INSERT ON patient
FOR EACH ROW
BEGIN
    IF EXISTS (SELECT 1 FROM patient WHERE id = NEW.id) THEN
        SIGNAL SQLSTATE '45000'
    END IF;
END;
//
DELIMITER ;