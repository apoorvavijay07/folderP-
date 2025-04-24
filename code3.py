'''
# 1 performing arithemetic opt
num1,num2=input(" enter 1st and 2nd no.").split(",")
#num2=int(input("enter 2nd no."))
print("output",int(num1)+int(num2))
#print("output", num1+num2)
'''
# 2 area of circle
'''
r= int(input("enter radius"))
print("area of circle: ",3.14*r*r)
'''


# 3 finding roots
'''
a= int(input("enter a value:"))
b= int(input("enter b value:"))
c= int(input("enter c value:"))
d= (b**2)-4*a*c
root1= (-b+(d**0.5))/2*a
root2= (-b-(d**0.5))/2*a
print(f"roots {root1,root2} ")
'''



# 3 finding roots (method 2)
'''
a, b, c = map(int, input("Enter a, b, c values: ").split(","))
d = (b**2) - 4*a*c
root1 = (-b + (d**0.5)) / (2*a)
root2 = (-b - (d**0.5)) / (2*a)
print("Root 1:", root1)
print("Root 2:", root2)
'''


# 4 swapping values using temperary variables
'''
a=int(input("enter a: "))
b=int(input("enter b: "))
print("given values :",a,b,sep=(","))
temp=a
a=b
b=temp

print(f"swapped values :",{a})# sepersate print must used for a as well as for b
print(f"swapped values :",{b})# if a single print is used than values wontb swap.
'''



# 5 swaping two variable without using temperary variable

a=int(input("enter a: "))
b=int(input("enter b: "))
a+=b
b=a-b
a=a-b
print(f"swapped values are:",{a})
print(f"swapped values are:",{b})

#6 temperature conversion
'''
c=float(input(" enter tem in celcious: "))
f= (c*(9/5))+32
k=273+c
print("temper in f: ",f)
print("temper in k: ",k)
'''