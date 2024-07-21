with open('this.txt','r')as f:
    content=f.read()
with open('this_Copy.txt','w')as f:
    f.write(content)