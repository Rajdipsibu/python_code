f=open("poem.txt")
content=f.read()
if "twinkle" in content:
    print("twinkle word is present in the file.")
else:
    print("twinkle word is not present in the file.")

f.close()