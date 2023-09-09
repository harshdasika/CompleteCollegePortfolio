
-- Query 1
INSERT INTO student (name, student_number, class_year, major)
VALUES ('Harshnandan Dasika', '652855943', '2023', 'Computer Science'),
	   ('George Bush', '674589723', '2023', 'Computer Science'),
       ('Barack Obama', '648976245', '2024', 'Computer Science'),
       ('Donald Trump', '698724562', '2024', 'Computer Science');

-- Query 2
CREATE TABLE IF NOT EXISTS grade_report (
  student_number  CHAR(9) NOT NULL,
  section_identifier INT NOT NULL,
  course_number INT NOT NULL,
  grade CHAR(4),
  PRIMARY KEY (student_number)
);

-- Query 3
INSERT INTO grade_report (student_number, section_identifier, course_number, grade)
VALUES ('652855943', 1, 480, NULL);

-- Query 4
UPDATE grade_report SET grade = 'B+' WHERE student_number = '652855943' AND course_number = 480;

-- Query 5
ALTER TABLE section ADD location VARCHAR(10);

-- Query 6
UPDATE section SET location = 'BCKM 208' WHERE course_number = 480;

-- Query 7
ALTER TABLE section DROP COLUMN location;

-- Query 8
DELETE FROM grade_report WHERE student_number = '652855943';

-- Query 9
DROP TABLE if exists grade_report;

-- Query 10
TRUNCATE TABLE student;

