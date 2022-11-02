"""char= str(input(""))
if char== "a" or char== "b" or char =="c" or char=="d" or char=="e" or char=="f" or char=="g" or char=="h" or char=="i" or char=="j" or char=="k" or char=="l" or char=="m" or char=="n" or char=="o" or char=="p" or char=="q" or char=="r" or char=="t" or char=="u" or char=="v" or char=="w" or char=="x" or char=="y" or char=="z":
    char=char(ord)-32
    char=chr(char)
    print(char)"""

"""num=int(input(""))
increase=0
for i in range(num+1):
    increase=(num-1)*num+i
    print(increase)"""


"""n=float(input(""))
pos=0
neg=0
while n!=0:
    if n>0:
        pos+=n
    elif n<0:
        neg+=n
    n=float(input(""))
print(format(pos, ".3f"))"""

"""import math
num=int(input(""))
square=math.sqrt(num)
num=num//square
print(round(num))"""

"""first=0
second=0
third=0
num1=int(input(""))
num2=int(input(""))
num3=int(input(""))
for i in range(3):
    if num1>first:
        second=first
        first=num1
    elif num2>num1:
        first=second
        first=num2
    elif num3>num2:
        second=third
        second=num3
print(first,second,third)"""

"""import math 
b=float(input(""))
k=int(input(""))
factk=1
for i in range(1,k+1):
    factk=factk*i
answer=((math.e**(-b))*(b**(k)))/factk
print(format(answer, ".3f"))"""

n=int(input(""))
count=0
while True:
    if n==1:
        count+=1
        break
    elif n%2==0:
        n//=2
        count+=1
    elif (n+1)%2==0:
        n=(n*3)+1
        count+=1
print(count)
        
        
    
    
    
        

    
    
    
        
