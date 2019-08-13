import unittest
import json
import os.path
from src.main.python.com.revature.controller import test
from src.main.python.com.revature.controller import menu, usermenu
from hashlib import sha256
from datetime import datetime


# THIS IS THE TESTING SCRIPT
def main():
    print('TO-DO')


# Menu(?)
class Menu_Test(unittest.TestCase):
    '''Tests that the command entered is a number'''

    def test_command_enter_number(self):
        # self.assertTrue(menu.main)
        test_option_login = '1'
        self.assertIs(test_option_login, '1')
        test_option_register = '2'
        self.assertIs(test_option_register, '2')
        test_option_logout = '3'
        self.assertIs(test_option_logout, '3')
        test_option_other = '4'
        self.assertIs(test_option_other, '4')


class Usermenu_Test(unittest.TestCase):

    def test_command_usermenu(self):
        test_usermenu_option_deposit = '1'
        self.assertIs(test_usermenu_option_deposit, '1')
        test_usermenu_option_withdraw = '2'
        self.assertIs(test_usermenu_option_withdraw, '2')
        test_usermenu_option_transaction = '3'
        self.assertIs(test_usermenu_option_transaction, '3')
        test_usermenu_option_logout = '4'
        self.assertIs(test_usermenu_option_logout, '4')


class login_test(unittest.TestCase):

    def test_login_password(self):
        # self.assertTrue(login.main())
        test_username = 'Joaquin Jorge'
        self.assertEqual(test_username, 'Joaquin Jorge')

    def test_login_password(self):
        with open(
                os.path.join("C:\\Users\\tito_\\PycharmProjects\\project-0-fcanetti94\\src\\test\\resources\\Accounts",
                             'jojo.json'), 'r') as read_acct:
            acct_data = json.load(read_acct)
        password_prompt = input("Please enter your password: ").encode('utf-8')
        hash_prompt = sha256(password_prompt).hexdigest()
        if hash_prompt in acct_data['Password ']:
            # logging.info((acct_username + " has logged in to the system"))
            usermenu.main()
        else:
            print("Wrong password, returning to main menu")
            # logging.error((acct_username + " has entered a wrong password"))
            menu.main()


class Deposit_Test(unittest.TestCase):

    def test_deposit_form(self):
        now = datetime.now()
        initial_balance_time = now.strftime("%m/%d/%Y")
        with open(
                os.path.join("C:\\Users\\tito_\\PycharmProjects\\project-0-fcanetti94\\src\\test\\resources\\Accounts",
                             "jojo.json"), 'r') as acct_balance:
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
                            'jojo.json'), 'r+') as balance_update:
                        balance_json = json.load(balance_update)
                        balance_json['Balance '] = new_balance
                        balance_update.seek(0)
                        balance_update.write(json.dumps(balance_json))
                        balance_update.truncate()

                    # Sve to the  transaction history goes here
                    balance_update = open(os.path.join(
                        "C:\\Users\\tito_\\PycharmProjects\\project-0-fcanetti94\\src\\test\\resources\\Balances",
                        "jojo.json"), 'a+')
                    balance_update.write(
                        "\n" + initial_balance_time + "- Deposit - " + "${:,.2f}.".format(deposit_amount))
                    balance_update.close()
                else:
                    print("Invalid Amount, please enter an amount higher than 0.Returning to menu")
                    usermenu.main()


class Withdraw_Test(unittest.TestCase):

    def test_withdraw_form(self):
        now = datetime.now()
        initial_balance_time = now.strftime("%m/%d/%Y")
        with open(
                os.path.join("C:\\Users\\tito_\\PycharmProjects\\project-0-fcanetti94\\src\\test\\resources\\Accounts",
                             "jojo.json"), 'r') as acct_balance:
            balance_info = json.load(acct_balance)
            # Verify the account number before proceeding
            account_number = input("Please verify your identity by entering the account number: ")
            if account_number in balance_info['Account Number ']:
                print("Current balance as of " + initial_balance_time + " is " + "${:,.2f}.".format(
                    balance_info['Balance ']))
                # asks for user input for the amount of money to be withdrawn. IF amount enter exceeds amount in balance, traansaction will be declined
                withdrawn_amount = (float(input("Please enter the amount to be withdrawn: ")))
                if withdrawn_amount <= balance_info['Balance ']:
                    # substract the amount entered from the balance
                    new_balance = balance_info['Balance '] - withdrawn_amount
                    # update json with new balance:
                    with open(os.path.join(
                            "C:\\Users\\tito_\\PycharmProjects\\project-0-fcanetti94\\src\\test\\resources\\Accounts",
                            "jojo.json"), 'r+') as balance_withdrawn:
                        balance_update = json.load(balance_withdrawn)
                        balance_update['Balance '] = new_balance
                        balance_withdrawn.seek(0)
                        balance_withdrawn.write(json.dumps(balance_update))
                        balance_withdrawn.truncate()

                    # record the transaction on the text file:
                    history_update = open(os.path.join(
                        "C:\\Users\\tito_\\PycharmProjects\\project-0-fcanetti94\\src\\test\\resources\\Balances",
                        "jojo.txt"), 'a+')
                    history_update.write(
                        "\n" + initial_balance_time + "- Withdrawal - " + "${:,.2f}.".format(withdrawn_amount))
                    history_update.close()

                    # return the user to the main menu


                else:
                    print(
                        "Overdraft Protection: The transaction you wish to make is unauthorized due to your withdrawal exceeding your available funds")
                    usermenu.main()
            else:
                print("The account number does not match, returning to main menu")


class Transaction_History_Test(unittest.TestCase):

    def test_transactionhistory_form(self):

        print("The complete transaction history for account")
        # search for file to open
        acct_name = input("Please enter the username for the account: ")
        # try - excpet in case file isnt found
        try:
            with open(os.path.join(
                    "C:\\Users\\tito_\\PycharmProjects\\project-0-fcanetti94\\src\\test\\resources\\Balances",
                    "%s.txt" % acct_name), 'r') as balance_history:
                print(balance_history.read())
                print("Transaction history for " + acct_name)
                print("Thanks for using PygBank.")
                usermenu.main()
        except FileNotFoundError:
            print("Account does not exist. Returning to main menu")
            usermenu.main()


if __name__ == '__main__':
    unittest.main()
