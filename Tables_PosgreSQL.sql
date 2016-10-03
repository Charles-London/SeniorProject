CREATE TABLE Baker(
Baker_ID SERIAL NOT NULL,
Baker_Fname varchar(30) NOT NULL,
Baker_Lname varchar(30) NOT NULL,
Baker_Email varchar(30) NOT NULL,
Baker_Phone varchar(20) NOT NULL,
Baker_Password varchar(30) NOT NULL,
BakerPayPal_ID varchar(30) NOT NULL,
Baker_License varchar(30) NOT NULL,
PRIMARY KEY (Baker_ID)
)

CREATE TABLE Bakery(
Bakery_ID SERIAL NOT NULL,
Baker_ID int NOT NULL,
Bakery_Name varchar(30) NOT NULL,
Bakery_Address varchar(30) NOT NULL,
Bakery_Offline boolean NOT NULL,
Close_Time varchar(10) NOT NULL,
Open_Time varchar(10) NOT NULL,
Delivery int NOT NULL,
Phone_Number varchar(20) NOT NULL,
PRIMARY KEY (Bakery_ID),
FOREIGN KEY (Baker_ID) REFERENCES Baker(Baker_ID) ON DELETE CASCADE
)

CREATE TABLE Product(
Product_ID SERIAL NOT NULL,
Bakery_ID int NOT NULL,
Pname varchar(30) NOT NULL,
Price varchar(10) NOT NULL,
Picture varchar(30) NOT NULL,
Description varchar(140) NOT NULL, --Length of a tweet sufficient for description
Product_Type varchar(10) NOT NULL,
PRIMARY KEY (Product_ID),
FOREIGN KEY (Bakery_ID) REFERENCES Bakery(Bakery_ID) ON DELETE CASCADE
)

CREATE TABLE Allergens(
Product_ID SERIAL NOT NULL,
Allergy_Type varchar(30) NOT NULL,
PRIMARY KEY (Product_ID, Allergy_Type),
FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID) ON DELETE CASCADE
)

CREATE TABLE Users(
User_ID SERIAL NOT NULL,
User_Fname varchar(30) NOT NULL,
User_Lname varchar(30) NOT NULL,
Saved_Address varchar(30),
User_Email varchar(30) NOT NULL,
User_Phone varchar(20) NOT NULL,
User_Password varchar(30) NOT NULL,
UserPayPal_ID varchar(30) NOT NULL,
PRIMARY KEY (User_ID)
)

CREATE TABLE BakeryFeedback(
Bakery_ID SERIAL NOT NULL,
User_ID int NOT NULL,
Text varchar(140) NOT NULL,
Feedback_Date DATE NOT NULL,
PRIMARY KEY (Bakery_ID, User_ID),
FOREIGN KEY (Bakery_ID) REFERENCES Bakery(Bakery_ID) ON DELETE CASCADE,
FOREIGN KEY (User_ID) REFERENCES Users(User_ID) ON DELETE CASCADE
)

CREATE TABLE Rating(
Product_ID SERIAL NOT NULL,
User_ID int NOT NULL,
Text varchar(140),
Rating_Value int NOT NULL,
Rating_Date DATE NOT NULL,
PRIMARY KEY (Product_ID, User_ID),
FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID) ON DELETE CASCADE,
FOREIGN KEY (User_ID) REFERENCES Users(User_ID) ON DELETE CASCADE
)

CREATE TABLE Orders(
Order_ID SERIAL NOT NULL,
User_ID int NOT NULL,
Status int NOT NULL,
Order_Date DATE NOT NULL,
Order_Address varchar(30) NOT NULL,
PRIMARY KEY (Order_ID),
FOREIGN KEY (User_ID) REFERENCES Users(User_ID) ON DELETE CASCADE
)

CREATE TABLE Order_Content(
Order_ID SERIAL NOT NULL,
Product_ID int NOT NULL,
Quantity int NOT NULL,
PRIMARY KEY (Order_ID, Product_ID),
FOREIGN KEY (Order_ID) REFERENCES Orders(Order_ID) ON DELETE CASCADE,
FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID) ON DELETE CASCADE
)
