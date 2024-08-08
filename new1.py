import csv

fields = ["name", "mobile"]
database = "contact.csv"

def create():
    data = []
    for field in fields:
        details = input("Enter " + field + ": ")
        data.append(details)
    
    with open(database, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    
    print("\nCreated successfully")

def view():
    try:
        with open(database, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(', '.join(row))
    except FileNotFoundError:
        print("No contacts found.")

def search(name):
    try:
        with open(database, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == name:
                    print('Found contact:', ', '.join(row))
                    return row
            print("Contact not found.")
    except FileNotFoundError:
        print("No contacts found.")
    return None

def update():
    name = input("Enter the name of the contact to update: ")
    contact = search(name)
    if contact:
        new_data = []
        for field in fields:
            if field == "name":
                new_data.append(contact[0])
            else:
                new_details = input(f"Enter new {field} (leave blank to keep current): ")
                if new_details:
                    new_data.append(new_details)
                else:
                    new_data.append(contact[fields.index(field)])
        
        # Read the current contacts
        contacts = []
        with open(database, 'r') as file:
            reader = csv.reader(file)
            contacts = list(reader)
        
        # Update the contact
        for i, row in enumerate(contacts):
            if row[0] == name:
                contacts[i] = new_data
                break
        
        # Write the updated contacts back to the file
        with open(database, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(contacts)
        
        print("\nContact updated successfully")

def main():
    while True:
        print("Menu:")
        print("1. Create")
        print("2. View")
        print("3. Search")
        print("4. Update")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create()
            ans = input("Next contact? (y/n): ").lower()
            if ans == 'y':
                continue
            else:
                break
        elif choice == '2':
            view()
        elif choice == '3':
            name = input("Enter the name to search: ")
            search(name)
        elif choice == '4':
            update()
        elif choice == '5':
            print("Exiting the menu. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
