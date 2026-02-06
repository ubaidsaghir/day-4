import pandas as pd

try:
    num = int(input("Enter number"))
    print(num)
except ValueError:
    print("Invalid input")
    


def safe_drive(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by zero"
print(safe_drive(10,0))    
            