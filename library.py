print("Book collection")
print("------------------")
print("1. Add book name")
print("2. Display book list")
print("3. Edit Books")
print("4. Search Books")
print("5. Delete Books")
print("6. Sorting Books")
print("7. Exit")
print("---------------------")

items = "1. Add book name, 2. Display book list,3. Edit Books, 4. Search Books, 5. Delete Books, 6. Exit"
booklist = []
while True:
    choise = input(items+" what do u want?: ")


    if(choise == "1"):
        bcount = int(input("How many book u want to add?: "))
        for i in range(bcount):
            bookname = input("type book name: ")
            booklist.append(bookname)
    elif(choise == "2"):
        print(booklist)

    elif(choise == "3"):
        print(booklist)
        edit = int(input("which no of book u want to edit: "))
        if edit < len(booklist):
            newname = input("Input the new name: ")
            booklist[edit] = newname
        else:print("wrong input")

    elif(choise == "4"):
        snmae = input("search for Book: ")
        if snmae in booklist:
            print("Yes..the book is available!")
        else:print("not available")

    elif(choise == "5"):
        print(booklist)
        ndel = int(input("which no book u want to delete?:"))
        del booklist[ndel]
        print("After deleting book: ",booklist)

    elif(choise == "6"):
        booklist.sort()
        print(booklist)

    elif(choise == "7"):
        break


    else:print("wrong input")
