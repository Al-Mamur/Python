print("Welcome to Padma Bridge!!!")
motorcycle = 100
car = 750
pickup = 1200
microbus = 1300
mini_bus = 1400
medium_bus = 2000
big_bus = 2400
small_truck = 1600
medium_truck = 2100
truck = 5500

vehicle = input("What is Your Vehicle? : ")

#motorcycle tol
if(vehicle=="motorcycle"):
    print("Your bill = 100")
    bill = int(input("Pay Your bill: "))
    if(bill == motorcycle):
        print("Thank You!!")
    else:print("Pay again...!")

#car tol
elif(vehicle == "car"):
    print("Your bill = 750")
    bill = int(input("Pay your bill: "))
    if(bill == car):
        print("Thank You")
    else:print("Pay again,,,!")

#pickup tol
elif(vehicle == "pickup"):
    print("Your bill = 1200")
    bill = int(input("Pay your bill: "))
    if(bill == pickup):
        print("Thank You")
    else:print("Pay again,,,!")

#microbus
elif(vehicle == "microbus"):
    print("Your bill = 1300")
    bill = int(input("Pay your bill: "))
    if(bill == microbus):
        print("Thank You")
    else:print("Pay again,,,!")

#mini_bus
elif(vehicle == "mini_bus"):
    print("Your bill = 1400")
    bill = int(input("Pay your bill: "))
    if(bill == mini_bus):
        print("Thank You")
    else:print("Pay again,,,!")

#big_bus
elif(vehicle == "big_bus"):
    print("Your bill = 2400")
    bill = int(input("Pay your bill: "))
    if(bill == big_bus):
        print("Thank You")
    else:print("Pay again,,,!")

#small_truck
elif(vehicle == "small_truck"):
    print("Your bill = 1600")
    bill = int(input("Pay your bill: "))
    if(bill == small_truck):
        print("Thank You")
    else:print("Pay again,,,!")

#medium_truck
elif(vehicle == "medium_truck"):
    print("Your bill = 2100")
    bill = int(input("Pay your bill: "))
    if(bill == medium_truck):
        print("Thank You")
    else:print("Pay again,,,!")

#truck
elif(vehicle == "truck"):
    print("Your bill = 5500")
    bill = int(input("Pay your bill: "))
    if(bill == truck):
        print("Thank You")
    else:print("Pay again,,,!")

else:
    print("not okay!..Press Again!!!")
