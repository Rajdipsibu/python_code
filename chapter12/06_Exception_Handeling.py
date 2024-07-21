try:
    a=int(input("Enter 1st num: "))
    b=int(input("Enter 2nd num: "))
    print(a/b)
except ValueError as v:
    print('hay you enter a wrong type value....!!!')
except ZeroDivisionError as z:
    print(z)
    
print("End the Programmer")