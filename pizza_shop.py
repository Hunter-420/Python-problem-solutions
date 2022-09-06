# global decleration for quit function
price=10
eat_in_count=0
take_away_count=0
SubTotalEatIn=0
SubTotalAway=0

# function define
def eat_in():
    # override global variable
    global eat_in_count
    global SubTotalEatIn
    eat_in_count=int(input("Enter the number of pizza required : "))
    SubTotalEatIn=int(eat_in_count*price)
    print("Subtotal : $",SubTotalEatIn)
    EatInServiceCharge=int(SubTotalEatIn*0.1)
    print("Eat-in Service Charge : $",EatInServiceCharge)
    TotalCharge=SubTotalEatIn+EatInServiceCharge
    print("Total for this order : $",TotalCharge,end="\n\n")
    
def take_away():
    global SubTotalAway
    global take_away_count
    take_away_count=int(input("Enter the number of pizza required : "))
    SubTotalAway=int(take_away_count*price)
    print("Subtotal : $",SubTotalAway)
    TakeAwayDiscount=int(SubTotalAway*0.1)
    print("Eat-in Service Charge : $",TakeAwayDiscount)
    TotalCharge=SubTotalAway-TakeAwayDiscount
    print("Total for this order : $",TotalCharge,end="\n\n")
    
def quit():
    # Acess global variable
    SubTotal=SubTotalEatIn+SubTotalAway
    print("Number of Eat-in Orders : ",eat_in_count)
    print("Number of Take-Away Orders : ",take_away_count)
    print("Total sales for today : $",SubTotal)
    
#  Program start from here
print("Welcome to Beezee Piza Shop!")
# For repetation untill user wants to exit
while True:
    # upper function is used to convert input into uppercase
    Type=input("Enter the type of order(E for Eat In, T for Take Away, or Q for Quit : ").upper()
    if Type=="E":
        # function call
        eat_in()
        # after execution of function again program start
        continue
        
    elif Type=="T":
        take_away()
        continue
        
    elif Type=="Q":
        quit()
        break
        
    else:
        print("Please choose valid option!!")
        continue

    