def gretestValue(n1,n2,n3):
    if(n1>n2 and n1>n3):
        print("greatest value is: ", n1)
    elif(n2>n1 and n2>n3):
        print("greatest value is: ", n2)
    else:
        print("greatest value is: ", n3)

x=int(input("Enter the n1 value: "))
y=int(input("Enter the n2 value: "))
z=int(input("Enter the n3 value: "))
gretestValue(x,y,z)