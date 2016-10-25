CREATE TABLE Baker(
baker_ID SERIAL PRIMARY KEY NOT NULL,
baker_Fname TEXT NOT NULL,
baker_Lname TEXT NOT NULL,
baker_Email TEXT NOT NULL,
baker_Phone TEXT NOT NULL,
baker_Password TEXT NOT NULL,
bakerPayPal_ID TEXT NOT NULL,
baker_License TEXT NOT NULL
);

CREATE TABLE Bakery(
bakery_ID SERIAL PRIMARY KEY NOT NULL,
baker_ID int NOT NULL REFERENCES Baker(baker_ID),
bakery_Name TEXT NOT NULL,
bakery_Address TEXT NOT NULL,
bakery_Offline boolean NOT NULL,
close_Time TEXT NOT NULL,
open_Time TEXT NOT NULL,
delivery int NOT NULL,
phone_Number TEXT NOT NULL
);

CREATE TABLE Product(
product_ID SERIAL PRIMARY KEY NOT NULL,
bakery_ID int NOT NULL REFERENCES Bakery(bakery_ID),
pname TEXT NOT NULL,
price TEXT NOT NULL,
picture TEXT NOT NULL,
description TEXT NOT NULL,
product_Type TEXT NOT NULL
);

CREATE TABLE Allergens(
product_ID SERIAL NOT NULL REFERENCES Product(product_ID),
allergy_Type TEXT NOT NULL,
PRIMARY KEY (product_ID, allergy_Type)
);

CREATE TABLE Users(
user_ID SERIAL PRIMARY KEY NOT NULL,
user_Fname TEXT NOT NULL,
user_Lname TEXT NOT NULL,
saved_Address TEXT,
user_Email TEXT NOT NULL,
user_Phone TEXT NOT NULL,
user_Password TEXT NOT NULL,
userPayPal_ID TEXT NOT NULL
);

CREATE TABLE BakeryFeedback(
bakery_ID SERIAL NOT NULL REFERENCES Bakery(bakery_ID),
user_ID int NOT NULL REFERENCES Users(user_ID),
entry TEXT NOT NULL,
feedback_Date DATE NOT NULL,
PRIMARY KEY (bakery_ID, user_ID)
);

CREATE TABLE Rating(
product_ID SERIAL NOT NULL REFERENCES Product(product_ID),
user_ID int NOT NULL REFERENCES Users(user_ID),
entry TEXT,
rating_Value int NOT NULL,
rating_Date DATE NOT NULL,
PRIMARY KEY (product_ID, user_ID)
);

CREATE TABLE Orders(
order_ID SERIAL PRIMARY KEY NOT NULL,
user_ID int NOT NULL REFERENCES Users(user_ID),
status int NOT NULL,
order_Date DATE NOT NULL,
order_Address TEXT NOT NULL
);

CREATE TABLE Order_Content(
order_ID SERIAL NOT NULL REFERENCES Orders(order_ID),
product_ID int NOT NULL REFERENCES Product(product_ID),
quantity int NOT NULL,
PRIMARY KEY (order_ID, product_ID)
);
