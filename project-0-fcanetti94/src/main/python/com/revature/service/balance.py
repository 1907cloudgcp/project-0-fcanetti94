import json
import logging
import os.path
from datetime import datetime
from src.main.python.com.revature.controller import usermenu

logging.basicConfig(filename='bank_tracking.log', level=logging.INFO,format="%(module)s : %(asctime)s : %(levelname)s : %(message)s")
# defines the basic structure of the logging message. We will record info, and error messages in this module

def main():
    # define the time to show in output
    now = datetime.now()
    current_time = now.strftime("%m/%d/%Y  %H:%m")

    # Searches for the Account file to open, we are using json in this module since it has the latest balance information
    acct_name = input("Please enter the username for your account: ")
    # try except method to catch a FileNot Found Error
    try:
        with open(
                os.path.join("C:\\Users\\tito_\\PycharmProjects\\project-0-fcanetti94\\src\\test\\resources\\Accounts",
                             "%s.json" % acct_name), 'r') as acct_information:
            balance_info = json.load(acct_information)
            acct_number = input("Please enter the account number: ")
            if acct_number in balance_info['Account Number ']:
                print("Current balance as of " + current_time + " is " + "${:,.2f}.".format(
                    balance_info['Balance ']))
                usermenu.main()
                logging.info("User " + acct_name + " has checked his balance")
            else:
                print("Account Number does not match your account username")
                logging.warning("Account Number entered does not match the one in record")




    except FileNotFoundError:
        print("No account was found under this username")
        logging.error("ACCOUNT NOT FOUND")
        usermenu.main()


if __name__ == '__main__':
    main()
