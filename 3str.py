## Exercise: String in Python

#1. Create 3 variables to store street, city and country, now create address variable to
#store entire address. Use two ways of creating this variable, one using + operator and the other using f-string.
#Now Print the address in such a way that the street, city and country prints in a separate line
street = "abc street"
city = "abc city"
country = "a"
addr=(street +"\n" +city +"\n" +country)
print(addr)
addr1=print(f"\n{street}\n{city}\n{country}")



#2. Create a variable to store the string "Earth revolves around the sun"
#   1. Print "revolves" using slice operator
#   2. Print "sun" using negative index
s= "Earth revolves around the sun"
print(s[6:14])
print(s[-3:])


#3. Create two variables to store how many fruits and vegetables you eat in a day.
#Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.

'''veg,fru=map(int,input().split(","))
print(f"I eat {veg} veggies and {fru} fruits daily")'''

'''4. I have a string variable called s='maine 200 banana khaye'. This of course is a
wrong statement, the correct statement is 'maine 10 samosa khaye'.
Replace incorrect words in original strong with new ones and print the new string.
Also try to do this in one line.'''

s= "maine 200 banana khaye"
print(s)
print(s.replace("200","10").replace("banana","samosa"))




#[Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/4_strings/4_string_exercise_answer.py)