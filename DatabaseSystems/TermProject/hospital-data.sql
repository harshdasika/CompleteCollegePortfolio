INSERT INTO hospital (name, address)
VALUES ('Northwestern Memorial', '251 E Huron St, Chicago'),
	   ('UI Health', '1740 W Taylor St, Chicago'),
       ('Rush Medical Center', '1620 W Harrison St, Chicago'),
       ('Ascension Saint Francis', '355 Ridge Ave, Evanston'),
       ('UChicago Medicine', '5841 S Maryland Ave, Chicago');

INSERT INTO physician (phys_id, name, cert_num, expertise, address, p_number, hosp)
VALUES (1, 'Harvey Specter', 126789234, 'Neurology', '151 N Michigan Ave, Chicago', '630-456-9872', 'Northwestern Memorial'),
	   (2, 'Jessica Pearson', 345762985, 'Cardiology', '233 S Wacker Drive, Chicago', '847-597-8154', 'UI Health'),
       (3, 'Mike Ross', 679845231, 'Internal Medicine', '827 S Miller St, Chicago', '847-682-7459', 'Northwestern Memorial'),
       (4, 'Rachel Zane', 745896512, 'Dermatology', '750 S Halsted St, Chicago', '630-652-8743', 'Rush Medical Center'),
       (5, 'Louis Litt', 246781356, 'Pediatrics', '875 N Michigan Ave, Chicago', '847-498-9156', 'UChicago Medicine');

INSERT INTO nurse (nurse_id, name, cert_num, address, p_number, hosp)
VALUES (1, 'John Keen', 347689213, '34 S Hamlin Ave, Chicago', '650-288-4309', 'UI Health'),
	   (2, 'Joyce Lopez', 345762985, '12 W Damen Ave, Chicago', '678-597-7135', 'Northwestern Memorial'),
       (3, 'Elaine Harris', 679845231, '312 Mohawk St, Chicago', '518-354-6159', 'Northwestern Memorial'),
       (4, 'Tiffany Wittmer', 745896512, '153 Monroe St, Chicago', '936-890-1039', 'Ascension Saint Francis'),
       (5, 'Dolores Tatum', 246781356, '43 Devon St, Chicago', '708-955-7743', 'UChicago Medicine');
       
INSERT INTO patient (id, name, address, p_number, hosp)
VALUES (1, 'Calum Calderon', '28 Pacific Ave, Chicago', '985-918-0465', 'Northwestern Memorial'),
	   (2, 'Edwin Stone', '224 E 65th St, Chicago', '410-428-8203', 'UI Health'),
       (3, 'Rosalie Pacheco', '18 Goodrich Ln, Chicago', '312-608-5334', 'UChicago Medicine'),
       (4, 'Leonard Klein', '834 S Halsted St, Chicago', '606-785-0259', 'Northwestern Memorial'),
       (5, 'Anton Mosley', '27 S Aberdeen St, Chicago', '206-585-2999', 'Rush Medical Center');
       
INSERT INTO room (room_no, capacity, fee)
VALUES (123, 2, 1500),
	   (124, 3, 1000),
       (125, 5, 500),
       (126, 10, 200),
       (127, 20, 100);
       
INSERT INTO healthrecord (record_id, patient_id, disease, date, status, description)
VALUES (1, 1, 'Covid-19', '2023-02-26', 'Recovering', 'Contracted Covid-19, currently recovering'),
	   (2, 2, 'Coronary Artery Disease', '2022-12-02', 'Critical', 'Plaque buildup in arteries, condition critical'),
       (3, 3, 'Pneumonia', '2023-04-14', 'Stable', 'Cold turned into pneumonia, now stable'),
       (4, 4, 'Epilepsy', '2021-01-17', 'Critical', 'Medication not stopping seizures anymore'),
       (5, 5, 'Psoriasis', '2023-06-13', 'Remission', 'Symptoms vanishing, needs monitoring'),
       (6, 3, 'Covid-19', '2023-05-24', 'Stable', 'Exposed to covid'),
       (7, 4, 'Emotional changes', '2022-02-14', 'Critical', 'Experiencing intense emotions of fear, anxiety');

INSERT INTO instruction (code, fee, patient_id, description)
VALUES (423, 1000, 1, 'Keep giving meds and monitoring'),
	   (126, 14500, 2, 'Surgery required as soon as possible'),
       (349, 3000, 3, 'Give antibiotics periodically'),
       (568, 10000, 4, 'Give family the bad news urgently'),
       (942, 5000, 5, 'Keep administering Apremilast');

INSERT INTO invoice (invoice_id, patient_id, room, instructions)
VALUES (304, 1, 123, 423),
	   (592, 2, 124, 126),
       (324, 3, 125, 349),
       (876, 4, 126, 568),
       (210, 5, 127, 942),
       (305, 1, 123, 349),
       (593, 2, 124, 942);

INSERT INTO payments (patient_id, date, amount)
VALUES (1, '2023-02-27', 1000),
	   (2, '2022-12-10', 14500),
       (3, '2023-04-17', 3000),
       (4, '2021-01-23', 10000),
       (5, '2023-06-13', 5000);
       
INSERT INTO medication (patient_id, amount)
VALUES ('1', '2 tables of aspirin'),
	   ('2', '5 tables of ibuprofen'),
       ('3', 'cold bath'),
       ('4', 'herbal tea'),
       ('5', 'Tables of xanax');


