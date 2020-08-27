import sys
import Myfunction
def menu():
    exit=0
    while exit==0:
        print("Select an option: ")
        option = input(
            "A: Create a new call\n"
            "B: View all customer calls by phone number\n"
            "C: Displays the amount to be paid by a customer to all his lines by ID card\n"
            "D: Check the number of lines per route\n"
            "E: Check whether the line has exceeded the allowed number of minutes\n"
            "Q: To exit\n")
        if option == 'A' or option == 'a' or option == 'ש':
            Myfunction.createNewCall()
        elif option == 'B' or option == 'b' or option == 'נ':
            Myfunction.displayCallsByPhone()
        elif option == 'C' or option == 'c' or option == 'ב':
            Myfunction.displayPay()
        elif option == 'D' or option == 'd' or option == 'ג':
            Myfunction.showLinesOfRouter()
        elif option == 'E' or option == 'e' or option == 'ק':
            Myfunction.ExceptionCheck()
        elif option == 'Q' or option == 'q' or option == '/':
            sys.exit()
            exit=1

menu()