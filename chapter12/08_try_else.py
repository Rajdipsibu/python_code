#try with else----->
try:
    a=int(input('enter a integer value: '))
    print(a)
except ValueError as v:
    print(v)
else:
    print('you are in else part')

'''if 'try' block success fully execute then -
    'else' part is execut.
    but 'try' block give an error then-
    it go to the 'excepts' part and does not run 'else' part.'''



