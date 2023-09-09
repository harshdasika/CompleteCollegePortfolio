SELECT p.patient_id, p.patient_name, p.hospital_name, p.latest_disease, p.latest_status,
       p.latest_description, 
       CASE WHEN p.latest_status = 'Critical' THEN 0 ELSE i.total_amount END AS total_amount_to_pay
FROM patient_health_status p
LEFT JOIN invoice_info i ON p.patient_name = i.patient_name;