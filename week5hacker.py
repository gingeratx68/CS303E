#week 5
#count positive and negative numbers
n=int(input(""))
negative=0
postive=0
while n!=0:
    if n>0:
        postive+=1
    elif n<0:
        negative+=1
    n=int(input(""))
print(postive, negative)

#compute future tuition
years=int(input(""))
tuition=10000
sum=0
for i in range(1,years+1):
    tuition=(tuition*1.05)
for j in range(4):
    sum=sum+tuition
    tuition=(tuition*1.05)
print("$",format(sum, ".2f"), sep="")

#dif in highest scores
first=0
second=0
for i in range(5):
    v=int(input(""))
    if v>first:
        second=first
        first=v
    elif v>second:
        second=v       
diff=first-second
print(diff)

#display next characters
character=str(input(""))
add=1
for i in range(10):
    print(chr(ord(character)+add),end=" ")
    add+=1

#odd fractions series
n= int(input(""))
sum=0
for i in range (1,n+1):
    sum+=(((2*i)-1)/((2*i)+1))
print(format(sum, ".2f"))

#abritrary time compound value
savings=float(input(""))
months=int(input(""))
n=savings
for i in range(months):
    total=savings*1.02
    savings=n+total
print("$",format(savings - n, ".2f"), sep="")

#maximum changes
n=int(input(""))
max=0
changes=0
while n!=0:
    if n>max:
        changes+=1
        max=n
    n=int(input(""))
print(changes)

#factorial computation
n=int(input(""))
fact=1
for i in range (1, n+1):
    fact=fact*i
print(fact)

#reccurent sequence
val1=0
val2=1
next=0
n=int(input(""))
if n==1:
    next=val1
elif n==2:
    next=val2
else:
    for i in range (1,n-1):
        temp=val1
        val1=val2
        val2=(((val2)*2)+((temp)*3))
    next=val2
print(next)

#sum divisors
num=int(input(""))
sum=0
for i in range(1,num+1):
    if num % (i)== 0:
        sum=sum+(i)
print(sum)

