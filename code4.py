# 1 if - statement
'''
w= input( "enter weather condition")
if(w == "sunny"):
     print("you can play outside")
     print("you can play outside")
print("havefun")
'''


# 2 if-else statements
'''
w= input("enter weather condition:")
if(w  == "sunny"):
    print("can play outside")
    print("can play outside")
else:
    print("play inside")
print("havefun")
'''


# 3 using if-elif-else statements
'''
w = input("enter weather condition:")
if(w == "sunny"):
    print(" go out and play")
elif(w == "rainy"):
    print("be inside and play")
elif(w == "hot"):
    print("go to swimming")
else:
    print("sleep")

print("have fun")  
'''


# 4 using if-elif-else along with logical operation

w = input("enter weather condition:")
w2 = input("enter w2")
if(w == "sunny"):
    print(" go out and play")
elif(w == "rainy"):
    print("be inside and play")
elif(w == "hot") or (w2 == "sunny"):
    print("go to swimming")
else:
    print("sleep")

print("have fun") 

# 5 build calculator 
'''
a=int(input("enter a value:"))
b=int(input("enter b value:"))
opt = input("enter operation :")
if(opt == "add"):
    print("addition:",a+b)
elif(opt == "sub"):
    print("substraction:",a-b)
elif(opt == "mul"):
    print("multiplication:",a*b)
else:
    print("division:",a/b)

print("mission success")
''' 
#or
'''
a=int(input("enter a value:"))
b=int(input("enter b value:"))
opt = input("enter operation :")
if(opt == "add"):
    print(f"addition:{a+b}")
elif(opt == "sub"):
    print(f"substraction:{a-b}")
elif(opt == "mul"):
    print(f"multiplication:{a*b}")
elif(opt == "div"):
    print(f"division:{a/b}")
else:
     print("invalid operation")# handling invalid operations
'''