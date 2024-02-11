try:
    p = float(input('What was your initial investment: '))
    r = float(input('Enter annual interest rate: '))
    n = int(input('How often is the interest compounded in a year: '))
    t = int(input('What is the number of years you been saving: '))

except ValueError:
    print("Enter valid values")
def calculate_interest():
    interest = p * (1 + r / n) ** (n * t)
    return interest
print(calculate_interest())