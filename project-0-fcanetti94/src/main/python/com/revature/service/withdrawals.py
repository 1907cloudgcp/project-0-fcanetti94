#import necessary modules for the code
import json
import os.path
from datetime import datetime
from src.main.python.com.revature.controller import usermenu
import logging


def main():
    #define basic variables to be used
    now = datetime.now()
    initial_balance_time = now.strftime("%m/%d/%Y")
    print("Withdraw Money from account")
    #define account name to be manipulated
    acct_name = input("Please reenter the account username: ")
    #try catch exception if account is not found
    try:
        with open(os.path.join("C:\\Users\\tito_\\PycharmProjects\\project-0-fcanetti94\\src\\test\\resources\\Accounts","%s.json" % acct_name), 'r') as acct_balance:
            balance_info = json.load(acct_balance)
            #Verify the account number before proceeding
            account_number = input("Please verify your identity by entering the account number: ")
            if account_number in balance_info['Account Number ']:
                print("Current balance as of " + initial_balance_time + " is " + "${:,.2f}.".format(balance_info['Balance ']))
                #asks for user input for the amount of money to be withdrawn. IF amount enter exceeds amount in balance, traansaction will be declined
                withdrawn_amount = (float(input("Please enter the amount to be withdrawn: ")))
                if withdrawn_amount <= balance_info['Balance ']:
                    #substract the amount entered from the balance
                    new_balance = balance_info['Balance '] - withdrawn_amount
                    #update json with new balance:
                    with open(os.path.join("C:\\Users\\tito_\\PycharmProjects\\project-0-fcanetti94\\src\\test\\resources\\Accounts","%s.json" % acct_name), 'r+') as balance_withdrawn:
                        balance_update = json.load(balance_withdrawn)
                        balance_update['Balance '] = new_balance
                        balance_withdrawn.seek(0)
                        balance_withdrawn.write(json.dumps(balance_update))
                        balance_withdrawn.truncate()

                    #record the transaction on the text file:
                    history_update = open(os.path.join("C:\\Users\\tito_\\PycharmProjects\\project-0-fcanetti94\\src\\test\\resources\\Balances", "%s.txt" % acct_name),'a+')
                    history_update.write("\n" + initial_balance_time + "- Withdrawal - " + "${:,.2f}.".format(withdrawn_amount))
                    history_update.close()
                    logging.info((acct_name + " has withdrawn the amount of " + "${:,.2f}.".format(withdrawn_amount)))
                    #return the user to the main menu


                else:
                    print("Overdraft Protection: The transaction you wish to make is unauthorized due to your withdrawal exceeding your available funds")
                    logging.error(("Amount requested can not be higher than " + "${:,.2f}.".format(balance_info['Balance '])))
                    usermenu.main()
            else:
                print("The account number does not match, returning to main menu")
                logging.error("The account number does not match")
                usermenu.main()
    except FileNotFoundError:
        print("Account does not exist, returning to the main menu")
        logging.error("Info entered does not match our records")
        usermenu.main()


if __name__ == '__main__':
    main()
