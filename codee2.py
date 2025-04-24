'''
#printing  type and modifing it
a=1.21
print(type(a))
print(str(a)) 
'''

# 2 print ascii value
'''
char_A= "A"
ascii=ord(char_A)
print("the ascii value of A :",ascii)
'''


# 3 printing ascii value based on given input
'''
char=input("Enter a letter:")
ascii= ord(char)   # for print charcter use "chr" insted of "ord".
print("The ascii value of entered character is :",ascii)
'''
# 4 simple arithemetic oprs
'''
a=5
b=6
print(a+b)
'''

# 5 simple arithemetic oprs based on input
'''
a=int(input("enter first number"))
b=int(input("enter second number"))
print("result of addition",a+b)
print("result of sub",a-b)
print("result of mul",a*b)
print("result of div",a/b)
print("result of floordiv",a//b)
print("result of mod",a%b)
print("result of exp",a**b)
'''
# 6 simple logical oprs based on input
'''
a=int(input("enter first input: "))
b=int(input("enter second input: "))
print("result of AND",a and b )
print("result of OR",a or b )
print("result of XOR",a ^ b )
print("result of left shift",a << b )
'''

# 7  arithemetic oprs based on multiple inputs in nsingle line
'''
a,b,c =input("enter a,b,c values").split(",")
print("addition:", int(a)+int(b)+int(c)) #"int" has to be give for performing arithemetic opt
'''

'''
a,b =input().split(",")
print( int(a)+int(b))
'''

#8 comparison operators by taking inputs
'''
a,b=input("enter inputs").split(",")
print(int(a)>int(b))
print(int(a)<int(b))
print(int(a)==int(b))
print(int(a)!=int(b))
'''


#9 formating output using f-string
'''
x,y= input("enter name and age").split(",")
print(f"Name:{x} Age:{y} years")
'''
