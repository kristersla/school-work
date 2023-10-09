CREATE TABLE GymMembership (
    MembershipID INT PRIMARY KEY,
    MemberID INT,
    StartDate DATE,
    EndDate DATE,
    IsActive BOOLEAN,
    CONSTRAINT fk_MemberID FOREIGN KEY (MemberID) REFERENCES GymMember(MemberID)
);

-- Inserting sample membership data
INSERT INTO GymMembership (MembershipID, MemberID, StartDate, EndDate, IsActive)
VALUES
    (1, 1, '2022-01-01', '2022-12-31', TRUE),
    (2, 2, '2022-02-15', '2022-11-30', TRUE),
    (3, 3, '2022-03-10', '2022-10-15', FALSE),
    (4, 4, '2022-04-20', '2022-09-30', TRUE),
    (5, 5, '2022-05-05', '2022-08-20', FALSE);
    
SELECT *
FROM GymMembership
WHERE isactive = 1 AND startdate > '2022-01-03' AND enddate < '2022-12-31';
    
SELECT *
FROM GymMembership
WHERE isactive = 0 AND startdate > '2022-05-01';

SELECT *
FROM GymMembership
WHERE startdate > '2022-01-01' AND (isactive = 1 OR enddate = '2022-08-15');

SELECT *
FROM GymMembership
WHERE startdate BETWEEN '2022-01-01' AND '2022-07-31' AND isactive = 1;

