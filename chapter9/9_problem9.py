with open('this.txt','r')as f:
    content1=f.read()
with open('this_Copy.txt','r')as f:
    content2=f.read()
if(content1==content2):
    print("the file ARE both identical and maches....")
else:
    print("the file are not maches !!!")