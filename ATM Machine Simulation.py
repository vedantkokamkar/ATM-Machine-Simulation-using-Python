import time

print("Welcome to the STATE BANK OF INDIA ATM!")
time.sleep(1)
print(f"==============================================================")
print("Please insert your CARD below")
time.sleep(1)
print(f"==============================================================")
print(f"Processing the Card Details...")
time.sleep(1)
print(f"...")
time.sleep(1)
print(f"...")
time.sleep(1)
print(f"==============================================================")

pin=1234
pin == pin
balance = 10000

while True: 
 print("""
 PLEASE SELECT THE TYPE OF SERVICE:    
 1.Account Balance Enquiry
 2.Withdraw Cash
 3.Cash Deposit
 4.Reset Pin
 5.Transaction History
 6.Exit
 ==============================================================      
 """
 )

 try:
  option = int(input("Please enter your choice:"))
 except:
  print("Please enter the valid option.")
        
 if option == 1:
  atm_pin=int(input("Enter your security Pin:"))
  if atm_pin == pin:
   print(f"Your current account balance is {balance}.")
   print(f"==============================================================")

 if option == 2:
  withdraw_amount=int(input("Please enter the withdrawal amount:"))
  atm_pin=int(input("Enter your security Pin:"))
  if atm_pin == pin:
   balance = balance - withdraw_amount
   print(f"Rs.{withdraw_amount} has been debited from your account.")
   print(f"Your current balance is Rs.{balance}.")
   print(f"==============================================================")

 if option == 3:
  deposit_amount=int(input("Please the enter amount to deposited:"))
  atm_pin=int(input("Enter your security Pin:"))
  if atm_pin == pin:
   balance = balance + deposit_amount
   print(f"Rs.{deposit_amount} has been deposited to your account.")
   print(f"Your current balance is Rs.{balance}.")
   print(f"==============================================================")

 if option == 4:
  pin=int(input("Enter your previous Pin:"))
  if pin == pin:
   new_pin=int(input("Enter your new Pin:"))
   print(f"Your Pin number has been changed successfully.")
   print(f"Your Updated Pin number is {new_pin}.")
   print(f"==============================================================")
   new_pin == pin

 if option == 5:
  atm_pin=int(input("Enter your security Pin:"))
  if atm_pin == pin:
   print(f"Transaction History for your account:")
   print(f"Rs.{withdraw_amount} was withdrawed.")
   print(f"Rs.{deposit_amount} was deposited.")
   print(f"Your current balance is Rs.{balance}.")
   print(f"==============================================================")

 if option == 6:
  print(f"Thank you for using the State bank of India ATM Service.")
  print(f"Dont forget to remove your card from the machine")
  print(f"See you again soon, Have a good day!!!")
  print(f"==============================================================")
  time.sleep(5)
  break
 
