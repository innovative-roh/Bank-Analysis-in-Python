	import cx_Oracle  
	from tkinter import *  
	false=0  
	root = Tk()  
	v = IntVar()  
	v.set(0)   
	  
	languages = [  
	    ("Sign Up",1),  
	    ("Sign In",2),  
	    ("Admin Sign In",3),  
	    ("Quit",4),  
	          
	]  
	  
	class Customer:  
	    def __init__(self):  
	        self.cid=""  
	        self.cphone=""  
	        self.cname=""  
	        self.caddress=""  
	        self.cpassword=""  
	        self.ctype=""  
	        self.cbalance=0  
	        self.check = 1  
	        self.repeat = 0  
	          
	    def addCustomer(self):  
	        while(self.check == 1):  
	            print("\n********** PLease enter your details for Sign Up **********\n")  
	            self.cname =  input("Enter Name              :")  
	            self.cphone = input("Enter Phone (10 digit)  :")  
	            self.caddress=input("Enter Address           :")  
	            self.cpassword=input("Enter 8char password    :")  
	            self.ctype=input("Current/Savings Account :")  
	            self.cid = self.cphone[::-1]  
	            self.check = 0  
	            try:  
	                if(len(self.cphone)!=10):  
	                    raise Exception("Invalid phone number")  
	                if(len(self.cphone)==10):  
	                    for i in self.cphone[0:]:  
	                        if(i.isdigit()==0):  
	                            raise Exception("Invalid phone number")  
	                if(len(self.cpassword)!=8):  
	                    raise Exception("Invalid password")  
	                if((self.ctype != "Current" and self.ctype != "current") and (self.ctype != "Savings" self.ctype != "savings")):  
	                    raise Exception("Invalid Account type")  
	            except Exception as e:  
	                print(e)  
	                self.check = 1  
	        print("\n\nAccount created successfully\n")  
	        print("Your Account number is :",self.cid)  
	        if(self.ctype == "Current" or self.ctype == "current"):  
	            self.cbalance = 0  
	        if(self.ctype == "Savings" or self.ctype == "savings"):  
	            self.cbalance = 5000   
	        con=cx_Oracle.connect('nvp/nvp@localhost/XE')  
	        cur=con.cursor()  
	        cur.execute("""INSERT INTO customer VALUES (:p1 ,:p2 ,:3 5,:6,:7)""",(self.cname,self.cid,self.cpassword,self.cphone,self.caddress,self.ctype,self.cbalance))  
	        con.commit()   
	        con.close()    
	          
	    def customerLogin(self):  
	        while(self.repeat != 3):  
	            print("\n********** Customer Login  **********\n")  
	            a = input("Customer Id : ")  
	            b = input("Password   : ")  
	            con=cx_Oracle.connect('nvp/nvp@localhost/XE')  
	            cur=con.cursor()  
	            cur.execute("""SELECT password FROM customer WHERE cid = :p1""",(a,))  
	            opt = cur.fetchall()  
	            con.close()   
	            try:  
	                new = opt[0]  
	                if( b != new[0] ) :  
	                    print("\n OOPS !! wrong password or Customer Id \n")   
	                    self.repeat = self.repeat + 1  
	                if(self.repeat == 2):  
	                    print("\n !!! This is your last chance to login !!! \n")   
	                if( b == new[0] ) :  
	                    print("\n <-- Login successful --> \n")  
	                    ac.active()  
	                    break  
	                if(self.repeat == 3):  
	                    print("Please contact Admin , 3 attempt finished ")  
	            except IndexError:  
	                print("Something went wrong ! , try again")   
	                self.repeat = self.repeat + 1  
	                if(self.repeat == 3):  
	                    print("Please contact Admin , 3 attempt finished ")  
	              
	class Account:  
	    def __init__(self):  
	        self.changeAddress=""  
	        self.deposit=0  
	        self.withdraw=0  
	        self.transfer=0  
	        self.cid=""  
	        self.cid2=""  
	          
	    def active(self):  
	        dot = 1  
	        while (dot == 1):  
	            print (" ------------------- Menu --------------------")  
	            print("1. Change address\n2. Money Deposit\n3. Money Withdraw\n4. Money Transfer\n5. Print Statement \n6. Account Closure \n7. Customer Logout")  
	            ch=int(input("\nEnter choice: "))  
	            if ch==1:  
	                self.changeAd()  
	            elif ch==2:  
	                self.depositM()  
	            elif ch==3:  
	                self.withdrawM()  
	            elif ch==4:  
	                self.transferM()  
	            elif ch==5:  
	                self.statement()  
	            elif ch==6:  
	                self.closure()  
	            elif ch==7:  
	                print("\n ---- Logged Out successfully -----\n")  
	                dot = 0  
	            else:  
	                print ("Wrong Choice")  
	                  
	    def changeAd(self):  
	        self.cid = input("\nEnter Customer id for conformation :")  
	        self.changeAddress=input("Enter Address change : ")  
	        con=cx_Oracle.connect('nvp/nvp@localhost/XE')  
	        cur=con.cursor()  
	        cur.execute("""UPDATE customer SET address = :p1 WHERE cid= :p2 self.changeAddress,self.cid))  
	        con.commit()   
	        con.close()   
	        print("\nAddress Updated !\n")  
	          
	    def depositM(self):  
	        self.cid = input("\nEnter Customer id for conformation :")  
	        self.deposit=input("Enter deposit amount : ")  
	        con=cx_Oracle.connect('nvp/nvp@localhost/XE')  
	        cur=con.cursor()  
	        cur.execute("""UPDATE customer SET balance = balance+:p1 WHERE cid= :p2 self.deposit,self.cid))  
	        con.commit()   
	        con.close()   
	        print("\n Transaction successful !\n")  
	          
	    def withdrawM(self):  
	        self.cid = input("\nEnter Customer id for conformation :")  
	        self.withdraw=int(input("Enter withdraw amount : "))  
	        con=cx_Oracle.connect('nvp/nvp@localhost/XE')  
	        cur=con.cursor()  
	        cur.execute("""SELECT balance FROM customer WHERE cid=:p1 """,(self.cid,))  
	        res=cur.fetchone()  
	        if(self.withdraw < res[0]):  
	            cur.execute("""UPDATE customer SET balance = balance-:p1 WHERE cid= :p2 self.withdraw,self.cid))  
	            con.commit()  
	            print("\n Transaction successful !\n")  
	        else:  
	            print("\n!!! Low balance !!!\n")  
	        con.close()   
	          
	    def transferM(self):  
	        self.cid = input("\nEnter Sender Customer id for conformation :")  
	        self.cid2 = input("\nEnter Receiver Customer id                :")  
	        self.transfer=int(input("Enter transfer amount : "))  
	        con=cx_Oracle.connect('nvp/nvp@localhost/XE')  
	        cur=con.cursor()  
	        cur.execute("""SELECT balance FROM customer WHERE cid=:p1 """,(self.cid,))  
	        res1=cur.fetchone()  
	        if(self.transfer < res1[0]):  
	            cur.execute("""UPDATE customer SET balance = balance-:p1 WHERE cid= :p2 self.transfer,self.cid))  
	            cur.execute("""UPDATE customer SET balance = balance+:p1 WHERE cid= :p2 self.transfer,self.cid2))  
	            con.commit()  
	            print("\n Transaction successful !\n")  
	        else:  
	            print("\n!!! Low balance !!!\n")  
	        con.close()   
	          
	    def statement(self):  
	        con=cx_Oracle.connect('nvp/nvp@localhost/XE')  
	        a = input("\nEnter Sender Customer id for conformation :")  
	        cur=con.cursor()  
	        cur.execute("""SELECT name FROM customer WHERE cid = :p1""",(a,))  
	        opt = cur.fetchone()  
	        cur.execute("""SELECT balance FROM customer WHERE cid = :p1""",(a,))  
	        opt1 = cur.fetchone()  
	        print("\n ------------ Account Statement ----------- \n")  
	        print("Account Number  : ",a)  
	        print("Account Holder  : ",opt[0])  
	        print("Account Balance : ",opt1[0])  
	        con.close()   
	          
	    def closure(self):  
	        a = input("\nEnter Customer id for conformation :")  
	        con=cx_Oracle.connect('nvp/nvp@localhost/XE')  
	        cur=con.cursor()  
	        cur.execute("""SELECT name FROM customer WHERE cid = :p1""",(a,))  
	        opt = cur.fetchone()  
	        cur.execute("""SELECT address FROM customer WHERE cid = :p1""",(a,))  
	        opt1 = cur.fetchone()  
	        cur.execute("""INSERT INTO admin VALUES (:p1 ,:p2 ,:3 )""",(opt[0],opt1[0],a))  
	        cur.execute("""DELETE FROM customer WHERE cid=:p1""",(a,))  
	        con.commit()  
	        con.close()  
	        print("\nYour account is closed , Thank you \n ")  
	        exit()  
	  
	class Admin:  
	    def __init__(self):  
	        self.id = "admin"  
	        self.pwd="admin"  
	      
	    def adminLogin(self):  
	        a=input("Enter Admin Username :")  
	        b=input("Enter Admin Password :")  
	        if(self.id == a and self.pwd == b):  
	            print("<----- Login successful ------>")  
	            con=cx_Oracle.connect('nvp/nvp@localhost/XE')  
	            cur=con.cursor()  
	            cur.execute("""SELECT * FROM admin""")  
	            opt = cur.fetchall()  
	            print("---------  Closed accounts details ---------")  
	            for i in opt:  
	                print("---------------------------")  
	                print("Name        :",i[0])  
	                print("Address     :",i[1])  
	                print("Customer id :",i[2])  
	                print("---------------------------")  
	              
	            con.close()  
	        else:  
	            print("<----- Login Failed ------>")  
	              
	            
	  
	c=Customer()  
	ac=Account()  
	ad=Admin()          
	  
	  
	def ShowChoice():     
	    loop=True     
	    while loop:   
	        choice = v.get()  
	        if choice==1:    
	            c.addCustomer()  
	            loop=false  
	        elif choice==2:  
	            c.customerLogin()  
	            loop=false  
	        elif choice==3:  
	            ad.adminLogin()  
	            loop=false  
	        else:  
	            loop=false  
	            root.destroy()  
	              
	Label(root,   
	      text="""Welcome to Bank of Troied.com""",  
	      justify = LEFT,  
	      padx = 20).pack()  
	  
	for txt, val in languages:  
	    Radiobutton(root,   
	                text=txt,  
	                indicatoron = 0,  
	                width = 40,  
	                height = 2,  
	                padx = 40,   
	                variable=v,   
	                bg="deepSkyBlue2",  
	                command=ShowChoice,  
	                value=val).pack(anchor=W)  
	  
	  
mainloop()  
