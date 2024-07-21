from functools import reduce
#map function......
l=[1,2,3,4,5]
squere = lambda x:x*x
sqlist=map(squere,l)
print(list(sqlist))

#FILTER function.........
def even(n):
    if(n%2==0):
        return True
    return False
evenlist=filter(even,l)
print(list(evenlist))

#reduce function.........
def sum(a,b):
    return a+b
print(reduce(sum,l))