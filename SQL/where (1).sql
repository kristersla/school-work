CREATE TABLE WorkoutLog (
    LogID INT PRIMARY KEY,
    ExerciseID INT,
    WorkoutDate DATE,
    Sets INT,
    Reps INT,
    Weight DECIMAL(5, 2),
    CONSTRAINT fk_ExerciseID FOREIGN KEY (ExerciseID) REFERENCES Exercise(ExerciseID)
);

-- Inserting sample workout log data
INSERT INTO WorkoutLog (LogID, ExerciseID, WorkoutDate, Sets, Reps, Weight)
VALUES
    (1, 1, '2023-01-10', 3, 15, 0),
    (2, 2, '2023-01-10', 4, 12, 50),
    (3, 3, '2023-01-11', 3, 20, 0),
    (4, 4, '2023-01-11', 5, 8, 100),
    (5, 5, '2023-01-12', 4, 10, 0),
    (6, 6, '2023-01-12', 3, 15, 0),
    (7, 7, '2023-01-13', 4, 12, 60),
    (8, 8, '2023-01-13', 5, 8, 120),
    (9, 9, '2023-01-14', 3, 20, 0),
    (10, 10, '2023-01-14', 4, 12, 80);
    
SELECT *
FROM WorkoutLog
WHERE weight > 0 and weight <= 120;

