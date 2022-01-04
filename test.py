'''a = str(input())
b = str(input())

if len(a) > len (b):
    sm = b 
else:
    sm = a 
c = 0  
l = len(sm)
for i in range(l):
    if a[i] == b[i]:
        c = c+1 
    
print(c)'''

'''
s1=input("enter:")
s2=input("enter val2:")
if len()
for i in range(len(s1)):
    count=0
    
    for j in range(1,i+1):
        if s1[i]==s2[j]:
            count=count+1
print(count)
'''
'''
a="11111111"  #input("enter 0 or 1")
b="00000100"#input("enter 0 or 1")
count=0
if len(a)<=len(b):
    for i in range(len(a)):
        for j in range(i,i+1):
            if a[i]==b[j]:
                count=count+1

print(count)




# Python Program to find Strong Number using for loop
  
Num = int(input(" Please Enter any Number: "))
Sum = 0
Temp = Num
 
while(Temp > 0):
    Factorial = 1
    Reminder = Temp % 10
 
    for i in range(1, Reminder + 1):
        Factorial = Factorial * i
 
    print("Factorial of %d = %d" %(Reminder, Factorial))
    Sum = Sum + Factorial
    Temp = Temp // 10
 
print("\n Sum of Factorials of a Given Number %d = %d" %(Num, Sum))
     
if (Sum == Num):
    print(" %d is a Strong Number" %Num)
else:
    print(" %d is not a Strong Number" %Num)
'''
'''

num=int(input("Enter:"))
e=int(input("End num:"))
temp=num
s=0
c=len(str(num))
for j in range(num,e+1):
    fact=1
    for i in range()
    rem=j%10
    
    for i in range(1,rem+1):
        fact=fact*i
    s=s+fact
temp=temp//10

if s==num:
    print(num)
    
   ''' 
'''
    
a=1#int(input("enter the 1 value"))
b=100000
#int(input("enter the 2 value"))
p=0
for i in range(a,b+1):
    
    temp=i
   
    d=str(i)
    c=len(d)
    for j in range(c):
       
        r=i%10
        i=i//10
      
        j=1
        for k in range(1,r+1):
            j=j*k
       
        p=p+j
   
    if temp==p:
        p=0
        print(temp,":strong")
    else:
        p=0
        '''
        
'''       
n=int(input("Enter:"))
i=1
j=0
while(i<=n):
    j=j+i
    i=i+1
print(j)
'''


b="sivadurga"
c=int(len(b)/2)
s=""
a="topper"
for i in range(len(b)):
    if i<c:
        s=s+b[i]
    elif i==c:
        s=s+a
        
    if i>=c:
        s=s+b[i]
print(s)