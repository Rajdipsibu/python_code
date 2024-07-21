l=[2,15,13,14,20]
def getfunk(n):
    if(n%5==0):
        return True
    return False
l1=filter(getfunk,l)
print(list(l1))