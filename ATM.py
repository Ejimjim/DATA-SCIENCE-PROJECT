#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("********************WELCOME TO PREMIUM BANK!***********************")
 
class Customer:

    def __init__(self, firstname, lastname):
        """ Initialize attributes to describe customer"""
        self.firstname = firstname
        self.lastname = lastname
        self.userpin = 1000
        self.balance = 0
         
    def greetings(self):
        print(f"Good Day! {self.firstname} {self.lastname}")
    
    def validate_pin(self):
        """ Check if pin is valid"""
        login_attempts = 0
        max_login_attempts = 3
        
        try:     
            while login_attempts < max_login_attempts:
                pin = int(input("Please enter your pin: ").strip())
                login_attempts += 1
                if pin == self.userpin:
                    break
                else: 
                    print("Invalid Pin!")
                    
            else:
                print("SORRY! CARD BLOCKED TEMPORARILY")
                
        except:
            print("Invalid Entry! Try Again")
       
            
    def check_balance(self):
        """Request for account balance"""
        print(f"Your Current Balance is $ {self.balance}")
    
    def deposit(self):
        """Deposit a certain amount"""
        try:
            deposit = float(input("How much would you like to deposit: "))
            self.balance += deposit
            print(f"Successful Deposit! \n Your Current Balance is now {self.balance}")
        except:
            print("Invalid Entry! Please Try Again!")
          
    def withdraw(self):
        """Withdraw a certain amount from balance"""
        try:
            withdraw = float(input("How much would you like to withdraw: "))
            if self.balance < withdraw:
                print("Insufficient balance")
            else:
                self.balance -= withdraw
                print(f"Successful Withdrawal! Your new Current Balance is {self.balance}")
        except:
               print("Invalid Entry! Try Again ")       
                             

# We create a while loop to filter through the ATM operations   
user = Customer("Joel", "Konye")
option = 0                           
while True:
    try:                 
        user.validate_pin()
        print("WELCOME \n***************ATM MENU*****************",
                       "\n1. Check Balance"
                       "\n2. Deposit"
                       "\n3. Withdraw"
                       "\n4. EXIT"
                      "\n*****************************************")
        option = int(input("Enter your option: "))
        
        if option == 1:
            user.check_balance()
            option = int(input("Enter your option: ")) 
        elif option == 2:
            user.deposit()
            option = int(input("Enter your option: ")) 
        elif option == 3:
            user.withdraw()
            option = int(input("Enter your option: ")) 
        elif option == 4:
            print("Thank you for banking with us. Do have a nice day")
            break                                              
                             
    except:
        print("Error: Enter 1, 2, 3, or 4 only")
       
       
                             
                             
                             
                             







