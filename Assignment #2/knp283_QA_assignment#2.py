# Created by Kris Penn
# Date: 01/30/20
# Software Testing and QA

def retire():
    print("\n\nWelcome to the Savings Calculator!\n")
    print("To start, we will need some information.\n")
    age = getAge()
    salary = getSalary()
    savings = getSavings()
    goal = getGoal()
    total = 0

    #Calculate if goal is met:
    yearly = ((savings / 100) * salary) * 1.35

    while True:
        total = total + yearly
        age += 1
        if total >= goal:
            print("Goal Met!")
            print("You will meet your goal by the time you are %d years old." % (age))
            break
        elif age >= 100:
            print("\nSavings goal not met by the time you reach 100 years old.\n")
            break
    
    x = True
    while x:
        ans = input("Enter 'A' to go to the main menu or 'X' to exit the application: ")
        ans = ans.upper()
        print("\n")
        if ans == 'A':
            x = False
            mainMenu()
        elif ans == 'X':
            x = False
            print("Thanks for using the savings calculator!")
            exit()
        else:
            print("Invalid input. Please enter either 'A' or 'X'")
    return

def getAge():
    try:
        age = int(input("Enter your age in years: "))
        return age
    except:
        print("Invalid input. Please enter a number for your age in years\n")
        getAge()
        return

def getSalary():
    try:
        salary = int(input("Enter yearly salary: "))
        return salary
    except:
        print("Invalid input. Please enter a number.\n")
        getSalary()

def getSavings():
    try:
        savings = int(input("Enter your percentage saved, leave out the percentage sign: "))
        return savings    
    except:
        print("Invalid input. Be sure you did not include the percentage symbol.\n")
        getSavings()

def getGoal():
    try:
        goal = int(input("Enter a number amount for your savings goal: "))
        return goal
    except:
        print("Invalid input.  Please enter just a number amount for your goal.\n")
        getGoal()
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
    print("A. Body Mass Index Calculator")
    print("B. Retirement Savings Calculator")
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
