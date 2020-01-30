# Created by Kris Penn
# Date: 01/30/20
# Software Testing and QA

def retire():
    return

def bmi():
    print("Welcome to the Body Mass Index application!\n")
    print("To start, we will need some information. Please enter it below.\n\n")

    heightFeet = getHeightFeet()
    heightInches = getHeightInches()
    weight = getWeight()

    #Calculate BMI:
    weight = weight * 0.45
    height = ((heightFeet * 12) + heightInches) * 0.025
    height = height * height
    bmi = weight / height

    print("Your Body Mass index is %d." % (bmi))
    
    if bmi < 18.5:
        print("Your Body Mass Index indicates that you are underweight.\n")
    elif bmi >= 30:
        print("Your Body Mass Index indicates that you are obese.\n")
    elif 25 <= bmi < 30:
        print("Your Body Mass Index indicates that you are overweight.\n")
    else:
        print("Your Body Mass Index indicates that you are of normal weight.\n")
        
    x = True
    while x:
        cont = input("Enter 'A' to return to Main Menu or 'X' to exit the application: ")
        cont = cont.upper()

        if cont == 'A':
            x = False
            mainMenu()
        elif cont == 'X':
            x = False
            exit()
        else:
            print("Invalid input.")
    return

def getHeightFeet():
    
    try:
        height = int(input("Enter height in feet without inches: "))
        return height
    except:
        print("You entered height with inches. Please try again.")
        getHeight()
    
def getHeightInches():
    
    try:
        print("Enter the inches to your height.  For example if you are 5'6\"then enter 6.")
        height = int(input("Enter inches here: "))
        return height
    except:
        print("You entered height with inches. Please try again.")
        getHeight()

def getWeight():
    try:
        weight = int(input("Enter your weight in pounds: "))
        return weight
    except:
        print("Please try again.")
        getWeight()

def mainMenu():
    print("Please choose an option below: ")
    print("A. Body Mass Index")
    print("B. Retirement")
    print("X. Exit Application\n")
    ans = str(input("Enter answer here: "))
    ans = ans.upper()
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
            ans = ans.upper()

def main():
    print("Welcome to the Decision Maker.\n")

    mainMenu()
    return

if __name__ == "__main__":
    main()
