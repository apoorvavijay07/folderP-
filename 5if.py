#1)Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
#i)Ask user to enter his fasting sugar level
#ii)If it is below 80 to 100 range then print that sugar is low
#iii)If it is above 100 then print that it is high otherwise print that it is normal

'''
print("enter sugar level :")
sugar = int(input())
if (sugar > 100):
    print("yor sugar is high")
elif (80<=sugar<=100 ):
    print("your sugar is low")
else:
    print("your sugar is normal")
'''

''' 2) Using following list of cities per country,

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

i) Write a program that asks user to enter a city name and it should tell which country the city belongs to
ii) Write a program that asks user to enter two cities and it tells you if they both are in same country or not. 
For example if I enter mumbai and chennai, it will print "Both cities are in India" 
but if I enter mumbai and dhaka it should print "They don't belong to same country"     '''

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
# to check one city
'''city =input("enter the city name :")
if (city in india):
    print("this city is in india")
elif (city in pakistan):
    print("this city is in pakistan")
elif (city in bangladesh):
    print("this city is in bangladesh")
else:
    print("none")'''


# to check two cities
city1 =input("enter the city1 name :")
city2 =input("enter the city2 name :")
if (city1 in india):
    if(city2 in india):
         print("both cities in india ")
    else:
        print(" naot in same contry")
elif (city1 in pakistan):
    if(city2 in pakistan):
        print("both cities in pakistan ")
    else:
        print(" naot in same contry")
elif (city1 in bangladesh):
    if(city2 in bangladesh):
        print("both cities in bangladesh ")
    else:
         print(" naot in same contry")
else:
    ("both cities not in same country")