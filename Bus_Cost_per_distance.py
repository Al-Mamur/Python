print("welcome to our bus service(Mohammodpur to Mirpur)")
Shyamoli_cost = 10
Tecniqal_cost = 20
Mirpur_cost = 30
destination = input("Where do u want to go: ")
paid_amount = int(input("Pay your money: "))

if(destination=="Shyamoli"):
    print("Your cost = 10")
    if(Shyamoli_cost == paid_amount):
        print("OK done")
    elif(Shyamoli_cost > paid_amount):
        x_vara = Shyamoli_cost-paid_amount
        print("U need to pay: ",x_vara)
    elif(Shyamoli_cost < paid_amount):
        new_vara = paid_amount-Shyamoli_cost
        print("You xtra money: ",new_vara)
    else:
        print("invalid")

if(destination=="Tecniqal"):
    print("Your cost = 20")
    if (Tecniqal_cost == paid_amount):
        print("OK done")
    elif (Tecniqal_cost > paid_amount):
        x_vara = Tecniqal_cost - paid_amount
        print("U need to pay: ", x_vara)
    elif (Tecniqal_cost < paid_amount):
        new_vara = paid_amount - Tecniqal_cost
        print("You xtra money: ", new_vara)
    else:
        print("invalid")

if(destination=="Mirpur"):
    print("Your cost = 30")
    if (Mirpur_cost == paid_amount):
        print("OK done")
    elif (Mirpur_cost > paid_amount):
        x_vara = Mirpur_cost - paid_amount
        print("U need to pay: ", x_vara)
    elif (Mirpur_cost < paid_amount):
        new_vara = paid_amount - Mirpur_cost
        print("You xtra money: ", new_vara)
    else:
        print("invalid")
