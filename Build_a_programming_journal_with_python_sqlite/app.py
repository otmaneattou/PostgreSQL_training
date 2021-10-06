from database import add_entry, create_table, get_entries


menu = """Please select one of the following options:
1) Add new entry for today. 
2) View entries.
3) Exit

Your selection: """

welcome = "Welcome to the programming diary!"
create_table()

def promt_new_entry(): 
    #Interaction with client (promt=demander)
    entry_content = input("What have you learned today? ")
    entry_date = input("Enter the  date: ")
    add_entry(entry_content, entry_date)

def view_enties(entries):
    for entry in entries:
        print(f"{entry[1]} \n \t {entry[0]} \n \n")


# The App
print(welcome)

while (user_input := input(menu)) != "3": 
    if user_input == "1":
        promt_new_entry()
    elif user_input == "2":
        view_enties(get_entries())
    else:
        print("Invalid option, please try again!")