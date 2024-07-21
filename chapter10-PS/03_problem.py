class Demo:
         a=10

   
harry=Demo()
print(harry.a)#here 'a' as a class attribute present
harry.a=0
print(harry.a)#here 'a' is instance  attribute ....
print(Demo.a)#but the main class attribute are not change.....