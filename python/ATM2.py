print("WELCOME TO HSP BANK")
acc_bal1 = 19500
acc_bal2 = 10000
acc_bal3 = 108680
acc_bal4 = 178900
number= int(input("\r\n ENTER YOUR MOBILE NUMBER"))
if (number==6264058800):
    print(" \r\n HELLO HARDIK")
    pin=int(input("\r\n ENTER YOUR PIN"))

    if(pin==9999):
        transaction=int(input("\r\n PRESS 1 TO WIDRAW \r\n PRESS 2 TO DEPOSITE \r\n PRESS 3 TO CHECK ACCOUNT BALANCE "))
        acc_type=int(input("\r\n SELECT ACCOUNT TYPE \r\n PRESS 1 FOR SAVING ACCOUNT \r\n PRESS 2 FOR CURRENT ACCOUNT"))
        if (transaction==1):
                        amount = int(input("\r\n ENTER AMOUNT YOU WANT TO WIDRAW"))
                        if (amount<=acc_bal1):
                            verification=(input("\r\n YOU HAVE SELECTED TO WIDRAW %d \r\n PRESS Y TO PROCEED PRESS N TO CANCEL "%(amount)))
                            if (verification=="Y"):
                                print("\r\n COLLECT CASH")
                                print(acc_bal1-amount)
                                print("\r\n  LEFT IN YOUR ACCOUNT")
                             
                                
        elif(transaction==2):
            amount1 = int(input("\r\n ENTER AMOUNT YOU WANT TO DEPOSITE"))
            verification=(input("\r\n YOU HAVE SELECTED TO DEPOSITE %d \r\n PRESS Y TO PROCEED PRESS N TO CANCEL"%(amount1)))
            if verification=="Y":
                print("\r\n PAYMENT SUCSESSFULL \r\n THANKS FOR YOUR TIME")
                
        elif(transaction==3):
            print("\r\n YOU HAVE %d LEFT IN YOUR ACCOUNT "%(acc_bal1))
    else:
         print("WRONG PIN")
         
         
elif(number==7067988848):
    print(" \r\n HELLO PRIYANSH")
    pin=int(input("\r\n ENTER YOUR PIN"))

    if(pin==8848):
      transaction=int(input("\r\n PRESS 1 TO WIDRAW \r\n PRESS 2 TO DEPOSITE \r\n PRESS 3 TO CHECK ACCOUNT BALANCE "))
      acc_type=int(input("\r\n SELECT ACCOUNT TYPE \r\n PRESS 1 FOR SAVING ACCOUNT \r\n PRESS 2 FOR CURRENT ACCOUNT "))
      if (transaction==1):
          amount = int(input("\r\n ENTER AMOUNT YOU WANT TO WIDRAW"))
          if (amount<=acc_bal2):
              verification=(input("\r\n YOU HAVE SELECTED TO WIDRAW %d \r\n PRESS Y TO PROCEED PRESS N TO CANCEL "%(amount)))
              if (verification=="Y"):
                  print("\r\n COLLECT CASH")
                  print(acc_bal2-amount)
                  print("\r\n  LEFT IN YOUR ACCOUNT")
                             
                                
      elif(transaction==2):
            amount1 = int(input("\r\n ENTER AMOUNT YOU WANT TO DEPOSITE"))
            verification=(input("\r\n YOU HAVE SELECTED TO DEPOSITE %d \r\n PRESS y TO PROCEED PRESS n TO CANCEL"%(amount1)))
            if verification=="Y":
                print("\r\n PAYMENT SUCSESSFULL \r\n THANKS FOR YOUR TIME")
               
                
      elif(transaction==3):
            print("\r\n YOU HAVE %d LEFT IN YOUR ACCOUNT "%(acc_bal2))          
        
    else:
         print("WRONG PIN")
        
elif(number==9826429900):
    print(" \r\n HELLO PRATAP")
    pin=int(input("\r\n ENTER YOUR PIN"))

    if(pin==9900):
        transaction=int(input("\r\n PRESS 1 TO WIDRAW \r\n PRESS 2 TO DEPOSITE \r\n PRESS 3 TO CHECK ACCOUNT BALANCE "))
        acc_type=int(input("\r\n SELECT ACCOUNT TYPE \r\n PRESS 1 FOR SAVING ACCOUNT \r\n PRESS 2 FOR CURRENT ACCOUNT "))
        if (transaction==1):
                        amount = int(input("\r\n ENTER AMOUNT YOU WANT TO WIDRAW"))
                        if (amount<=acc_bal3):
                            verification=(input("\r\n YOU HAVE SELECTED TO WIDRAW %d \r\n PRESS Y TO PROCEED PRESS N TO CANCEL "%(amount)))
                            if (verification=="Y"):
                                print("\r\n COLLECT CASH")
                                print(acc_bal3-amount)
                                print("\r\n  LEFT IN YOUR ACCOUNT")
                             
                                
        elif(transaction==2):
            amount1 = int(input("\r\n ENTER AMOUNT YOU WANT TO DEPOSITE"))
            verification=(input("\r\n YOU HAVE SELECTED TO DEPOSITE %d \r\n PRESS y TO PROCEED PRESS n TO CANCEL"%(amount1)))
            if verification=="Y":
                print("\r\n PAYMENT SUCSESSFULL \r\n THANKS FOR YOUR TIME")
           
        elif(transaction==3):
            print("\r\n YOU HAVE %d LEFT IN YOUR ACCOUNT "%(acc_bal3))
    else:
         print("WRONG PIN")


if (number==9826022227):
    print(" \r\n HELLO PARIDHI")
    pin=int(input("\r\n ENTER YOUR PIN"))
    if(pin==2227):
       transaction=int(input("\r\n PRESS 1 TO WIDRAW \r\n PRESS 2 TO DEPOSITE \r\n PRESS 3 TO CHECK ACCOUNT BALANCE "))
       acc_type=int(input("\r\n SELECT ACCOUNT TYPE \r\n PRESS 1 FOR SAVING ACCOUNT \r\n PRESS 2 FOR CURRENT ACCOUNT  "))
       if (transaction==1):
           amount = int(input("\r\n ENTER AMOUNT YOU WANT TO WIDRAW"))
           if (amount<=acc_bal4):
               verification=(input("\r\n YOU HAVE SELECTED TO WIDRAW %d \r\n PRESS Y TO PROCEED PRESS N TO CANCEL "%(amount)))
               if (verification=="Y"):
                   print("\r\n COLLECT CASH")
                   print(acc_bal4-amount)
                   print("\r\n  LEFT IN YOUR ACCOUNT")
                             
                                
       elif(transaction==2):
           amount1 = int(input("\r\n ENTER AMOUNT YOU WANT TO DEPOSITE"))
           verification=(input("\r\n YOU HAVE SELECTED TO DEPOSITE %d \r\n PRESS y TO PROCEED PRESS n TO CANCEL"%(amount1)))
           if verification=="Y":
               print("\r\n PAYMENT SUCSESSFULL \r\n THANKS FOR YOUR TIME")
       elif(transaction==3):
            print("\r\n YOU HAVE %d LEFT IN YOUR ACCOUNT "%(acc_bal4))
    else:
         print("\r\n WRONG PIN")

















                  

            
