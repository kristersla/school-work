CREATE TABLE Author(
  	AuthorID KEY,
  	Name TEXT,
  	Biography TEXT
);
  
CREATE TABLE AuthorBooks(
  	BookID INTEGER,
  	AuthorID INTEGER
);
  
CREATE TABLE Books(
    BookID Key,
    ISBN INTEGER,
    Title TEXT
	PublicationDate REAL,
    Genre TEXT
);

CREATE TABLE Copies(
 	CopyID KEY,
  	BooksID INTEGER,
  	ConditionStatus TEXT
);
CREATE TABLE Patrons(
  PatronID KEy,
  Name TEXT,
  MembershipDate REAL
);
CREATE TABLE Loans(
  	LoanID KEY,
  	CopyID INTEGER,
  	PatronID INTEGER,
  	LoanDate REAl,
  	DueDate REAL,
  	ReturnDate REAL
);

    
   