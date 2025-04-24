# 1 methods in dictionary
'''
d= {1:"vijay",2:"b",3:"3"}

print(d.keys())
print(d.values())
print(d.items())
print(d.get(1))

d[3]="c" #updating 3rd key value with "c"
print(d.get(3))#checking if updated or not

print(d.pop(3))#pop is nothing but removing
print(d.items())
'''
# 2 looping in dictionary
'''
d= {1:"vijay",2:"b",3:"3"}
for key in d.keys():
    print(key)
for values in d.values():
    print(values)
for keys,values in d.items():# remember the names given in loop same should be given in print
    print(keys,values)
'''

# findingg sum 
'''
l=[10,20,30,40,50]
sum=0
for i in l:
    sum=sum+i
    print(sum)
    '''


# finding max and min
# this is easy method and shortcut one but wont apperciated to use
'''
inp =input().split(",")
l = [int(item) for item in inp]
l.sort()
print(l[-1])
print(l[0])
'''
#or method 2 aslo called as hard method is important
'''
inp=input().split(",")
l=[int(i) for i in inp]
maxi=l[0]
min=l[0]
for i in l:
    if i>maxi:
        maxi=i
    if i<min:
        min=i
print(maxi,min)
'''

# removing duplication
'''
inp=input().split(",")
l=[int(a) for a in inp]
newl=[]
for i in l:
    if i in newl:
        continue
    else:
        newl.append(i)
print(newl)
'''

#method 2 sortcut 
'''
inp = input().split(",")
l = [int(i) for i in inp]
s = set(l)
newl=list(s)
newl.sort()
print(newl)
'''
# for counting an element that is repeating 
'''
inp=input().split(",")
l=[int(i)for i in inp]
r=int(input("enter:")) #r is specific elementthat need to count
c=0
for i in l:
    if i == r:
        c+=1
print(c)
'''
# enter ,update and iterate
my_d={}
n=input("enter name:")
age=int(input("enter age:"))
c=input("enter city:")

my_d["name"]=n
my_d["age"]=age
my_d["city"]=c
print(my_d)

for keys,values in my_d.items():
    print(keys,values)