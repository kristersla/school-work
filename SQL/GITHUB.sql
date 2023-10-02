CREATE table friends(
  id INTEGER,
  name TEXT,
  birthday DATE
);

SELECT * FROM friends

INSERT INTO friends(id, name, birthday)
VALUES(1, 'Ororo Munroe', '30/05/1940');
INSERT INTO friends(id, name, birthday)
VALUES(2, 'Gorge Wittek', '05/06/2005');
INSERT INTO friends(id, name, birthday)
VALUES(3, 'Baca', '02/07/1996'); 


UPDATE friends
SET name = 'Strom'
WHERE id = 1;

ALTER TABLE friends
ADD COLUMN email;

UPDATE friends
SET email = 'storm@codecademy.com'

DELETE FROM friends
WHERE id = 1;

DELETE FROM friends