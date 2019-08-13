import os.path
import json
from src.main.python.com.revature.controller import usermenu
from datetime import datetime
import logging


def main():
    now = datetime.now()
    initial_balance_time = now.strftime("%m/%d/%Y")
    print("Deposit Money to account")
    acct_name = input("Please enter the account username: ")
    try:
        with open(
                os.path.join("C:\\Users\\tito_\\PycharmProjects\\project-0-fcanetti94\\src\\test\\resources\\Accounts",
                             "%s.json" % acct_name), 'r') as acct_balance:
            balance_info = json.load(acct_balance)
            account_number = input("Please verify your identity by entering the account number: ")
            if account_number in balance_info['Account Number ']:
                print("Current balance as of " + initial_balance_time + " is " + '${:,.2f}'.format(
                    balance_info['Balance ']))
                deposit_amount = (float(input("Please enter the deposit amount: ")))
                if deposit_amount > 0.0:
                    # creating the new balance
                    new_balance = deposit_amount + balance_info['Balance ']

                    # saving to json and
                    with open(os.path.join(
                            "C:\\Users\\tito_\\PycharmProjects\\project-0-fcanetti94\\src\\test\\resources\\Accounts",
                            "%s.json" % acct_name), 'r+') as balance_update:
                        balance_json = json.load(balance_update)
                        balance_json['Balance '] = new_balance
                        balance_update.seek(0)
                        balance_update.write(json.dumps(balance_json))
                        balance_update.truncate()

                    # Sve to the  transaction history goes here
                    balance_update = open(os.path.join(
                        "C:\\Users\\tito_\\PycharmProjects\\project-0-fcanetti94\\src\\test\\resources\\Balances",
                        "%s.txt" % acct_name), 'a+')
                    balance_update.write(
                        "\n" + initial_balance_time + "- Deposit - " + "${:,.2f}.".format(deposit_amount))
                    balance_update.close()
                else:
                    print("Invalid Amount, please enter an amount higher than 0.Returning to menu")
                    logging.error("Deposit Amount is 0")
                    usermenu.main()

                # after transaction is done return to the user menu
                usermenu.main()
            else:
                print("Account Number does not match the one on record, please try again.")
                logging.warning("INVALID Account number entered")
                usermenu.main()
    except FileNotFoundError:
        print("User not Found returning to main menu")
        logging.ERROR("ACCOUNT NOT FOUND")
        usermenu.main()

    if __name__ == '__main__':
        main()
