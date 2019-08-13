import json
import os.path
import logging
from src.main.python.com.revature.controller import usermenu
from datetime import datetime


def main():
    #defines and sets the time format
    now = datetime.now()
    transfer_time = now.strftime("%m/ %d/ %Y")
    #asks the user for account username. Try exception used to catch a failed login attempt
    acct_name = input("Please enter the account username: ")
    try:
        with open(os.path.join("C:\\Users\\tito_\\PycharmProjects\\project-0-fcanetti94\\src\\test\\resources\\Accounts",
                             "%s.json" % acct_name), 'r+') as sender_account:
            #verifies the account number is a valid one:
            sender_info = json.load(sender_account)
            account_number = input("Please verify your identity by using the account number: ")
            if account_number in sender_info['Account Number ']:
                print("This transfer cant be cancelled once is done, make sure you send it to the right person.")
                #calls upon the search for the reciving account
                recieving_acct_username = input("Please enter the username of the person recieving money: ")
                #another try except to handle the exception of not finding the recieving account
                try:
                    with open(os.path.join("C:\\Users\\tito_\\PycharmProjects\\project-0-fcanetti94\\src\\test\\resources\\Accounts", "%s.json" % recieving_acct_username), 'r+') as recipient_account:
                        reciever_balance = json.load(recipient_account)
                        #enter the transfer amounts and checks that sender has the available funds for it
                        transfer_amount = float(input("Please enter the amount of money to be transfered: "))
                        if transfer_amount <= sender_info['Balance ']:
                            #records the transfer on senders json file and txt file
                            sender_updated_balance = sender_info['Balance '] - transfer_amount
                            #print("${:,.2f}.".format(sender_updated_balance))
                            #updates the senders json file
                            sender_info['Balance '] = sender_updated_balance
                            sender_account.seek(0)
                            sender_account.write(json.dumps(sender_info))
                            sender_account.truncate()

                            #updates the transaction history for the sender
                            transaction_update = open(os.path.join("C:\\Users\\tito_\\PycharmProjects\\project-0-fcanetti94\\src\\test\\resources\\Balances", "%s.txt" % acct_name), 'a+')
                            transaction_update.write("\n" + transfer_time + " - Transfer to " + recieving_acct_username + " ${:,.2f}.".format(transfer_amount))
                            transaction_update.close()

                            #records the transfer on the recipient json file and txt file
                            new_recipient_balance = transfer_amount + reciever_balance['Balance ']
                            #updates recipient json file
                            reciever_balance['Balance '] = new_recipient_balance
                            recipient_account.seek(0)
                            recipient_account.write(json.dumps(reciever_balance))
                            recipient_account.truncate()

                            #save to the text file
                            transaction_update =  open(os.path.join("C:\\Users\\tito_\\PycharmProjects\\project-0-fcanetti94\\src\\test\\resources\\Balances", "%s.txt" % recieving_acct_username), 'a+')
                            transaction_update.write("\n" + transfer_time + " - Transfer from " + acct_name + " ${:,.2f}.".format(transfer_amount))
                            transaction_update.close()

                        else:
                            print("Insufficient Funds")
                            logging.warning("Not enough funds avaialble  for "  + acct_name)
                            usermenu.main()

                except FileNotFoundError:
                    print("Username not found, transfer cancelled")
                    logging.warning("Transfer cancelled due to not finding the account")
                    usermenu.main()

            else:
                print("Account Number does not match the one on record")
                logging.warning("Invalid account number")
                usermenu.main()

    except FileNotFoundError:
        print("Username not found, returning to main menu")
        logging.error("Account not found")
        usermenu.main()



if __name__ == '__main__':
    main()
