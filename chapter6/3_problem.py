p1="make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"

massege=input("Enter your massege here: ")
if((p1 in massege) or (p2 in massege) or (p3 in massege) or (p4 in massege)):
    print("this massege is a spam..!")
else:
    print("this is not a spam...")