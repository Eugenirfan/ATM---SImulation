class Atm:

    opening_balance=0

    
    def __init__(self):
        tries=0
        times=3
        while tries<3:
            print("Welcome to your Bank: ")
            pin =int(input("Please enter your 4 digit PIN: "))

            if pin==1234:
                
                print("1.Balance Enquiry, 2.Withdrawal, 3.Deposit,4.Pin Change".replace(",", "\n"))
                x= int(input("choose the function you would like to perform: "))

                if x==1:
                    print(self.balance())

                if x==2:
                    print(self.withdrawal())

                if x==3:
                    print(self.deposit())

            else:
                tries+=1
                times-=1
                print("Wrong Pin, Try again")
                print("You have {0} Tries Left".format(times))
                
        else:
            
            print("Goodbye, Try again tomorrow")




    def deposit(self):
        a=int(input("Enter the deposit amount: "))
        self.opening_balance+=a
        print("Your Balance is: {}".format(self.opening_balance))
        snow=int(input("would you like another transaction?, 1.Yes 2.No:  ".replace(",", "\n")))
        if snow==1:
            self.__init__()
        else:
            print("Thank you")
        
        
    def withdrawal(self):
        a=int(input("Enter the withdrawal amount: "))
        self.opening_balance-=a
        print("Your Balance is: {0}".format(self.opening_balance))
        b=a/2000
        print("your 2000 is",b)
        c=a%2000
        d=c/500
        print("your 500 is",d)
        e=c%500
        f=e/100
        print("your 100 is",f)
        g=e%100
        h=g/10
        print("your 10 is",h)
        snow=int(input("would you like another transaction?, 1.Yes 2.No:  ".replace(",", "\n")))
        if snow==1:
            self.__init__()
        else:
            print("Thank you")

    def balance(self):
        print("Your Balance is: {0}".format(self.opening_balance))
        snow=int(input("would you like another transaction?, 1.Yes 2.No:  ".replace(",", "\n")))
        if snow==1:
            self.__init__()
        else:
            print("Thank you")
    

ob=Atm()    
    
