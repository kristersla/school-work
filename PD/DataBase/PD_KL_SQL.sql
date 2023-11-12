CREATE TABLE Owner (
    OwnerID INT PRIMARY KEY,
    Name TEXT,
    Contact_Info TEXT
);

CREATE TABLE Pets (
    PetID INT PRIMARY KEY,
    Species TEXT,
    Name TEXT
);

CREATE TABLE Pet_Owner (
    PetID INT UNIQUE,
    OwnerID INT,
    PRIMARY KEY (PetID),
    FOREIGN KEY (OwnerID) REFERENCES Owner(OwnerID),
    FOREIGN KEY (PetID) REFERENCES Pets(PetID)
);

CREATE TABLE Staff (
    StaffID INT PRIMARY KEY,
    Role TEXT,
    Name TEXT
);

CREATE TABLE Specialize (
    SpecializeID INT PRIMARY KEY,
    Specialize_In TEXT
);

CREATE TABLE Services (
    ServiceID INT PRIMARY KEY,
    Type_Of_Service TEXT,
    Price FLOAT
);

CREATE TABLE Staff_Specialize (
    SpecializeID INT,
    StaffID INT,
    Type_Of_Service TEXT,
    PRIMARY KEY (SpecializeID, StaffID),
    FOREIGN KEY (SpecializeID) REFERENCES Specialize(SpecializeID),
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID),
    FOREIGN KEY (Type_Of_Service) REFERENCES Services(Type_Of_Service)
);

CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY,
    PetID INT,
    ServiceID INT,
    StaffID INT,
    DateAndTime DATETIME,
    FOREIGN KEY (PetID) REFERENCES Pets(PetID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID),
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID)
);
