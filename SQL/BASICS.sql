SELECT * FROM celebs



INSERT INTO celebs(id, name, age, twiter)
VALUES (1, 'Justin Bieber', 22, 'balls to deep');
INSERT INTO celebs(id, name, age, twiter)
VALUES (2, 'XQC', 24, 'hellnaa');
INSERT INTO celebs(id, name, age, twiter)
VALUES (3, 'Kristers', 18, 'yikes');
INSERT INTO celebs(id, name, age, twiter)
VALUES (5, 'Yappin', 22, 'I hate that');

SELECT name FROM celebs;

DELETE FROM celebs;

UPDATE celebs

SET twitter = '@taylor'
WHERE id = 3 OR name = "lolW";

ALTER TABLE celebs
ADD COLUMN twiter TEXT;

DELETE FROM celebs
WHERE agfe IS 22


SELECT * FROM awards

INSERT into awards(id, recipient, award_name)
VALUES(3, "DABBAY", "Oscar");

DELETE FROM awards
WHERE award_name IS "Oscar"


