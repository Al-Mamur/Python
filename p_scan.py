fname = input("Enter Your First Name: ")
lname = input("Enetr Your Last Name: ")
fdigit = int(input("Enter First Number= "))
ldigit = int(input("Enter Last Number= "))
operator = input("Enter Operator= ")


sum = fdigit+ldigit
sub = fdigit-ldigit
multi = fdigit*ldigit
div = fdigit/ldigit


print("Your Name: ",fname+" "+lname)


if(operator=="+"):
    print("Addition= ",sum)
elif(operator=="-"):
    print("Submission= ",sub)
elif(operator=="*"):
    print("Multiplication= ",multi)
elif(operator=="/"):
    print("Division= ",div)
elif(operator=="all"):
    print("Addition= ",sum)
    print("Submission= ",sub)
    print("Multiplication= ",multi)
    print("Division= ",div)
else:
    print("InValid")

    

