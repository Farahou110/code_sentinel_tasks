def append_inputs():
    Name = str(input("Please enter your Name: ")).strip()
    phone_Number = str(input("Phone number please: ")).strip()
    
    with open("contacts.txt", "a") as file:
        file.write(Name + "," + phone_Number + "\n")
    print("Successfully saved")

def check_db():
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
        
        if not contacts:
            print("No contacts found in database")
            return
            
        print("===== List of Saved Contacts =====")
        for index, contact in enumerate(contacts, 1):
            contact = contact.strip()
            if ',' in contact:
                name, phone = contact.split(',', 1)  # Split only on first comma
                print(f"{index}. {name}: {phone}")
            else:
                print(f"{index}. Invalid format: {contact}")
                
    except FileNotFoundError:
        print("No contacts database found. Please add some contacts first.")

def main():
    print("+=== Phone Book ====")   
    print("\nA. Enter details")
    print("\nB. Check database")
    
    choice = input("What would you like to do from the above choices? ").upper()
    
    if choice == "A":
        append_inputs()
    elif choice == "B":
        check_db()
    else:
        print("Please choose from the above choices (A or B)")

if __name__ == "__main__":
    main()