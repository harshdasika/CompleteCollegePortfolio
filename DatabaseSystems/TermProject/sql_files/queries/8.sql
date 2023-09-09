SELECT SUM(amount) AS Total, AVG(amount) AS Average
FROM Hospital.payments
WHERE Payments.patient_id IN (
    SELECT Patient.id 
    FROM Hospital.patient 
    WHERE Patient.hosp = 'Northwestern Memorial'
);
