def books():
    cur.execute("create table books(ID_NO int auto_increment not null primary key unique key,Name varchar(255),Author char(200),Price float)")
    mydb.commit()
    cur.execute("alter table books AUTO_INCREMENT=01")
    mydb.commit()
    cur.execute("insert into books(Name,Author,Price) values('Kensuke Kingdom','Michael Morpurgo',140.5),('Otherworld','Jason Segel',130.0),('Otherearth','Kirsten Miller',120.5),('Famous Five','Enid Blyton',125.0),('Refugee','Alan Gratz',160.5),('The Godfather','Mario Puzo',170.0),('Silent Patient','Alex Michaelides',110.0),('Under Ground','S.L Grey',120.50)")
    mydb.commit()
def customers():
    cur.execute("create table customers(ID int not null,Customer varchar(255),DateofIssue date,Book varchar(255),foreign key(ID) references books(ID_NO),foreign key(Customer) references accounts(Username))")
    mydb.commit()
    cur.execute("insert into customers values(01,'Dylan James','2023-02-23','Kensuke Kingdom'),(02,'Simon Minter','2023-03-24','Otherworld'),(04,'Josh Murray','2023-03-26','Famous Five'),(08,'Ethan Hunt','2023-05-13','Under Ground'),(06,'Harry Lewis','2023-02-24','The Godfather')")
    mydb.commit()
def magazines():
    cur.execute("create table magazines(ID int not null primary key,Name varchar(255),Price float,No_Copies int)")
    mydb.commit()
    cur.execute("insert into magazines values(09,'Discover',120.0,30),(10,'American Scientist',130.0,40),(11,'Cosmopolitan',125.0,35),(12,'Forbes India',130.0,50),(13,'India Today',140.0,50),(14,'The Week',110.0,25)")
    mydb.commit()
def buyers():
    cur.execute("create table buyers(ID int,Buyer varchar(255),DateofPurchase date,Magazine varchar(255),foreign key(ID) references magazines(ID),foreign key(Buyer) references accounts(Username))")
    mydb.commit()
    cur.execute("insert into buyers values(09,'Mohan Mohandas','2023-04-06','Discover'),(10,'Rohan Anil','2023-03-07','American Scientist'),(11,'Aditya Iyer','2023-06-21','Cosmopolitan'),(13,'Tony Kroos','2023-04-23','India Today')")   
    mydb.commit()
def accounts():
    cur.execute("create table accounts(Username varchar(255) primary key,Password varchar(255) unique)")
    mydb.commit()
    cur.execute("insert into accounts values('Dylan James','Dyl123'),('Simon Minter','Tal#23'),('Josh Murray','Fre#238'),('Ethan Hunt','MI_62'),('Harry Lewis','W2S#3'),('Mohan Mohandas','AmbMo2'),('Rohan Anil','Ro#45'),('Aditya Iyer','Iyer45'),('Tony Kroos','Ton*8')")
    mydb.commit()

