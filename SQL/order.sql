CREATE TABLE Attendance (
    AttendanceID INT PRIMARY KEY,
    MemberID INT,
    AttendanceDate DATE,
    IsPresent BOOLEAN
);

-- Inserting sample attendance data
INSERT INTO Attendance (AttendanceID, MemberID, AttendanceDate, IsPresent)
VALUES
    (1, 1, '2023-01-10', TRUE),
    (2, 2, '2023-01-10', FALSE),
    (3, 3, '2023-01-11', TRUE),
    (4, 4, '2023-01-11', TRUE),
    (5, 5, '2023-01-12', FALSE),
    (6, 1, '2023-01-12', TRUE),
    (7, 2, '2023-01-13', TRUE),
    (8, 3, '2023-01-13', FALSE),
    (9, 4, '2023-01-14', TRUE),
    (10, 5, '2023-01-14', TRUE);
    
    SELECT *
    FROM Attendance
    ORDER by attendancedate ASC
   
    SELECT *
    FROM Attendance
    WHERE memberid = 2
    ORDER by attendancedate DESC
        
    SELECT *
    FROM Attendance
    ORDER by memberid, attendancedate DESC
    
    SELECT *
    FROM Attendance
	LIMIT 4
    