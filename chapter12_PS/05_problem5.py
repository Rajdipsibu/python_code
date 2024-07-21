n=int(input('Enter the number: '))
list1=[i*n for i in range(1,11)]
print(list1)

with open('Table.txt','w') as f:
    f.write(str(list1))