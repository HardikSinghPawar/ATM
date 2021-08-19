print("WELCOME TO HSP BANK")

name = [ "hardik","priyansh","noddy","pratap"]
acc_num=[6264058800,7067988848,9926809900,9826429900]
acc_bal=[15660,66844,55774,55989]
gender=["male","male","male","male"]
age = [15,21,8,46]
passcode = [8800,8848,9900,9900]


while True:
    number= int(input("\r\n ENTER YOUR MOBILE NUMBER"))

    if number in acc_num:
        index = acc_num.index(number)
        print(name[index])
        pin=int(input("\r\n ENTER YOUR PIN"))
        if(pin==passcode[index]):
            transaction=int(input("\r\n PRESS 1 TO WIDRAW \r\n PRESS 2 TO DEPOSITE \r\n PRESS 3 TO CHECK ACCOUNT BALANCE \r\n PRESS 4 TO CHANGE PIN "))
            acc_type=int(input("\r\n SELECT ACCOUNT TYPE \r\n PRESS 1 FOR SAVING ACCOUNT \r\n PRESS 2 FOR CURRENT ACCOUNT"))
            if (transaction==1):
                amount = int(input("\r\n ENTER AMOUNT YOU WANT TO WIDRAW"))
                if (amount<=acc_bal[index]):
                    verification=(input("\r\n YOU HAVE SELECTED TO WIDRAW %d \r\n PRESS Y TO PROCEED PRESS N TO CANCEL "%(amount)))
                    if (verification=="Y"):
                        print("\r\n COLLECT CASH")
                        print(acc_bal[index]-amount)
                        print("\r\n  LEFT IN YOUR ACCOUNT")
                else:
                    print(" \r\n INSUFFICIANT BANLANCE ")
                                 

            elif(transaction==2):
                amount1 = int(input("\r\n ENTER AMOUNT YOU WANT TO DEPOSITE"))
                verification=(input("\r\n YOU HAVE SELECTED TO DEPOSITE %d \r\n PRESS Y TO PROCEED PRESS N TO CANCEL"%(amount1)))
                if verification=="Y":
                    print("\r\n PAYMENT SUCSESSFULL \r\n THANKS FOR YOUR TIME")
                    
            elif(transaction==3):
                print("\r\n YOU HAVE %d LEFT IN YOUR ACCOUNT "%(acc_bal[index]))
            elif(transaction==4):
                new_pin=int(input("\r\n ENTER NEW PIN"))
                if(new_pin<10000):
                    pin=new_pin
                    print("\r\n PIN UPDATE SUCSESSFULLY")
            else:
                print("\r\n INVALID OPTION")
        else:
            print("\r\n WRONG PIN")
            continue
    else:
        print("\r\n USER NOT EXISTS")
        continue

            
