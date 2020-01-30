# Created by Kris Penn
# Date: 01/30/20
# Software Testing and QA

def retire():
    return

def bmi():
    return

def mainMenu():
    print("Please choose an option below: ")
    print("A. Body Mass Index")
    print("B. Retirement")
    print("X. Exit Application\n")
    ans = str(input("Enter answer here: "))
    ans.upper()
    x = True
    while x:
        if ans == 'A':
            x = False
            bmi()
            return
        elif ans == 'B':
            x = False
            retire()
            return
        elif ans == 'X':
            print("\nThanks for choosing the Decision Maker application!")
            exit()
        else:
            print("Please enter 'A' for the Body Mass Index app or 'B' for the retirement app.")
            print("If you would like to close the application, enter X.\n")
            ans = str(input("Enter answer here: "))

def main():
    print("Welcome to the Decision Maker.\n")

    mainMenu()
    return

if __name__ == "__main__":
    main()
