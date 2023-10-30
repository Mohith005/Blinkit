

def Menu():
    print()
    while True:
        print() 
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("THINKIT".center(80))
        print()
        print('Seasonal Fruits','   ','Fresh Vegetables','  ','Cold Drinks & Juices','  ','Snacks and Munchies','   ','Sweet Tooth','         ')
        print('  ~A~','                     ~B~','                    ~C~','                    ~D~','              ~E~')
        print()
        print()
        print()
        print("_________________________________________________________________________________________________")
        print("                                                                                                ")
        print(" HOT SUMMER DEALS                      PET NEEDS                  IN SICKNESS & IN HEALTH      ")    
        print("        X                               Y                                     Z              ")
        print("                                                                                             ")     
        print("_________________________________________________________________________________________________")
        print()
        print()
        print()
        print('Pet Care','         ','Aata,Rice& Daal','         ','Dairy','         ','Medicines','         ','Personal Care','         ')
        print('  ~F~','                     ~G~','              ~H~','              ~I~','                ~J~')
        print()
        print()
        print("1. Select Items  ")
        print("2. Show Cart")
        print("3. Bill ")
        print()
        w=int(input("What would you like to do: "))
        
        if w==1:
            sc=input("Select a category: ")
            if sc.lower()=='a':
                print()
                import mysql.connector as mc
        
                mydb = mc.connect(host = 'localhost', user = 'root', passwd = 'mohith2005', database = 'ThinkIt')   
                cur = mydb.cursor()
                cur.execute("select * from a")
                rec= cur.fetchall()
                t = "Code","Item","Price"
                print(t)
                print()
                for i in rec:
                    print(i)
                    mydb.commit()

                print()
                inp=input("Would you like to add item to cart (y/n): ")

                if inp=='y':
                    while True:
                        print()
                        adt = int(input("Enter item code to be added: "))
                        amt = int(input("Enter quantity: "))
                        adtt =(adt,)
                        query = "select * from a where code=%s;"
                        cur.execute(query,adtt)
                    
                        fet=cur.fetchall()
                    
                        code = fet[0][0]
                        name = fet[0][1]
                        price = fet[0][2]

                        tup = (code,name,amt,price)
                        query = "insert into cart values(%s,%s,%s,%s)"

                        cur.execute(query,tup)
    
                        print(fet[0][1],"added to the cart.")

                        mydb.commit()
                        print()
                        ate=input("anything else(Y/N): ")
                        if ate in "yY":
                            continue

                        if ate in "nN":
                            break
                    
                
                else:
                    pass
            

            elif sc.lower()=='b':
                print()
                import mysql.connector as mc
        
                mydb = mc.connect(host = 'localhost', user = 'root', passwd = 'mohith2005', database = 'ThinkIt')   
                cur = mydb.cursor()
                cur.execute("select * from b")
                rec= cur.fetchall()
                t = "Code","Item","Price"
                print(t)
                print()
                for i in rec:
                    print(i)
                    mydb.commit()

                print()
                inp=input("Would you like to add item to cart (y/n): ")

                if inp=='y':
                    while True:
                        print()
                        adt = int(input("Enter item code to be added: "))
                        amt = int(input("Enter quantity: "))
                        adtt =(adt,)
                        query = "select * from b where code=%s;"
                        cur.execute(query,adtt)
                    
                        fet=cur.fetchall()
                    
                        code = fet[0][0]
                        name = fet[0][1]
                        price = fet[0][2]

                        tup = (code,name,amt,price)
                        query = "insert into cart values(%s,%s,%s,%s)"

                        cur.execute(query,tup)
    
                        print(fet[0][1],"added to the cart.")

                        mydb.commit()
                        print()
                        ate=input("anything else(Y/N): ")
                        if ate in "yY":
                            continue

                        if ate in "nN":
                            break
                    
                
                else:
                    pass
                
            elif sc.lower()=='c':
                print()
                import mysql.connector as mc
        
                mydb = mc.connect(host = 'localhost', user = 'root', passwd = 'mohith2005', database = 'ThinkIt')   
                cur = mydb.cursor()
                cur.execute("select * from c")
                rec= cur.fetchall()
                t = "Code","Item","Price"
                print(t)
                print()
                for i in rec:
                    print(i)
                    mydb.commit()

                print()
                inp=input("Would you like to add item to cart (y/n): ")

                if inp=='y':
                    while True:
                        print()
                        adt = int(input("Enter item code to be added: "))
                        amt = int(input("Enter quantity: "))
                        adtt =(adt,)
                        query = "select * from c where code=%s;"
                        cur.execute(query,adtt)
                    
                        fet=cur.fetchall()
                    
                        code = fet[0][0]
                        name = fet[0][1]
                        price = fet[0][2]

                        tup = (code,name,amt,price)
                        query = "insert into cart values(%s,%s,%s,%s)"

                        cur.execute(query,tup)
    
                        print(fet[0][1],"added to the cart.")

                        mydb.commit()
                        print()
                        ate=input("anything else(Y/N): ")
                        if ate in "yY":
                            continue

                        if ate in "nN":
                            break
                    
                
                else:
                    pass
                
            elif sc.lower()=='d':
                print()
                import mysql.connector as mc
        
                mydb = mc.connect(host = 'localhost', user = 'root', passwd = 'mohith2005', database = 'ThinkIt')   
                cur = mydb.cursor()
                cur.execute("select * from d")
                rec= cur.fetchall()
                t = "Code","Item","Price"
                print(t)
                print()
                for i in rec:
                    print(i)
                    mydb.commit()

                print()
                inp=input("Would you like to add item to cart (y/n): ")

                if inp=='y':
                    while True:
                        print()
                        adt = int(input("Enter item code to be added: "))
                        amt = int(input("Enter quantity: "))
                        adtt =(adt,)
                        query = "select * from d where code=%s;"
                        cur.execute(query,adtt)
                    
                        fet=cur.fetchall()
                    
                        code = fet[0][0]
                        name = fet[0][1]
                        price = fet[0][2]

                        tup = (code,name,amt,price)
                        query = "insert into cart values(%s,%s,%s,%s)"

                        cur.execute(query,tup)
    
                        print(fet[0][1],"added to the cart.")

                        mydb.commit()
                        print()
                        ate=input("anything else(Y/N): ")
                        if ate in "yY":
                            continue

                        if ate in "nN":
                            break
                    
                
                else:
                    pass

            elif sc.lower()=='e':
                print()
                import mysql.connector as mc
        
                mydb = mc.connect(host = 'localhost', user = 'root', passwd = 'mohith2005', database = 'ThinkIt')   
                cur = mydb.cursor()
                cur.execute("select * from e")
                rec= cur.fetchall()
                t = "Code","Item","Price"
                print(t)
                print()
                for i in rec:
                    print(i)
                    mydb.commit()

                print()
                inp=input("Would you like to add item to cart (y/n): ")

                if inp=='y':
                    while True:
                        print()
                        adt = int(input("Enter item code to be added: "))
                        amt = int(input("Enter quantity: "))
                        adtt =(adt,)
                        query = "select * from e where code=%s;"
                        cur.execute(query,adtt)
                    
                        fet=cur.fetchall()
                    
                        code = fet[0][0]
                        name = fet[0][1]
                        price = fet[0][2]

                        tup = (code,name,amt,price)
                        query = "insert into cart values(%s,%s,%s,%s)"

                        cur.execute(query,tup)
    
                        print(fet[0][1],"added to the cart.")

                        mydb.commit()
                        print()
                        ate=input("anything else(Y/N): ")
                        if ate in "yY":
                            continue

                        if ate in "nN":
                            break
                    
                
                else:
                    pass
                
            elif sc.lower()=='f':
                print()
                import mysql.connector as mc
        
                mydb = mc.connect(host = 'localhost', user = 'root', passwd = 'mohith2005', database = 'ThinkIt')   
                cur = mydb.cursor()
                cur.execute("select * from f")
                rec= cur.fetchall()
                t = "Code","Item","Price"
                print(t)
                print()
                for i in rec:
                    print(i)
                    mydb.commit()

                print()
                inp=input("Would you like to add item to cart (y/n): ")

                if inp=='y':
                    while True:
                        print()
                        adt = int(input("Enter item code to be added: "))
                        amt = int(input("Enter quantity: "))
                        adtt =(adt,)
                        query = "select * from f where code=%s;"
                        cur.execute(query,adtt)
                    
                        fet=cur.fetchall()
                    
                        code = fet[0][0]
                        name = fet[0][1]
                        price = fet[0][2]

                        tup = (code,name,amt,price)
                        query = "insert into cart values(%s,%s,%s,%s)"

                        cur.execute(query,tup)
    
                        print(fet[0][1],"added to the cart.")

                        mydb.commit()
                        print()
                        ate=input("anything else(Y/N): ")
                        if ate in "yY":
                            continue

                        if ate in "nN":
                            break
                    
                
                else:
                    pass
                
            elif sc.lower()=='g':
                print()
                import mysql.connector as mc
        
                mydb = mc.connect(host = 'localhost', user = 'root', passwd = 'mohith2005', database = 'ThinkIt')   
                cur = mydb.cursor()
                cur.execute("select * from g")
                rec= cur.fetchall()
                t = "Code","Item","Price"
                print(t)
                print()
                for i in rec:
                    print(i)
                    mydb.commit()

                print()
                inp=input("Would you like to add item to cart (y/n): ")

                if inp=='y':
                    while True:
                        print()
                        adt = int(input("Enter item code to be added: "))
                        amt = int(input("Enter quantity: "))
                        adtt =(adt,)
                        query = "select * from g where code=%s;"
                        cur.execute(query,adtt)
                    
                        fet=cur.fetchall()
                    
                        code = fet[0][0]
                        name = fet[0][1]
                        price = fet[0][2]

                        tup = (code,name,amt,price)
                        query = "insert into cart values(%s,%s,%s,%s)"

                        cur.execute(query,tup)
    
                        print(fet[0][1],"added to the cart.")

                        mydb.commit()
                        print()
                        ate=input("anything else(Y/N): ")
                        if ate in "yY":
                            continue

                        if ate in "nN":
                            break
                    
                
                else:
                    pass
                
            elif sc.lower()=='h':
                print()
                import mysql.connector as mc
        
                mydb = mc.connect(host = 'localhost', user = 'root', passwd = 'mohith2005', database = 'ThinkIt')   
                cur = mydb.cursor()
                cur.execute("select * from h")
                rec= cur.fetchall()
                t = "Code","Item","Price"
                print(t)
                print()
                for i in rec:
                    print(i)
                    mydb.commit()

                print()
                inp=input("Would you like to add item to cart (y/n): ")

                if inp=='y':
                    while True:
                        print()
                        adt = int(input("Enter item code to be added: "))
                        amt = int(input("Enter quantity: "))
                        adtt =(adt,)
                        query = "select * from h where code=%s;"
                        cur.execute(query,adtt)
                    
                        fet=cur.fetchall()
                    
                        code = fet[0][0]
                        name = fet[0][1]
                        price = fet[0][2]

                        tup = (code,name,amt,price)
                        query = "insert into cart values(%s,%s,%s,%s)"

                        cur.execute(query,tup)
    
                        print(fet[0][1],"added to the cart.")

                        mydb.commit()
                        print()
                        ate=input("anything else(Y/N): ")
                        if ate in "yY":
                            continue

                        if ate in "nN":
                            break
                    
                
                else:
                    pass
                

            elif sc.lower()=='i':
                print()
                import mysql.connector as mc
        
                mydb = mc.connect(host = 'localhost', user = 'root', passwd = 'mohith2005', database = 'ThinkIt')   
                cur = mydb.cursor()
                cur.execute("select * from i")
                rec= cur.fetchall()
                t = "Code","Item","Price"
                print(t)
                print()
                for i in rec:
                    print(i)
                    mydb.commit()

                print()
                inp=input("Would you like to add item to cart (y/n): ")

                if inp=='y':
                    while True:
                        print()
                        adt = int(input("Enter item code to be added: "))
                        amt = int(input("Enter quantity: "))
                        adtt =(adt,)
                        query = "select * from i where code=%s;"
                        cur.execute(query,adtt)
                    
                        fet=cur.fetchall()
                    
                        code = fet[0][0]
                        name = fet[0][1]
                        price = fet[0][2]

                        tup = (code,name,amt,price)
                        query = "insert into cart values(%s,%s,%s,%s)"

                        cur.execute(query,tup)
    
                        print(fet[0][1],"added to the cart.")

                        mydb.commit()
                        print()
                        ate=input("anything else(Y/N): ")
                        if ate in "yY":
                            continue

                        if ate in "nN":
                            break
                    
                
                else:
                    pass
                

            elif sc.lower()=='j':
                print()
                import mysql.connector as mc
        
                mydb = mc.connect(host = 'localhost', user = 'root', passwd = 'mohith2005', database = 'ThinkIt')   
                cur = mydb.cursor()
                cur.execute("select * from j")
                rec= cur.fetchall()
                t = "Code","Item","Price"
                print(t)
                print()
                for i in rec:
                    print(i)
                    mydb.commit()

                print()
                inp=input("Would you like to add item to cart (y/n): ")

                if inp=='y':
                    while True:
                        print()
                        adt = int(input("Enter item code to be added: "))
                        amt = int(input("Enter quantity: "))
                        adtt =(adt,)
                        query = "select * from j where code=%s;"
                        cur.execute(query,adtt)
                    
                        fet=cur.fetchall()
                    
                        code = fet[0][0]
                        name = fet[0][1]
                        price = fet[0][2]

                        tup = (code,name,amt,price)
                        query = "insert into cart values(%s,%s,%s,%s)"

                        cur.execute(query,tup)
    
                        print(fet[0][1],"added to the cart.")

                        mydb.commit()
                        print()
                        ate=input("anything else(Y/N): ")
                        if ate in "yY":
                            continue

                        if ate in "nN":
                            break
                    
                
                else:
                    pass
                
            elif sc.lower()=='x':
                print()
                import mysql.connector as mc
        
                mydb = mc.connect(host = 'localhost', user = 'root', passwd = 'mohith2005', database = 'ThinkIt')   
                cur = mydb.cursor()
                cur.execute("select * from x")
                rec= cur.fetchall()
                t = "Code","Item","Price"
                print(t)
                print()
                for i in rec:
                    print(i)
                    mydb.commit()

                print()
                inp=input("Would you like to add item to cart (y/n): ")

                if inp=='y':
                    while True:
                        print()
                        adt = int(input("Enter item code to be added: "))
                        amt = int(input("Enter quantity: "))
                        adtt =(adt,)
                        query = "select * from x where code=%s;"
                        cur.execute(query,adtt)
                    
                        fet=cur.fetchall()
                    
                        code = fet[0][0]
                        name = fet[0][1]
                        price = fet[0][2]

                        tup = (code,name,amt,price)
                        query = "insert into cart values(%s,%s,%s,%s)"

                        cur.execute(query,tup)
    
                        print(fet[0][1],"added to the cart.")

                        mydb.commit()
                        print()
                        ate=input("anything else(Y/N): ")
                        if ate in "yY":
                            continue

                        if ate in "nN":
                            break
                    
                
                else:
                    pass
                
            elif sc.lower()=='y':
                print()
                import mysql.connector as mc
        
                mydb = mc.connect(host = 'localhost', user = 'root', passwd = 'mohith2005', database = 'ThinkIt')   
                cur = mydb.cursor()
                cur.execute("select * from y")
                rec= cur.fetchall()
                t = "Code","Item","Price"
                print(t)
                print()
                for i in rec:
                    print(i)
                    mydb.commit()

                print()
                inp=input("Would you like to add item to cart (y/n): ")

                if inp=='y':
                    while True:
                        print()
                        adt = int(input("Enter item code to be added: "))
                        amt = int(input("Enter quantity: "))
                        adtt =(adt,)
                        query = "select * from y where code=%s;"
                        cur.execute(query,adtt)
                    
                        fet=cur.fetchall()
                    
                        code = fet[0][0]
                        name = fet[0][1]
                        price = fet[0][2]

                        tup = (code,name,amt,price)
                        query = "insert into cart values(%s,%s,%s,%s)"

                        cur.execute(query,tup)
    
                        print(fet[0][1],"added to the cart.")

                        mydb.commit()
                        print()
                        ate=input("anything else(Y/N): ")
                        if ate in "yY":
                            continue

                        if ate in "nN":
                            break
                    
                
                else:
                    pass
                
            elif sc.lower()=='z':
                print()
                import mysql.connector as mc
        
                mydb = mc.connect(host = 'localhost', user = 'root', passwd = 'mohith2005', database = 'ThinkIt')   
                cur = mydb.cursor()
                cur.execute("select * from z")
                rec= cur.fetchall()
                t = "Code","Item","Price"
                print(t)
                print()
                for i in rec:
                    print(i)
                    mydb.commit()

                print()
                inp=input("Would you like to add item to cart (y/n): ")

                if inp=='y':
                    while True:
                        print()
                        adt = int(input("Enter item code to be added: "))
                        amt = int(input("Enter quantity: "))
                        adtt =(adt,)
                        query = "select * from z where code=%s;"
                        cur.execute(query,adtt)
                    
                        fet=cur.fetchall()
                    
                        code = fet[0][0]
                        name = fet[0][1]
                        price = fet[0][2]

                        tup = (code,name,amt,price)
                        query = "insert into cart values(%s,%s,%s,%s)"

                        cur.execute(query,tup)
    
                        print(fet[0][1],"added to the cart.")

                        mydb.commit()
                        print()
                        ate=input("anything else(Y/N): ")
                        if ate in "yY":
                            continue

                        if ate in "nN":
                            break
                    
                
                else:
                    pass
                

        elif w==2:
            print()
            import mysql.connector as mc
            mydb = mc.connect(host = 'localhost', user = 'root', passwd = 'mohith2005', database = 'ThinkIt')
            cur = mydb.cursor()

            query = ('select * from cart')
            cur.execute(query)
            columns = cur.fetchall()
            if columns == []:
                print()
                print('Cart is Empty!!')
    

            else: 
                print("YOUR CART")
                print()
                cur.execute("select * from cart")
                rec=cur.fetchall()

                t = "Code","Item","Quantity","Price"
                print(t)
                print()               
                for i in rec:
                    print(i)

                print()
                inp=input("Do you want to remove an item (y/n): ")
                print()
                while True:
                    
                    if inp.lower()=='y':
                        cur.execute("select * from cart")
                        rec=cur.fetchall()

                        for i in rec:
                            print("Code: ",i[0],", Item: ",i[1],", Quantity: ",i[2],", Price: ",i[2])
                            print()

                        rem = int(input("Enter Item code to be removed: "))
                        qyt = int(input("Enter how much to remove: "))

                        qur1 = "update cart set quantity = quantity - %s where code = %s;"
                        tup = (qyt,rem)
                        cur.execute(qur1,tup)
                        mydb.commit()
                    
                        qur = "delete from cart where code=%s and quantity<=0;"
                        rem1=(rem,)
                        cur.execute(qur,rem1)
                        mydb.commit()

                        print()

                        inp=input("Do you want to remove an item (y/n): ")

                    elif inp.lower() == "n":
                        break


                inpu=input("press any key to go back:  ")
                if inpu==True:
                        continue

 
        elif w==3:
            print()
            import mysql.connector as mc
            mydb = mc.connect(host = 'localhost', user = 'root', passwd = 'mohith2005', database = 'ThinkIt')
            cur = mydb.cursor()

            query = ('select * from cart')
            cur.execute(query)
            columns = cur.fetchall()
            if columns == []:
                print()
                print('Cart is Empty!!')

            else:
                query = ('select * from login')
                cur.execute(query)
                data = cur.fetchall()
                phone = None
                name = None
                
                for i in data:
                    phone = i[0]
                    name = i[1]


                inp1=input("Continue Shopping (y/n):  ")
                print()
                if inp1.lower()=='y':
                    continue

                elif inp1.lower()=='n':
                    
                    pay=int(input("Enter Payment Method (Card[1]/Cash[2]): "))
                    if pay==2:
                        detail = "CASH"
                        print("Payment Method: ",detail)

                  
                    elif pay==1:
                        detail = "CARD"
                        print()
                        crno=input("enter card number: ")
                        cvv=input("enter cvv: ")
                        nm=input("enter name on card:  ")

                        print()
                        print()
                        print("Payment Method: ",detail)
                        print("Card number: ",crno)
                        print("Card holder: ",nm)
                    
                    address = input("Enter address: ")
                    print()
            
                

                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    
                print("User name: ",name)
                print("Phone number: ",phone)
                print("User address: ",address)
                    
                  
                print()
                print("YOUR CART")
                print()
                total = 0
                
                cur.execute("select * from cart")
                rec=cur.fetchall()

                t = "Code","Item","Quantity","Price"
                print(t)
                print()               
                for i in rec:
                    print(i)
                    amount = i[2]*i[3]
                    total += amount

                print()
                    
                if total<500:
                    print("Oops sorry, you are not eligible for any discount.")

                elif total>=500 and total<1000:
                    print("You have recieved 5% discount")
                    total = (95/100)*total
                    print()
                            

                elif total>=1000:
                    print("You have recieved 10% discount")
                    total = (90/100)*total
                    print()
                       

                print()
                print("Final price: ",total)
                
                Delivery_boys = ['Tanishq Pradhan', 'Vishesh Gupta', 'Nikhil Sharma', 'Divit Vohra', 'Ishaan Karwaal', 'Hardik Gaba', 'Navdeep Singh', 'Atharv Sharma', 'Vedant Seth', 'Mahesh Talle']
                n = True
                while n == True:
                    db = Delivery_boys[random.randint(0,9)]
                    print(db,"will be there in 8 minutes.")
                    n = False
                   
                
                print()
                print("THANK YOU FOR SHOPPING WITH US")
                print()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                cur.execute("truncate table cart;")
                cur.execute("truncate table login;")
                
                break

        

import random
import mysql.connector as mc
mydb = mc.connect(host = 'localhost', user = 'root', passwd = 'mohith2005', database = 'ThinkIt')
cur = mydb.cursor()
cur.execute("truncate table cart;")
cur.execute("truncate table login;")


while True:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("WELCOME TO THINKIT".center(80))
    print()


    print('1. Want to create a new acount? Sign up')
    print('2. Already a user? Log in')
    print('3. Do you want to delete your existing account?')
    print()


    x = int(input('Select what you want to do: '))
    if x == 1:
        mydb = mc.connect(host = 'localhost', user = 'root', passwd = 'mohith2005', database = 'thinkit')
        cur = mydb.cursor()
        phone = int(input('Enter your phone number: '))
        name = input('Enter your name: ')
        passwd = input('Enter your password: ')

        query = ('select * from user where phone = %s')
        tup = (phone,)
        cur.execute(query, tup)
        columns = cur.fetchall()
        if columns == []:
            query = ('insert into user values(%s, %s, %s)')
            tup = (phone, name, passwd)
            cur.execute(query, tup)
            mydb.commit()
            print()
            print('Your account has been created.')

        else:
            print()
            print("Account already exist.")




    elif x == 2:
        mydb = mc.connect(host = 'localhost', user = 'root', passwd = 'mohith2005', database = 'thinkit')
        cur = mydb.cursor()
        phone = int(input('Enter your phone number: '))
        passwd = input('Enter your password: ')
        query = ('select * from user where phone = %s and pass = %s')
        tup = (phone, passwd)
        cur.execute(query, tup)
        columns = cur.fetchall()
        if columns == []:
            print()
            print('Account does not exist!!')
            print("Check your username or password again.")
            print()
            y = input('Want to create a new account instead?(Y/N): ')

            if y == 'Y' or y == 'y':
                print()
                phone1 = int(input('Enter your phone number: '))
                name1 = input('Enter your name: ')
                passwd1 = input('Enter your password: ')
                query = ('insert into user values(%s, %s, %s)')
                tup = (phone1, name1, passwd1)
                cur.execute(query, tup)
                mydb.commit()
                print()
                print('Your account has been created.')

                Menu()

            elif y == 'N' or y == 'n':
                print()
                print('Thank you for visinting ThinkIt.')
                print()
            

        elif columns != None:
            print()
            name = ''
            query = ('select * from user where phone = %s and pass = %s')
            tup = (phone, passwd)
            cur.execute(query, tup)
            data = cur.fetchall()
            for i in data:
                name  = i[1]            

            qry = ('insert into login(phone,name,pass) values(%s,%s,%s)')
            tup1 = (phone,name,passwd)
            cur.execute(qry, tup1)
            mydb.commit()
            print('You have successfully logged in.')
    
            Menu()

    elif x == 3:
        mydb = mc.connect(host = 'localhost', user = 'root', passwd = 'mohith2005', database = 'thinkit')
        cur = mydb.cursor()
        phone = int(input('Enter your phone number: '))
        passwd = input('Enter your password: ')
        query = ('select * from user')
        cur.execute(query)
        columns = cur.fetchall()
        if columns == []:
            print()
            print('Account does not exist!!')

        else: 
            query = ('delete from user where phone = %s and pass = %s')
            tup = (phone, passwd)
            cur.execute(query, tup)
            print()
            print('Your account has been deleted.')

        mydb.commit()
    


