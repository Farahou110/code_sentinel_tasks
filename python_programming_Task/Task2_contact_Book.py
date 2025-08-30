def append_inputs() :
    Name = str(input(("please enter your Name ")))
    phone_Number=str(input(("phone mumber please ")))

    with open("contacts.txt","a") as file:
        file.write(Name+ "\t" + phone_Number + "\n")
    print("successfully saved")

def check_db():
    with open("contacts.txt","r") as file:
     Name=file.readline()
    if Name:
        print("=====list of saved details======")
    for name1 in phone_Num:
        print(name1)


def main():
    print("+===phone Book =====")   

    print("\n A. Enter details")

    print("\n B. Check database")
    choice=input("what would you like to do from the above choices ? ")
    if choice == "A":
        append_inputs()
    elif choice =="B":
        check_db()
    else :
        print("please choose from the above choices")

if __name__=="__main__" :
    main()


