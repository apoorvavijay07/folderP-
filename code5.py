# 1 printing stringindexing 
'''
name = input("enter NAME:")
print(name)    # python
print(name[1])     # y [start:stop:step]
print(name[-1])   # n
print(name[1:-1]) # ytho
print(name[1:3])  # yt
print(name[1:-3]) # yt
print(name[:3])   # pyt
print(name[2:])   #pyt
print(name[:-1])  #pytho
print(name[::2])  #pto
print(name[1::2]) #yhn
print(name[::-1]) #nohtyp

s="hello world"
print(s[::-1])
'''
#2 sting concatenation
'''
name1 = (input())
name2 = (input())
full_name = name1+name2
print(full_name) #output will be not arithemetic opt but will be printing combined 
'''
# 3 printing length of string
'''
name1 = (input())
name2 = (input())
full_name = name1+name2
print(full_name) 
print(len(full_name))#len() is used to find to sting length and need to enter with print for value printing
'''

#4 string methods
'''
s="hello WORld"
print(s)
print(s.upper())

print(s.lower())
print(s.count("o"))
print(s.count("o" ))
print(s.strip())
print(s.replace("o","x"))
print(s.find("e"))
print(s.find("e"))
print(s.rfind("h"))
print(s.rindex("h"))
'''
# 5 vowels counter
'''
s= input()
s1=s.lower()
a=s1.count("a")
e=s1.count("e")
i=s1.count("i")
o=s1.count("o")
u=s1.count("u")
print(f"no. of vowels : {a+e+i+o+u}")
'''
# 6 awarding grades based on marks
'''
M1= float(input("marks in sub1:"))
M2= float(input("marks in sub2:"))
M3= float(input("marks in sub3:"))
t=M1+M2+M3
print(f"total marks: {t}")
print(f"average marks: {t/3}")
p=(t/300)*100
if(p>90):
    print("grade: A")
elif(90>p>80):   
    print("grade: B")
elif(80>p>70):   
    print("grade: C")
elif(70>p>60):   
    print("grade: D")
else: 
    print("grade: E")

#or

M1= float(input("marks in sub1:"))
M2= float(input("marks in sub2:"))
M3= float(input("marks in sub3:"))
t=M1+M2+M3
print(f"total marks: {t}")
print(f"average marks: {t/3}")
p=(t/300)*100
grade = ""
if(p>90):
    grade = "A"
elif(90>p>80):   
    grade = "B"
elif(80>p>70):   
    grade = "C"
elif(70>p>60):   
    grade = "D"
else: 
    grade = "E"
print(grade)
'''
# 7 checking palindrome 
'''
name = input("enter name: ")
if(name == name[::-1] ): #st.[::-1] revers the string
    print(" given name is parandrom")
else:
    print(" it\'s not parandrom ")
'''
# 8 finding the greatest number
'''
#n1= int(input("enter 1st no:"))
#n2= int(input("enter 2nd no:"))
#n3= int(input("enter 3rd no:"))
n1,n2,n3 = map(int,input("enter 3 no:").split(","))
if (n1>n2 and n1>n3):
    print(f"{n1}is greater")
#elif (n1>n3):
 #   print(f"{n1}is greater")
elif (n2>n1 and n2>n3):
    print(f"{n2 }is greater")
#elif (n2>n3):
 #   print(f"{n2 }is greater")
elif (n3>n1 and n3>n2):
    print(f"{n3 }is greater")
#elif (n3>n2):
 #   print(f"{n3 }is greater")
else:
    print("some no. are equal")
'''
# 9 finding leap year
# here a leap year is divisible by 4;for century  years they must be divisible by 400
year= int(input("enter year:"))
r=year%4 #to check  general leap year
r1=year%100 #for identifing century years
r2=year%400 #for checking century year as leap year or not
if(r1 == 0): 
    print("its century year")
    if(r2 == 0):
        print("given year is leap year")
    else:
        print("given year is not leap year")
elif(r == 0):
    print("given year is leapyear")
else:
    print("not a leap year")