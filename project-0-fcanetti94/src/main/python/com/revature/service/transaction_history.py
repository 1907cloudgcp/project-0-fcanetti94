import os.path
import logging
from src.main.python.com.revature.controller import usermenu

#define the logging metrics
logging.basicConfig(filename='bank_tracking.log', level=logging.INFO,format="%(module)s : %(asctime)s : %(levelname)s : %(message)s")


def main():
    print("The complete transaction history for account")
    #search for file to open
    acct_name = input("Please enter the username for the account: ")
    #try - excpet in case file isnt found
    try:
        with open(os.path.join("C:\\Users\\tito_\\PycharmProjects\\project-0-fcanetti94\\src\\test\\resources\\Balances" , "%s.txt" % acct_name), 'r') as balance_history:
            print (balance_history.read())
            print("Transaction history for " + acct_name)
            print("Thanks for using PygBank.")
            logging.info("User " + acct_name + " checked transaction history")
            usermenu.main()
    except FileNotFoundError:
        print("Account does not exist. Returning to main menu")
        usermenu.main()
        logging.warning("Account was not found on the Records")


    #return to menu
    usermenu.main()


if __name__ == '__main__':
    main()