# You are given following list of stocks and their prices in last 3 days,

'''Stock	Prices
info	[600,630,620]
ril	[1430,1490,1567]
mtl	[234,180,160]   '''
#   i) Write a program that asks user for operation. Value of operations could be,
    #print: When user enters print it should print following,
'''info ==> [600, 630, 620] ==> avg:  616.67
ril ==> [1430, 1490, 1567] ==> avg:  1495.67
mtl ==> [234, 180, 160] ==> avg:  191.33'''
#   ii)add: When user enters 'add', it asks for stock ticker and price. 
# If stock already exist in your list (like info, ril etc) then it will append the price to the list. 
# Otherwise it will create new entry in your dictionary. 
# For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.
'''

d = {"info":[600,630,620],"ril":[1430,1490,1567],"mtl":[234,180,160] }
def printt():
    for keys,values in d.items():
        avg=sum(values)/len(values)
        print(f"{keys}==>{values}==>{avg:.2f}")

def add():
    s=input("enter stock ticker: ")
    p=input("enter price: ")
#p=float(p)
    if s in d:
        print(" already listed")
    else:
        d.setdefault(s,[]).append(p)
    #d(s,[]).append(p)
        print(d)

opt=input("enter operation either add or print:")
if opt == "add":
    add()
elif opt == "print":
    printt()
else:
    print("invalid operation",opt)
 '''

#3 We have following information on countries and their population (population is in crores),

'''Country	Population
China	143
India	136
USA	    32
Pakistan	21 '''

#Using above create a dictionary of countries and its population
# i)Write a program that asks user for three type of inputs,
#print: if user enter print then it should print all countries with their population in this format,
'''china==>143
india==>136
usa==>32
pakistan==>21 '''
#ii) add: if user input add then it should further ask for a country name to add.
#  If country already exist in our dataset then it should print that it exist and do nothing.
#  If it doesn't then it asks for population and add that new country/population in our dictionary and print it
#iii) remove: when user inputs remove it should ask for a country to remove.
#  If country exist in our dictionary then remove it and print new dictionary using format shown above in 
# (a). Else print that country doesn't exist!
#iv) query: on this again ask user for which country he or she wants to query.
#  When user inputs that country it will print population of that country.

country_dict = { "china":143,"india":136,"usa":32,"pakistan":21} 

def printt():
    for keys,values in country_dict.items():
        print(f"{keys}==>{values}")

def add():
    country = input("enter name of country:")
    country=country.lower()
    if country not in country_dict:
      popu = input("enter no. of population:")
      country_dict.setdefault(country,[]).append(popu)
    #print(country_dict)
      for keys,values in country_dict.items():
             print(f"{keys}==>{[values]}")
    else:
     print("country already exists" )

def remove():

    country = input("enter name of country to be removed :")
    country=country.lower()
    if country  in country_dict:
        country_dict.pop(country)
        for keys,values in country_dict.items():
             print(f"{keys}==>{[values]}")
    else:
     print(" country not found ")

def query():
    country = input("enter name of country for queary:")
    country=country.lower()
    if country in country_dict:
         print(country_dict[country])
    else:
        print("country is not listed in data")

opt = input(" enter the operation to perform :")
if opt == "print":
    printt()
elif opt == "add":
    add()
elif opt == "remove":
    remove()
elif opt == "query":
    query()
else:
    print(" invalid operation",opt)


