CREATE TABLE WorkoutRating (
    RatingID INT PRIMARY KEY,
    MemberID INT,
    ExerciseID INT,
    Rating INT
);

-- Inserting sample workout rating data
INSERT INTO WorkoutRating (RatingID, MemberID, ExerciseID, Rating)
VALUES
    (1, 1, 1, 4),
    (2, 1, 2, 5),
    (3, 2, 1, 3),
    (4, 2, 3, 4),
    (5, 3, 2, 5),
    (6, 3, 3, 2),
    (7, 4, 1, 5),
    (8, 4, 2, 4),
    (9, 5, 1, 3),
    (10, 5, 3, 5);
    
SELECT rating,
CASE
	WHEN rating < 3 THEN "pretty bad"
    ELSE "I mean its alright"
END AS "score"
FROM WorkoutRating;