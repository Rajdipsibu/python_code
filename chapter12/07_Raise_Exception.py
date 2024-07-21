
a=int(input("Enter 1st num: "))
b=int(input("Enter 2nd num: "))
if(b==0):
    # so here we raise a error to dont run whole program stop this time ,,,here program will crash/distroy
    raise ZeroDivisionError('hy you are not divaded by zero any no...stupid !!!')
else:
    print(f'a/b= {a/b}')
