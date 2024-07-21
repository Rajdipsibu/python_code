a=100      #global variable..........

def funk():
    a=3    #Local variable............
    print(a)


funk() #print 3
print(a) #print 100

#-------------------------------------------------------------------------------------------------------------------------
a=100      #global variable..........

def funk():
    global a # this Global keyword  change the value of global value of a,,,
    a=3    
    print(a)


funk() #print 3
print(a) #print 3