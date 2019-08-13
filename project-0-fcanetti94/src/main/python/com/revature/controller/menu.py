import sys
from src.main.python.com.revature.io import login
from src.main.python.com.revature.io import registration
# import the logging  to keep track of possible errors in the code(?)
import logging


# Menu SCRIPTING


def main():
    print("Welcome to Python Bank. Make a selection by typing the number of the option")
    print("""  
1-ENTER
2- REGISTER
3- LOGOUT """)

    ans = input("\n Please enter a number to make your selection")

    # try:
    if ans == "1":
        print("Log In Menu")
        login.main()
    elif ans == "2":
        print("Registration Menu")
        registration.main()
    elif ans == "3":
        print("Goodbye")
        logging.info("Program closed")
        sys.exit(0)
    else:
        logging.error(("INVALID Menu Selection"))
        main()


if __name__ == '__main__':
    main()
