CREATE TABLE GymMember (
    MemberID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    Phone VARCHAR(15)
);

-- Inserting sample member data
INSERT INTO GymMember (MemberID, FirstName, LastName, Email, Phone)
VALUES
    (1, 'John', 'Doe', 'john.doe@example.com', '555-1234'),
    (2, 'Jane', 'Smith', 'jane.smith@example.com', '555-5678'),
    (3, 'Alipce', 'Johnson', 'alice.j@example.com', '555-9876'),
    (4, 'Bob', 'Brown', 'bob.b@example.com', '555-4321'),
    (5, 'Eva', 'White', 'eva.white@example.com', '555-8765');
    
SELECT *
FROM GymMember
WHERE firstname LIKE '%p%';

SELECT *
FROM GymMember
WHERE lastname LIKE '%on';

SELECT *
FROM GymMember
WHERE email LIKE '%.j%';

SELECT *
FROM GymMember
WHERE phone LIKE '%5-5%';