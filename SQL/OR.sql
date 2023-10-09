CREATE TABLE GymClassSchedule (
    ClassID INT PRIMARY KEY,
    ClassName VARCHAR(50),
    InstructorName VARCHAR(50),
    StartTime TIME,
    EndTime TIME,
    DayOfWeek VARCHAR(15)
);

-- Inserting sample class schedule data
INSERT INTO GymClassSchedule (ClassID, ClassName, InstructorName, StartTime, EndTime, DayOfWeek)
VALUES
    (1, 'Yoga', 'Alice Instructor', '08:00:00', '09:00:00', 'Monday'),
    (2, 'Spin', 'Bob Instructor', '12:00:00', '13:00:00', 'Wednesday'),
    (3, 'Zumba', 'Charlie Instructor', '18:30:00', '19:30:00', 'Friday'),
    (4, 'Bootcamp', 'David Instructor', '10:00:00', '11:00:00', 'Tuesday'),
    (5, 'Pilates', 'Eva Instructor', '17:00:00', '18:00:00', 'Thursday');
    
SELECT *
FROM GymClassSchedule
WHERE dayofweek = 'Monday' OR dayofweek = 'Wednesday';

SELECT *
FROM GymClassSchedule
WHERE instructorname = 'Alice Instructor' OR instructorname = 'David Instructor';

SELECT *
FROM GymClassSchedule
WHERE starttime < '09:00:00' OR endtime > '17:00:00';

SELECT *
FROM GymClassSchedule
WHERE dayofweek = 'Friday' OR (endtime - starttime) > '01:00:00';