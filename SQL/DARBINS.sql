CREATE TABLE movies(
  name TEXT,
  genre TEXT,
  year INTEGER
);

SELECT name, genre FROM movies

SELECT * FROM movies 

INSERT INTO movies(name, genre, year)
VALUES('balls too deep','comic', 2005);
INSERT INTO movies(name, genre, year)
VALUES('titanic','drama', 1997);
INSERT INTO movies(name, genre, year)
VALUES('blue blue sky','thriller', 2010);
INSERT INTO movies(name, genre, year)
VALUES('number 1','succes', 2023);
INSERT INTO movies(name, genre, year)
VALUES('IT','horror', 2014);