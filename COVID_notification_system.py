"""COVID Notification System
- This system will be used by Costa Rican public health system to handle COVID notifications.
- The system stores active COVID notifications based on the person's ID.
- It is available for both Guest users who want to consult and professionals who manage the system."""

from getpass import getpass
import time

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


def consult_func(consulta, consult_list):    # Function to consult a notification
    list_cont = 0
    while list_cont <= len(consult_list):
            if consulta == consult_list[list_cont]:
                print(f"{consulta} you're notified forCOVID-19.\n")
                list_cont = 0
                break
            else:
                list_cont += 1
                if list_cont == len(consult_list):
                    print(f"{consulta} you're not notified for COVID-19\n")
                    list_cont = 0
                    break

def ingreso_func(new_notificaction, consult_list):    # Function to enter a notification
    list_cont = 0
    while list_cont <= len(consult_list):
        if new_notificaction == consult_list[list_cont]:
            print(f"{new_notificaction} is already added in the notification system.\n")
            list_cont = 0
            break
        else:
            list_cont += 1
            if list_cont == len(consult_list):
                consult_list.append(new_notificaction)
                print(f"{new_notificaction} has been added to the notification system.\n")
                list_cont = 0
                break

def remove_func(to_remove, consult_list):    # Function to remove a notification
    list_cont = 0
    while list_cont <= len(consult_list):
        if to_remove == consult_list[list_cont]:
            consult_list.remove(to_remove)
            print(f"{to_remove} has been removed from the notification list.\n")
            list_cont = 0
            break
        else:
            list_cont += 1
            if list_cont == len(consult_list):
                print(f"{to_remove} is not currently added in the notification list.\n")
                list_cont = 0
                break


user1 = User('CCSS', 'covid123')
user2 = User('CCSS1', 'Covid20')
notified_list = ['402340017', '402300470']
option = ""    # Variable for the main menu selection
list_cont = 0    # Global counter to run the notified_list
tries = 0    # Counter for amount of tries for an user to enter their login information

             
while option != "e":    # loop to keep user coming back to the main menu
    print("""Welcome to the COVID-19 Notification System.
Choose your user type -> CCSS, Guest or e to exit.""")
    option = input("Type your user: ")

    if option == "Guest":    # Guest user options
        print("This profile only has consultation access by ID number.")
        consult = input("Enter the 10-digit ID you want to check: ")
        consult_func(consult, notified_list)
    elif option == "CCSS":    # CCSS user options
        while tries < 3:
            print("You have 3 tries.")
            user_entry = input("Username: ")
            pass_entry = getpass("Password: ")
            		
            if user_entry == user1.username and pass_entry == user1.password:
            # conditional for a correct login
                tries += 3
                print(f"Welcome {user_entry}.")
                
                task = 0
                while task < 5: 
                    print("""Profile options:
1. Consult notifications.
2. Add new notification.
3. Delete notification.
4. Exit.""")
                    task = int(input("Choose an option (1-4): "))
                    if task == 1:
                        consult = input("Enter the 10-digit ID you want to check: ")
                        consult_func(consult, notified_list)
                    elif task == 2:
                        new_notify = input("Enter the ID number to notify: ")
                        ingreso_func(new_notify, notified_list)
                    elif task == 3:
                        to_remove = input("Enter the ID number to remove: ")
                        remove_func(to_remove, notified_list)
                    elif task == 4:
                        print("Logging you out.")
                        time.sleep(5)
                        break
                        
                            
            else:
                print("Incorrect username/password.")
                tries += 1
        tries = 0
		
