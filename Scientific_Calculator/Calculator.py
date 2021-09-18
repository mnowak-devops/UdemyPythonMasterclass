
#This is one of my first Python prorgam.
#Scientific Calculator with menu.

#Importing the necessary module for advanced math operations
import math

#While loop for continuously running the program and allowing the user to always go back to the main menu and choose another option

while True:
    print("\nChoose the math operation. \n\n0 - Addition\n1 - Subtraction\n2 - Multiplication\n3 - Divide\n4 - Modulo\n5 - Rising to a power\n6 - Squere root\n7 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent\n")

    oper = input("\nYour option from the menu: ")

#Addition
    if oper == "0":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecend value: "))

        print("\nThe result is: " + str(val1 + val2) + "\n")

        # Back to the menu
        back = input('\nGo back to the main menu? (y/n): ')

        if back == "y":
            continue
        else:
            break

#Substraction
    elif oper == "1":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecend value: "))

        print("\nThe result is: " + str(val1 - val2) + "\n")

        # Back to the menu
        back = input('\nGo back to the main menu? (y/n): ')

        if back == "y":
            continue
        else:
            break

#Multiplication
    elif oper == "2":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecend value: "))

        print("\nThe result is: " + str(val1 * val2) + "\n")

        # Back to the menu
        back = input('\nGo back to the main menu? (y/n): ')

        if back == "y":
            continue
        else:
            break

#Division
    elif oper == "3":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecend value: "))

        print("\nThe result is: " + str(val1 / val2) + "\n")

        # Back to the menu
        back = input('\nGo back to the main menu? (y/n): ')

        if back == "y":
            continue
        else:
            break

#Modulo
    elif oper == "4":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecend value: "))

        print("\nThe result is: " + str(val1 % val2) + "\n")

        # Back to the menu
        back = input('\nGo back to the main menu? (y/n): ')

        if back == "y":
            continue
        else:
            break

#Raising to a power
    elif oper == "5":
        val1 = float(input("\nEnter the value: "))
        val2 = float(input("\nEnter the power: "))

        print("\nThe result is: " + str(math.pow(val1, val2)) + "\n")

        # Back to the menu
        back = input('\nGo back to the main menu? (y/n): ')

        if back == "y":
            continue
        else:
            break
#Square root
    elif oper == "6":
        val1 = float(input("\nEnter value for extracting the square root: "))

        print("\nThe result is: " + str(math.sqrt(val1)) + "\n")

        # Back to the menu
        back = input('\nGo back to the main menu? (y/n): ')

        if back == "y":
            continue
        else:
            break

#Logarithm
    elif oper == "7":
        val1 = float(input("\nEnter value for calculating the logarithm of the base 2: "))

        print("\nThe result is: " + str(math.log(val1, 2)) + "\n")

        # Back to the menu
        back = input('\nGo back to the main menu? (y/n): ')

        if back == "y":
            continue
        else:
            break
#Sine
    elif oper == "8":
        val1 = float(input("\nEnter the value (in degrees) for calculating the sine: "))

        print("\nThe result is: " + str(math.sin(math.radians(val1))) + "\n")

        # Back to the menu
        back = input('\nGo back to the main menu? (y/n): ')

        if back == "y":
            continue
        else:
            break

#Cosine
    elif oper == "9":
        val1 = float(input("\nEnter the value (in degrees) for calculating the cosine: "))

        print("\nThe result is: " + str(math.cos(math.radians(val1))) + "\n")

        # Back to the menu
        back = input('\nGo back to the main menu? (y/n): ')

        if back == "y":
            continue
        else:
            break
#Tangent
    elif oper == "10":
        val1 = float(input("\nEnter the value (in degrees) for calculating the tangent: "))

        print("\nThe result is: " + str(math.tan(math.radians(val1))) + "\n")

        # Back to the menu
        back = input('\nGo back to the main menu? (y/n): ')

        if back == "y":
            continue
        else:
            break
#Handling the invalid options
    else:
        print("\nInvalid option!\n")
        continue
#End of the program
