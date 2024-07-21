list1=[12,13,14,15,16]

# indexNo=0
# for i in list1:
#     print(f'the value of index {indexNo} is {i}')
#     indexNo +=1


#using enumerate more efficent way to print the index no with index value:------------------

for i,item in enumerate(list1):
    print(f'the value of index {i} is {item}')