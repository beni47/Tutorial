#Simple calculator
import math
#Can use int,but for calculator use float(allows decimals)
#try and except used to handle errors
#float has a specific number it can hold


try:
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))
    operator = input("Enter operator: ")
    if operator =='+':
        result = num1+num2
    elif operator =='-':
        result = num1-num2
    elif operator == '*':
        result = num1*num2
    elif operator == '/':
        if num2 == 0:
            print("Can not divide by zero")
        else:
            result = num1/num2


    print(f"{result:,}")#adds a coma after 3 digits
except ValueError:
    print("INVALID CHARACTERS!")
except ZeroDivisionError as e:
    print(f"ERROR: {e}")


    #functions-round(number[,ndigits])

