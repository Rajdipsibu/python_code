from functools import reduce
l=[2,15,13,14,20]
def getMax(a,b):
    if(a>b):
        return a
    return b
max=reduce(getMax,l)
print(max)