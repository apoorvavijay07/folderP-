'''expense_list = [2340, 2500, 2100, 3100, 2980]
total = 0
for i in range(len(expense_list)):
    total += expense_list[i]
print("totsl expense is :",total)'''

#1)Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
#area = (1/2)*base*height
'''def cal_triarea(base,height):
    area = 0.5*base*height
    return area

#calulate area of triangle using function call
b=int(input("enter base length:"))
h=int(input("enter height length:"))
tri_area=cal_triarea(b,h)
print(tri_area)'''

#2 Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". 
# Based on shape type it will calculate area. Equation of rectangle's area is,
#rectangle area=length*width
#If no shape is supplied then it should take triangle as a default shape

#creating function
'''def cal_area(shape,dimension1,dimension2):
    if shape== "triangle":
        area = 0.5*dimension1*dimension2
    elif shape == "rectangle":
         area = dimension1*dimension2
    else:
        area = 0
        print("undefine shape area = none ")
    return area

#using function call
shape = input("enter name of shape :")
dim1 = int(input("enter first dimension :"))
dim2 = int(input("enter second dimension :"))
area = cal_area(shape,dim1,dim2)
print(area)  '''

#3 Write a function called print_pattern that takes integer number as an argument and prints  pattern 
# Basically number of lines it prints is equal to that number.
'''def pattern(inp):
    star=""
    for i in range(inp):
        star += "*"
        print(star)
    return None

a = int(input("enter no. of stars :"))
pattern(a)'''

# 4 Write circle_calc() function that takes radius of a circle as an input from user and then it calculates and returns area, 
# circumference and diameter. You should get these values in your main program by calling circle_calc function and then print them

def circle_cal(radius):
    circum=2*3.14*radius
    return circum

r = int(input(" enter radius value:"))
area=circle_cal(r)
print(f"{area:.2f}")
