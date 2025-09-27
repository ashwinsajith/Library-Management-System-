import mysql.connector
from prettytable import PrettyTable
from prettytable import from_db_cursor as p
import table_creation #importing the module containing functions for creating tables
from utilities import * #importing the module containing all the other user defined functions apart from creation.

mydb=mysql.connector.connect(host="localhost",user="root",password="1712Ashw",database="library")
cur=mydb.cursor()

try:
    table_creation.books()
except:
    pass
try:
    table_creation.accounts()
except:
    pass
try:
    table_creation.magazines()
except:
    pass
try:
    table_creation.customers()
except:
    pass
try:
    table_creation.buyers()
except:
    pass

print("*"*108)
print("\t\t\t\t\t 𝓦𝓔𝓛𝓒𝓞𝓜𝓔 𝓣𝓞 𝓣𝓗𝓔 𝓛𝓘𝓑𝓡𝓐𝓡𝓨")
print("*"*108)
print()
print("+ "*52)
print("+\t\t\t\t\t 𝑅𝒰𝐿𝐸𝒮 𝒪𝐹 𝒯𝐻𝐸 𝐿𝐼𝐵𝑅𝒜𝑅𝒴                                       +")
print("+1)An issued book must be returned within 15 days.An sum of ₹2 must be paid for every exceeding day.   +")
print("+2)If a book is not returned within a year,a police complaint will rightfully be filed.                +")
print("+3)While creating an account,Username must be the full name of the User.                               +")
print("+4)A borrower can borrow another book only after return of the first book.                             +")
print("+5)The admin must make sure to delete the record after the borrower has returned the book.             +")
print("+ "*52)
print()
position=position()
counte=0
if position=='Admin':
    print(" "+"-"*63)
    print("| 1 to view the existing records of the books.                  |")
    print("| 2 to view the existing records of the customers for books.    |")
    print("| 3 to view the existing records of the magazines.              |")
    print("| 4 to view the existing records of the buyers of magazines.    |")
    print("| 5 to add a record.                                            |")
    print("| 6 to remove a record.                                         |")
    print("| 7 to add or remove a column.                                  |")
    print("| 8 to modify column or to add/drop primary key in any table.   |")
    print("| 9 to add similar values to a particular column.               |")#This is useful to add default
    #values when a column has just been added.
    print("| 10 to sort the table in ascending or descending order.        |")
    print("| 11 to update a particular record.                             |")
    print("| 12 to find the sum/average of the prices or number of records.|")
    print(" "+"-"*63)
    choice=int(input("Enter your choice:"))
    while choice!=0:
        if choice==1:
            cur.execute("select * from books")
            x=p(cur)
            print(x)
        elif choice==2:
            cur.execute("select * from customers")
            x=p(cur)
            print(x)
        elif choice==3:
            cur.execute("select * from magazines")
            x=p(cur)
            print(x)
        elif choice==4:
            cur.execute("select * from buyers")
            x=p(cur)
            print(x)
        elif choice==5:
            optional=input("Book/Customer/Magazine/Buyer?-")
            if optional=='Book':
                #According to the rules of the library,a customer can only issue a book that is listed in the
                #book records.Also,the customer has to return a book before issuing another one.
                identity=int(input("Enter the id number of the book:"))
                name=input("Enter the name of the book:")
                auth=input("Enter the author of the book:")
                price=eval(input("Enter the price of the book:"))
                cur.execute("select Name from books")
                fetch=cur.fetchall()
                check=count_particular(fetch,name)
                if check==True:
                    print("The book is already in the system.")
                else:
                    sql="insert into books values(%s,%s,%s,%s)"
                    val=(identity,name,auth,price)
                    cur.execute(sql,val)
                    mydb.commit()
                    print("Record added!")
            elif optional=='Customer':
                identity=int(input("Enter the id number of the book:"))
                name=input("Enter the name of the customer:")
                date=input("Enter the date issued(yyyy-mm-dd):")
                book=input("Enter the name of the book:")
                cur.execute("select Customer from customers")
                fetch=cur.fetchall()
                check=count_particular(fetch,name)
                cur.execute("select Username from accounts")
                fetch1=cur.fetchall()
                check1=count_particular(fetch1,name)
                if check==True or check1==False:
                    print("Make sure to delete the existing record after the customer has returned the book.Also,ensure that the account has been created.")
                else:
                    sql="insert into customers values(%s,%s,%s,%s)"
                    val=(identity,name,date,book)
                    cur.execute(sql,val)
                    mydb.commit()
                    print("Record added!")
            elif optional=='Magazine':
                iden=int(input("Enter the id number of the magazine:"))
                name=input("Enter the name:")
                Price=float(input("Enter the price:"))
                copies=int(input("Enter the number of copies:"))
                cur.execute("select Name from magazines")
                fetch=cur.fetchall()
                check=count_particular(fetch,name)
                if check==True:
                    print("Record containing",name,"already exists.")
                else:
                    sql="insert into magazines values(%s,%s,%s,%s)"
                    tup=(iden,name,Price,copies)
                    cur.execute(sql,tup)
                    mydb.commit()
                    print("Record added!")
            elif optional=='Buyer':
                name=input("Enter the name of the buyer:")
                iden=int(input("Enter the id of the magazine:"))
                dop=input("Enter the date of purchase:")
                mag=input("Enter the name of the magazine:")
                cur.execute("select Username from accounts")
                fetch=cur.fetchall()
                check=count_particular(fetch,name)
                if check==True:
                    tup=(iden,name,dop,mag)
                    sql="insert into buyers values(%s,%s,%s,%s)"
                    cur.execute(sql,tup)
                    mydb.commit()
                    print("Record added!")
                else:
                    print("Ensure that the account is created first.")
            else:
                print("Invalid choice.")
        elif choice==6:
            optional=input("Book,Customer,Magazine or Buyer?-")
            if optional=='Book':
                iden=int(input("Enter the id of the book to be deleted:"))
                cur.execute("select ID_NO from books")
                fetch=cur.fetchall()
                check=count_particular(fetch,iden)
                if check==False:
                    print("Record does not exist.")
                else:
                    try:
                        lqs=f"DELETE FROM customers where ID={iden}"
                        cur.execute(lqs)
                        mydb.commit()
                        sql=f"DELETE FROM books where ID_NO={iden}"
                        cur.execute(sql)
                        mydb.commit()
                        print("Record removed!")
                    except:
                        sql=f"DELETE FROM books where ID_NO={iden}"
                        cur.execute(sql)
                        mydb.commit()
                        print("Record removed!")
            elif optional=='Customer':
                name=input("Enter the name of the customer:")
                cur.execute("select Customer from customers")
                fetch=cur.fetchall()
                check=count_particular(fetch,name)
                if check==False:
                    print("Record does not exist.")
                else:
                    tup=(name,)
                    delete="DELETE FROM customers where Customer=%s"
                    cur.execute(delete,tup)
                    mydb.commit()
                    print("Record removed!")
            elif optional=='Magazine':
                iden=int(input("Enter the id of the magazine to be deleted:"))
                cur.execute("select ID from magazines")
                fetch=cur.fetchall()
                check=count_particular(fetch,iden)
                if check==False:
                    print("Record does not exist.")
                else:
                    try:
                        lqs=f"DELETE FROM buyers where ID={iden}"
                        cur.execute(lqs)
                        mydb.commit()
                        sql=f"DELETE FROM magazines where ID={iden}"
                        cur.execute(sql)
                        mydb.commit()
                        print("Record removed!")
                    except:
                        sql=f"DELETE FROM magazines where ID={iden}"
                        cur.execute(sql)
                        mydb.commit()
                        print("Record removed!")                   
            elif optional=='Buyer':
                name=input("Enter the name of the buyer:")
                mag=input("Enter the name of the magazine:")
                cur.execute("select Buyer from buyers")
                fetch=cur.fetchall()
                check=count_particular(fetch,name)
                if check==False:
                    print("Record does not exist.")
                else:
                    tup=(name,mag)
                    delete="DELETE FROM buyers where Buyer=%s and Magazine=%s"
                    cur.execute(delete,tup)
                    mydb.commit()
                    print("Record removed!")
            else:
                print("Invalid choice.")
        elif choice==7:
            option=input("Add or remove column(Add or Remove)?-")
            if option=='Add':
                table=input("Enter the table where the column is to be added(books/customers/magazines/buyers/accounts):")
                column=input("Enter the column to be added:")
                data=input("Enter the data type:")
                sql=f"alter table {table} add {column} {data}"
                cur.execute(sql)
                mydb.commit()
                print("Column added!")
            elif option=='Remove':
                table=input("Enter the table where the column is to be removed(books/customers/magazines/buyers/accounts):")
                column=input("Enter the column to be removed:")
                sql=f"alter table {table} drop column {column}"
                cur.execute(sql)
                mydb.commit()
                print("Column removed!")
            else:
                print("Invalid option")
        elif choice==8:
            option=input("Modify the datatype or add or drop primary key constraint(Answer with M or A or D):")
            n1=input("Enter the table name(books/customers/magazines/buyers:")
            print("Before changes:")
            statement=f"DESC {n1}"
            cur.execute(statement)
            x=p(cur)
            print(x)
            if option=='M':
                n2=input("Enter the column whose datatype is to be modified:")
                n3=input("Enter the new datatype:")
                s=f"ALTER TABLE {n1} MODIFY {n2} {n3}"
                cur.execute(s)
                mydb.commit()
                print("After changes:")
                statement=f"DESC {n1}"
                cur.execute(statement)
                x=p(cur)
                print(x)
            elif option=='A':
                try:
                    n2=input("Enter the column name of the column where primary key constraint is to be added:")
                    s=f"ALTER TABLE {n1} add PRIMARY KEY({n2})"
                    cur.execute(s)
                    mydb.commit()
                    print("Primary key added.")
                except:
                    print("Cannot be added.This can be because it does not meet the conditions or it already exists.")
            elif option=='D':
                try:
                    cur.execute(f"ALTER TABLE {n1} drop PRIMARY KEY")
                    mydb.commit()
                    print("Primary key dropped.")
                except:
                    print("Primary key cannot be dropped.This could be due to foreign key constraint or it does not exist.")
            else:
                print("Invalid.")
        elif choice==9:
            table=input("Enter the table to be updated(books/magazines/customers/buyers):")
            print("Original table:")
            cur.execute(f"SELECT * from {table}")
            x=p(cur)
            print(x)
            col=input("Enter the column to be updated:")
            val=eval(input("Enter the new value:"))
            cur.execute(f"UPDATE {table} set {col}={val}")
            mydb.commit()
            print("Updated table:")
            cur.execute(f"SELECT * from {table}")
            x=p(cur)
            print(x)
        elif choice==10:
            table=input("Enter the table to be displayed(books/magazines/customers/buyers):")
            print("Original table:")
            cur.execute(f"SELECT * from {table}")
            x=p(cur)
            print(x)
            print()
            col=input("Enter the column to be sorted:")
            sort=input("Ascending or Descending(A or D):")
            print()
            if sort=='A':
                print("Sorted table:")
                cur.execute(f"SELECT * from {table} order by {col} asc")
                x=p(cur)
                print(x)
            elif sort=='D':
                cur.execute(f"SELECT * from {table} order by {col} desc")
                x=p(cur)
                print(x)
            else:
                print("Invalid choice.")
        elif choice==11:
            table=input("Enter the table(books/magazines/customers/buyers):")
            try:
                column=input("Enter the column where the record is to be updated:")
                data=input("Enter the datatype(str or numeric):")
                condition=input("Enter the condition for updation:")
                print("Original table:")
                cur.execute(f"SELECT * from {table}")
                x=p(cur)
                print(x)
                if data=='str':
                    
                    val=input("Enter the new value:")
                elif data=='numeric':
                    val=eval(input("Enter the new value:"))
                else:
                    print("Invalid entry.")
                cur.execute(f"UPDATE {table} set {column}={val} where {condition}")
                mydb.commit()
                print("Updated table:")
                cur.execute(f"SELECT * from {table}")
                x=p(cur)
                print(x)
            except:
                print("Record not updated.This could be because of the foreign key constraint or the non-existence of the condition/column.")
        elif choice==12:
            table=input("Enter the table(books or magazines):")
            avg_sum_count=input("Sum/Average/Count?-")
            if avg_sum_count=='Sum':
                cur.execute(f"SELECT sum(Price) from {table}")
                fetch=cur.fetchall()
                total=fetch[0][0]
                print("The sum of the prices is:",total)
            elif avg_sum_count=='Average':
                cur.execute(f"SELECT avg(Price) from {table}")
                fetch1=cur.fetchall()
                avg=fetch1[0][0]
                print("The average of the prices is:",avg)
            elif avg_sum_count=='Count':
                cur.execute(f"SELECT count(*) from {table}")
                fetch2=cur.fetchall()
                count=fetch2[0][0]
                print("The number of records is:",count)
            else:
                print("Invalid entry.")
        else:
            print("Invalid entry.")
        choice=int(input("Enter your choice(0 to exit):"))
        print("~"*108)
elif position=='Guest':
    choice=input("Do you have an existing account(Yes or No)?-")
    cur.execute("SET SQL_SAFE_UPDATES = 0;")
    if choice=='Yes':
        user=input("Enter your username:")#Username is the full name of the guest
        passwd=input("Enter your password:")
        #A table is made containing all the usernames and passwords of the guests
        cur.execute("SELECT * FROM accounts")
        fetch=cur.fetchall()
        for i in fetch:
            if i[0]==user and i[1]==passwd:
                counte=1
                print(" "+"-"*80)
                print("| Enter 1 to view issued books.                                                  |")
                print("| Enter 2 to view bought magazines.                                              |")
                print("| Enter 3 to know the excess(if required)amount to be paid in case of a borrowal.|")
                print("| Enter 4 to check for strength of password.                                     |")
                print("| Enter 5 to update your details.                                                |")
                print("| Enter 6 to remove your account.                                                |")
                print("| Enter 7 to view the books,magazines bought along with their prices.            |")
                print(" "+"-"*80)
                n=int(input("Enter your choice:"))
                #mydb.commit()
                while True:
                    if n==1:
                        print("Books Issued:")
                        cur.execute(f"SELECT Book from customers where Customer='{user}'")
                        x=p(cur)
                        print(x)
                    elif n==2:
                        print("Magazines Bought:")
                        cur.execute(f"SELECT Magazine from buyers where Buyer='{user}'")
                        x=p(cur)
                        print(x)
                    elif n==3:
                        #Every day exceeding 15 days from the day of borrowal costs an extra 2 rupees to be paid.
                        #According to the rules of the library,a police complaint will be filed against anyone keeping the book
                        #for over a year.Therefore,this option is only for the borrowers who have borrowed the book for less than a year.
                        day=input("Enter the date of return of the books(yyyy-mm-dd):")
                        Year=int(day[0:4])
                        if int(day[5])==0:
                            month=int(day[6])
                        else:
                            month=int(day[5:7])
                        if day[-2]==0:
                            date=int(day[-1])
                        else:
                            date=int(day[-2::])
                        dor=dayofyear(Year,month,date)
                        #dor stands for date of return
                        #doi stands for date of issue
                        sql=f"select month(DateofIssue),day(DateofIssue),year(DateofIssue) from customers where Customer='{user}'"
                        cur.execute(sql)
                        fetch=cur.fetchall()
                        total=0
                        for i in fetch:
                            mon=i[0]
                            dat=i[1]
                            year=i[2]
                            doi=dayofyear(year,mon,dat)
                        if dor-doi<0:#This condition is kept for the situation when the issue date is in one year but the date
                            #of return is in the next year.
                            if leap(year)==True:
                                excess=366-doi
                                total+=(dor+excess-15)*2
                            else:
                                excess=365-doi
                                total+=(dor+excess-15)*2
                        else:
                            if dor-doi>15:
                                total+=(dor-doi-15)*2
                            else:
                                total=0
                        print("The total to be paid is:",total)
                    elif n==4:
                        print(" "+"-"*97)
                        print("|\t\t\t\t\t 𝒫𝒜𝒮𝒮𝒲𝒪𝑅𝒟 𝒮𝒯𝑅𝐸𝒩𝒢𝒯𝐻 𝒞𝐻𝐸𝒞𝒦                            |")
                        print("|1)A password is deemed strong if it is atleast 5 characters in length and has special characters.|")
                        print("|2)Special characters must be either # or - or _. Otherwise,the password is invalid.              |")
                        print("|3)It is deemed weak if it contains only alphabets and numbers.                                   |")
                        print("|4)It is deemed very weak if it contains only one type of character.                              |")
                        print("|5)A password can be made stronger if it starts or ends with a number.                            |")
                        print("|6)The password can also be deemed invalid if it contains whitespaces.                            |")
                        print(" "+"-"*97)                           
                        counter=0
                        for i in passwd:
                            if i in '#-_':
                                if len(passwd)>=5:
                                    counter=1
                            else:
                                if i.isalnum():
                                    pass
                                else:
                                    print("Your password is invalid. It contains unpermitted special characters.Please update it.")
                                    counter=2
                                    break
                        if counter==1:
                            print("Your password is strong.")
                        elif counter==2:
                            break
                        
                        else:
                            alpha=[]
                            number=[]
                            for i in passwd:
                                if i.isalpha():
                                    alpha.append(i)
                                elif i.isdigit():
                                    number.append(i)
                            if alpha==[] or number==[]:
                                print("Your password is very weak.Please add different types of characters.")
                            else:
                                print("Your password is weak.It is reccomended to use special characters.")
                        if startsends_number(passwd)==True:
                            print("Your password can be made stronger.Make sure it does not start or end with a number.")
                        
                        if whitespace(passwd)==True:
                            print("Your password contains whitespaces.It is invalid.")
                    elif n==5:
                        new_username=input("Enter the new username:")
                        new_password=input("Enter the new password:")
                        cur.execute("SET FOREIGN_KEY_CHECKS=0;")
                        mydb.commit()
                        cur.execute(f"UPDATE accounts set Username='{new_username}' where Username='{user}'")
                        mydb.commit()
                        cur.execute(f"UPDATE accounts set Password='{new_password}' where Username='{new_username}'")
                        mydb.commit()
                        try:
                            cur.execute(f"UPDATE customers set Customer='{new_username}' where Customer='{user}'")
                            mydb.commit()
                        except:
                            pass
                        try:
                            cur.execute(f"UPDATE buyers set Buyer='{new_username}' where Buyer='{user}'")
                            mydb.commit()
                        except:
                            pass
                        cur.execute("SET FOREIGN_KEY_CHECKS=1;")
                        mydb.commit()
                        print("Records updated!")
                        break
                    elif n==6:
                        try:
                            cur.execute(f"DELETE from customers where Customer='{user}'")
                            mydb.commit()
                        except:
                            pass
                        try:
                            cur.execute(f"DELETE from buyers where Buyer='{user}'")
                            mydb.commit()
                        except:
                            pass
                        cur.execute(f"DELETE from accounts where Username='{user}'")
                        mydb.commit()
                        print("Records deleted!")
                        break
                    elif n==7:
                        print("Books:")
                        cur.execute(f"SELECT books.name,books.price from books,customers where books.ID_NO=customers.ID and customers.Customer='{user}'")
                        x=p(cur)
                        print(x)
                        print("Magazines:")
                        cur.execute(f"SELECT magazines.Name,magazines.Price from magazines,buyers where magazines.ID=buyers.ID and buyers.Buyer='{user}'")
                        x=p(cur)
                        print(x)
                    elif n==0:
                        break
                    else:
                        print("Invalid option.")
                    n=int(input("Enter your choice again(0 to exit):"))
                    print("~"*108)
        else:
            if counte!=1:
                print("Your details are invalid.")
    elif choice=='No':
        new_account=input("Do you wish to create a new account(Yes or No)?-")
        if new_account=='Yes':
            new_user=input("Enter the username:")
            new_pass=input("Enter the password:")
            cur.execute(f"INSERT INTO accounts values('{new_user}','{new_pass}')")
            mydb.commit()
            print("New account created!")
        else:
            print("Creating a new account is free!We would like you to join us on our inquisitive journey of books and magazines!")
    else:
        print("Invalid choice.")
else:
    print("Invalid choice.")
print("𝑻𝒉𝒂𝒏𝒌 𝒚𝒐𝒖!𝑾𝒆 𝒉𝒐𝒑𝒆 𝒕𝒐 𝒔𝒆𝒆 𝒚𝒐𝒖 𝒂𝒈𝒂𝒊𝒏..")
print("*"*108)           






    


































