print("Welcome to my Dokan..!!!")
print("--------------------------")

products = ["Shirt","Pant","Watch","Shoe"]
shirts = ["red", "blue", "black"]
s_prices = [600,650,700]
pants = ["jeans","gevadin","formal"]
p_prices = [1200,1300,1400]
watches = ["rollex", "timex", "tissot"]
p_watches = [2000,3000,4000]
shoes = ["lotto","nike","puma"]
p_shoes = [5000,6000,7000]

for i in products:
    print(products)
    select1 = input("what do u need? :")
    if(select1 == "shirt"):
        print("here is our shirts")
        print(shirts)
        color_choise = input("Give us your selected color: ")
        if(color_choise == "red"):
            print("Price: ",s_prices[0])
            bill = int(input("Pay ur bills: "))
            if(bill == s_prices[0]):
                print("Thanks for shopping!")
            else:print("pay again")
            break

        elif(color_choise == "blue"):
            print("price: ",s_prices[1])
            bill = int(input("Pay Your bill: "))
            if(bill == s_prices[1]):
                print("Thanks for shopping!")
            else:print("Try again!")
            break

        elif(color_choise == "black"):
            print("price: ",s_prices[2])
            bill = int(input("Pay Your bill: "))
            if(bill == s_prices[2]):
                print("Thanks for shopping!")
            else:print("Try again!")
            break

        else:print("This color is not available")

    elif(select1 == "pant"):
        print("This is our pants: ")
        print(pants)
        color_choise = input("Which color do u want?: ")
        if(color_choise == "jeans"):
            print("price: ",p_prices[0])
            bill = int(input("Pay ur bill: "))
            if(bill == p_prices[0]):
                print("Thanks for shopping!")
            else:print("pay again!")
            break

        elif(color_choise == "gevadin"):
            print("price: ",p_prices[1])
            bill = int(input("Pay ur bill: "))
            if(bill == p_prices[1]):
                print("Thanks for shopping!!")
            else:print("pay again!")
            break

        elif(color_choise == "formal"):
            print("price: ",p_prices[2])
            bill = int(input("Pay ur bill: "))
            if(bill == p_prices[2]):
                print("Thanks for shopping!!")
            else:print("pay again!")
            break

        else:print("This kinda pant not available here!")

    elif(select1 == "watch"):
        print("This is our watchs: ")
        print(watches)
        color_choise = input("Which watch do u want to buy?: ")
        if(color_choise == "rollex"):
            print("prices: ",p_watches[0])
            bill = int(input("Pay ur bill: "))
            if(bill == p_watches[0]):
                print("Thanks for shopping!")
            else:print("Pay again!")
            break

        elif(color_choise == "timex"):
            print("price: ",p_watches[1])
            bill = int(input("Pay ur bill: "))
            if(bill == p_watches[1]):
                print("Thanks for shopping!")
            else:print("Pay again!")
            break

        elif(color_choise == "tissot"):
            print("price: ",p_watches[2])
            bill = int(input("Pay ur bill: "))
            if(bill == p_watches[2]):
                print("Thanks for shopping!")
            else:print("Pay again!")
            break

        else:print("This brand is not available Here!")

    elif(select1 == "shoe"):
        print("This is our shoe collection: ")
        print(shoes)
        color_choise = input("which shoe do u want to buy: ")
        if(color_choise == "lotto"):
            print("price: ",p_shoes[0])
            bill = int(input("Pay ur bill: "))
            if(bill == p_shoes[0]):
                print("Thanks for shopping")
            else:print("pay again!")
            break

        elif(color_choise == "nike"):
            print("price: ",p_shoes[1])
            bill = int(input("Pay ur bill: "))
            if(bill == p_shoes[1]):
                print("Thanks for shopping")
            else:print("pay again!")
            break

        elif(color_choise == "puma"):
            print("price: ",p_shoes[2])
            bill = int(input("Pay ur bill: "))
            if(bill == p_shoes[2]):
                print("Thanks for shopping")
            else:print("pay again!")
            break

        else:print("this shoe is not available")
