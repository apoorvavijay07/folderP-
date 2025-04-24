# 1 print n natural numbers using for loops
'''
n= int(input("enter natural no:"))
i= 1
while(i <= n):
    print( i )
    i += 1
'''    
# print n natural numbers using for loops
'''
n= int(input("enter natural no:"))
for i in range(1,n+1):
   print(i) 
   '''
# 2 printing sum of n numbers
'''
n= int(input("enter no:"))
i=1
sum = 0
while (i <= n):
    
    sum = sum+i
    i+=1 
    print(sum)
'''
#3 printing only odd numbers
'''
n= int(input("enter natural no:"))
i= 0
while(i <= n ):
    i += 1
    if(i%2==1):
        print(i)
    continue
'''
# 4 priting tables
'''
n= int(input("enter number:"))
i = 1
while(i<11):
    print(f"{n}*{i}={n*i}")
    i += 1
'''
n= int(input("enter number:"))
f=1
while(n>f):
     f=f*n
     n-= 1
     print(f)
'''
n= int(input("enter number:"))
i = 1
f=1
f1=0
while(i<=n):
     f=i*f
     i+=1
     print(f)
     '''