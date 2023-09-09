DELIMITER //
CREATE TRIGGER new_invoice AFTER INSERT ON healthrecord
FOR EACH ROW
BEGIN
    INSERT INTO invoice (patient_id, room, instructions)
    VALUES (NEW.patient_id, (SELECT MAX(room_no) FROM room), (SELECT MAX(code) FROM instruction WHERE patient_id = NEW.patient_id));
END;
//
DELIMITER ;


