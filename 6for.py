#1After flipping a coin 10 times you got this result,Using for loop figure out how many times you got heads

'''result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
c = 0
for i in (result):
    if i == "heads" :
        c += 1
print(c)'''

#2 Print square of all numbers between 1 to 10 except even numbers

'''for i in range(1,10):
    if i%2!=0:
        print(i*i)'''

#3 Your monthly expense list (from Jan to May) looks like this,

#Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. 
#If expense is not found then it should print that as well.

'''expense_list = [2340, 2500, 2100, 3100, 2980]
month_name = ["jan","feb","mar","apr","mayi"]
expense =int(input("Enter the expense amount:"  ))
month = -1
for i in range(len(expense_list)):
    if expense == expense_list[i]:
        month += 1
        break
if month != -1:
    print(f"the expense {expense} occured in {month_name[month]}")
else:
    print("not occured")'''

#4 Lets say you are running a 5 km race. Write a program that,

# i)Upon completing each 1 km asks you "are you tired?"
#ii)If you reply "yes" then it should break and print "you didn't finish the race"
#iii)If you reply "no" then it should continue and ask "are you tired" on every km
#iv) If you finish all 5 km then it should print congratulations message
'''
for i in range(5):
    print(f"you ran {i+1}km")
    reply = input(" are you tired ? 'yes' or 'no' ")
    if reply == "yes":
        print("you didn't finish the race")
        break
if(i == 4):
    print(" hurry you fineshed race")  '''
#else:
  #  print("you didn't finish the race")

# 5)Write a program that prints following shape
'''
*
**
***
****
*****       '''
s = ""
inp = int(input("enter no. of *:")) # here for this Q  inp = 5
for i in range(inp):
    s += "*"
    print(f"{s}")

    

