import json
from src.main.python.com.revature.controller import menu
from datetime import datetime
from hashlib import sha256
import os.path
import logging
import getpass
# this function will hash the password for storage on the json file
# Hashes the password so it isnt stored on a plain text format on a json file
def secure_passwd():
    base_passwd = getpass.getpass("Please enter your password. Must have a minimum of six characters: ").encode('utf-8')
    if len(base_passwd) >= 6:
        hash_passwd = sha256(base_passwd).hexdigest()
        logging.info("Password has been hashed")
        return hash_passwd
    else:
        logging.info("Password size created is to small")
        print("Password Must be at least seven characters long")
        secure_passwd()

# This scripts calls for the registration form after the user presses the registration option
def main():
    now = datetime.now()
    acct_creation = now.strftime("%m, %d, %Y")
    name = input("Please enter your name: ")
    acct_number = input("Please enter your account number: ")
    initial_balance = 0.0
    username = input("Please enter a username associated with this account: ")
    hash_passwd = secure_passwd()

    acct_details = {
        'Account Holder ': name,
        'Account Number ': acct_number,
        'Account Creation ': acct_creation,
        'Username ': username,
        'Password ': hash_passwd,
        'Balance ': initial_balance,
    }

    #CREATES THE JSON FILE WITH USERNAME AS ITS NAME. STORES THE ACCOUNT INFORMATION ENTERED TO IT.
    with open(os.path.join("C:\\Users\\tito_\\PycharmProjects\\project-0-fcanetti94\\src\\test\\resources\\Accounts", "%s.json" % username), 'w') as json_file:
        json.dump(acct_details, json_file)
        json_file.write("\n")
    #creates the txt files containing the balances histories
    acct_balancehistory = open(os.path.join("C:\\Users\\tito_\\PycharmProjects\\project-0-fcanetti94\\src\\test\\resources\\Balances" , "%s.txt" % username), 'w')
    acct_balancehistory.write("Account created on " + acct_creation )
    acct_balancehistory.write("\n Transaction History")
    acct_balancehistory.write("\n Initial Balance: " + "${:,.2f}".format(initial_balance))
    acct_balancehistory.close()
    #ADDS USER REGISTRATION TO LOGIN FILE
    logging.info(("Account for: " +name + " has registered an account with the username " + username))
    menu.main()


if __name__ == '__main__':
    main()
