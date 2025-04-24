# 1 adding 2 no. using function calling
'''
a= int(input("enter no."))
b= int(input("enter no."))

def sumof2no(a,b):
    print(a+b)
# here only save inputs can be used in arguments (down)
sumof2no(c,d) #if direct no. are given than it will print directly
'''

# 2 find area of circle using function calling
'''
r=int(input("enter radius"))
def areaofcircle(r):
   print(2*3.14*r*r)

areaofcircle(r)
'''
# finding roots using function calling
'''
def roots(x,y,z):
    root1= (-y+(y*y-4*x*z)**0.5)/2*x
    root2= (-y-(y*y-4*x*z)**0.5)/2*x
    print(root1,root2)

a= int(input("enter "))
b= int(input("enter "))
c= int(input("enter "))
roots(a,b,c)
'''

# swaping no. using function call
def swap(a,b):
    #a=int(input("enter a: "))
    #b=int(input("enter b: "))
    a=a+b
    print(a)
    b=a-b
    print(b)
    a=a-b
    
    print(f"swapped values are:",{a})
    print(f"swapped values are:",{b})
x=int(input("enter x: "))
y=int(input("enter y: "))
swap(x,y)

