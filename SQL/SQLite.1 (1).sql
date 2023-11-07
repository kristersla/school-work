CREATe TABLE Customers(
  	CustomerID INTEGER PRIMARY KEY,
  	Name TEXT,
  	Email TEXT,
  	Password TEXT,
  	ShippingAddress TEXT,
  	BillingAddress TEXT
);
CREATe TABLE Products(
  	ProductID INTEGER PRIMARY KEY,
  	Name TEXT,
  	Description TEXT,
  	Price REAL,
  	StockQuantity INTEGER
);
CREATe TABLE Categories(
  	CategoryID INTEGER PRIMARY KEY,
  	Name TEXT,
  	Description TEXT
);
CREATe TABLE ProductCategories(
  	ProductID INTEGER,
  	CategoryID INTEGER,
  	FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
  	FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID)
  	PRIMARY KEY (ProductID, CategoryID)
);
CREATe TABLE Orders(
  	OrderID	INTEGER PRIMARY KEY,
  	CustomerID INTEGER,
  	OrderDate REAL,
  	Status TEXT,
  	FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);
CREATe TABLE OrderDetails(
  	OrderDetailID INTEGER PRIMARY KEY,
  	OrderID	INTEGER,
  	ProductID INTEGER,
  	Quantity INTEGER,
  	UnitPrice INTEGER,
  	FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);
CREATe TABLE Reviews(
  	ReviewID INTEGER PRIMARY KEY,
  	ProductID INTEGER,
  	CustomerID INTEGER,
  	Rating INTEGER,
  	Comment TEXT,
  	ReviewDate REAL,
  	FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
  	FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);