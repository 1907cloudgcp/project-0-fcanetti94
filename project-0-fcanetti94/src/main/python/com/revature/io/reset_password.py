# import necsarry stuff to this module
import json
import logging
import os.path
import getpass
from hashlib import sha256
from src.main.python.com.revature.controller import menu
from src.main.python.com.revature.io import registration


def main():
    acct_name = input("Please enter your account name: ")
    #try except to catch an account that wasnt found
    try:
        with open(os.path.join("C:\\Users\\tito_\\PycharmProjects\\project-0-fcanetti94\\src\\test\\resources\\Accounts",
                           "%s.json" % acct_name), 'r+') as acct_verification:
            acct_information = json.load(acct_verification)
            print("Please verify your identity by providing the request information")
            #asks for account number and Full name to verify the information
            fullname_prompt = input("Please enter your full name: ")
            acct_number_prompt = input("Please your account number: ")
            #update_account = json.load(acct_verification)
            #if- else statement to catch if both prompts are on the json file
            if fullname_prompt in acct_information['Account Holder ']:
                if acct_number_prompt in acct_information['Account Number ']:
                    #calls the secure password function found on
                    new_password_hashed = registration.secure_passwd()
                    #record the password on the json file

                    acct_information['Password '] = new_password_hashed
                    acct_verification.seek(0)
                    acct_verification.write(json.dumps(acct_information))
                    acct_verification.truncate()
                    #records the password change on the logging file
                    logging.info("User " + acct_name + " has changed their password")
                    #returns to the menu
                    menu.main()
                else:
                    print("Information provided conflicts with your record")
                    logging.warning("Account Information conflicts with records")
            else:
                print("Information provided conflicts with your record")
                logging.warning("Account Holder Information was not found")
                menu.main()

    except FileNotFoundError:
        print("Account not found,please register for an account")
        logging.error("Account username invalid")
        menu.main()


if __name__ == '__main__':
    main()
