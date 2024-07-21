with open('old.txt','r')as f:
    content=f.read()
with open('renamed_by_Python.txt','w')as f:
    f.write(content)
    #to delete privious file we use OS module 
    #that wee learn next chapter
    