import json
from src.main.python.com.revature.controller import  menu
import logging
from src.main.python.com.revature.controller import usermenu
from hashlib import sha256
import os.path


# THIS SCRIPT IS FOR THE MAIN LOG IN SCREEN FOR THE SYSTEM
def main():
    #MUST CREATE A TRY-EXCEPT THINGY TO CATCH IF THE FILE NAME ISNT FOUND.
    acct_username = input("Please enter the username: ")
    try:
        with open(os.path.join("C:\\Users\\tito_\\PycharmProjects\\project-0-fcanetti94\\src\\test\\resources\\Accounts",
                           "%s.json" % acct_username), 'r') as read_acct:
            acct_data = json.load(read_acct)
            #print(acct_data['Password '])
            password_prompt = input("Please enter your password: ").encode('utf-8')
            hash_prompt = sha256(password_prompt).hexdigest()
            try:
                if hash_prompt in acct_data['Password ']:
                    logging.info((acct_username + " has logged in to the system"))
                    usermenu.main()
                else:
                    print("Wrong password, returning to main menu")
                    logging.error((acct_username + " has entered a wrong password"))
                    menu.main()
            except:
                print("Useless")
    except FileNotFoundError:
        print("The account does not exist, please reenter your username. If you dont have a username you must "
              "register for the service before attempting to log in. Returning to Main Menu")
        logging.error(("Account Username does not exist"))
        menu.main()


if __name__ == '__main__':
    main()
