SELECT SUM(amount) AS TotalFromCrit
FROM (
    SELECT Healthrecord.patient_id, Payments.amount
    FROM Hospital.healthrecord
    JOIN Payments on Healthrecord.patient_id = Payments.patient_id
    WHERE Healthrecord.status = 'Critical'
) as sumCritical;

