schema_script = """
-- Create the User_Roles table

CREATE TABLE User_Roles (
    Id SERIAL PRIMARY KEY,
    Role_Name VARCHAR(255)
);

-- Create the Countries table

CREATE TABLE Countries (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(255)
);

-- Create the Users table

CREATE TABLE Users (
    Id SERIAL PRIMARY KEY,
    Username VARCHAR(255),
    Password VARCHAR(255),
    Email VARCHAR(255),
    User_Role INTEGER,
    FOREIGN KEY (User_Role) REFERENCES User_Roles(Id)
);

-- Create the Airline_Companies table

CREATE TABLE Airline_Companies (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(255),
    Country_Id INTEGER,
    User_Id INTEGER,
    FOREIGN KEY (Country_Id) REFERENCES Countries(Id),
    FOREIGN KEY (User_Id) REFERENCES Users(Id)
);

-- Create the Flights table

CREATE TABLE Flights (
    Id SERIAL PRIMARY KEY,
    Airline_Company_Id INTEGER,
    Origin_Country_Id INTEGER,
    Destination_Country_Id INTEGER,
    Departure_Time TIMESTAMP,
    Landing_Time TIMESTAMP,
    Remaining_Tickets INTEGER,
    FOREIGN KEY (Airline_Company_Id) REFERENCES Airline_Companies(Id),
    FOREIGN KEY (Origin_Country_Id) REFERENCES Countries(Id),
    FOREIGN KEY (Destination_Country_Id) REFERENCES Countries(Id)
);

-- Create the Customers table

CREATE TABLE Customers (
    Id SERIAL PRIMARY KEY,
    First_Name VARCHAR(255),
    Last_Name VARCHAR(255),
    Address VARCHAR(255),
    Phone_No VARCHAR(255),
    Credit_Card_No VARCHAR(255),
    User_Id INTEGER,
    FOREIGN KEY (User_Id) REFERENCES Users(Id)
);

-- Create the Tickets table

CREATE TABLE Tickets (
    Id SERIAL PRIMARY KEY,
    Flight_Id INTEGER,
    Customer_Id INTEGER,
    UNIQUE (Flight_Id, Customer_Id),
    FOREIGN KEY (Flight_Id) REFERENCES Flights(Id),
    FOREIGN KEY (Customer_Id) REFERENCES Customers(Id)
);

-- Create the Administrators table

CREATE TABLE Administrators (
    Id SERIAL PRIMARY KEY,
    First_Name VARCHAR(255),
    Last_Name VARCHAR(255),
    User_Id INTEGER,
    FOREIGN KEY (User_Id) REFERENCES Users(Id)
);

-- Add the flag field to the Countries table (challenge)

ALTER TABLE Countries
ADD COLUMN Flag BYTEA;

-- Add the thumbnail field to the Users table (challenge)

ALTER TABLE Users
ADD COLUMN Thumbnail BYTEA;
"""
