#try with finally----->
def main():
    try:
        a=int(input('enter a integer value: '))
        print(a)
        return
    except ValueError as v:
        print(v)
        return
    finally:
        print('you are in finally part')

main()

'''
    'FINALLY' block must be execute 
    it does not depend on  
    'try' block execute or not
    'except' block execute or not 
'''