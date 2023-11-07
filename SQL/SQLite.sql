CREATE TABLE Authors (
    AuthorID INTEGER PRIMARY KEY,
    Name TEXT,
    Biography TEXT
);

CREATE TABLE Books (
    BookID INTEGER PRIMARY KEY,
    ISBN TEXT,
    Title TEXT,
    PublicationYear REAL,
    Genre TEXT
);

CREATE TABLE BookAuthors (
    BookID INTEGER,
    AuthorID INTEGER,
    PRIMARY KEY (BookID, AuthorID),
    FOREIGN KEY (BookID) REFERENCES Books(BookID),
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)
);

CREATE TABLE Copies (
    CopyID INTEGER PRIMARY KEY,
    BookID INTEGER,
    ConditionStatus INTEGER,
    FOREIGN KEY (BookID) REFERENCES Books(BookID)
);

CREATE TABLE Patrons (
    PatronID INTEGER PRIMARY KEY,
    Name TEXT,
    MembershipDate REAL
);

CREATE TABLE Loans (
    LoanID INTEGER PRIMARY KEY,
    CopyID INTEGER,
    PatronID INTEGER,
    LoanDate REAL,
    DueDate REAL,
    ReturnDate REAL,
    FOREIGN KEY (CopyID) REFERENCES Copies(CopyID),
    FOREIGN KEY (PatronID) REFERENCES Patrons(PatronID)
);