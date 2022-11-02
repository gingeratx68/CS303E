#WEEK 4 IF,ELSE
#cramers rule
a= int(input(""))
b=int(input(""))
c=int(input(""))
d=int(input(""))
e=int(input(""))
f=int(input(""))
condition=((a*d)-(b*c))
if (condition == 0): 
    print("The equation has no solution")
else:
    x=((e*d)-(b*f))/(condition)
    y=((a*f)-(e*c))/(condition)
    float(x)
    float(y)
    print("x is " + format(x, ".1f") + " and y is " + format(y,".1f"))

#find future dates
current=int(input(""))
elapsed =int(input(""))
futureday = ((current + elapsed) % 7)

if current==(0):
    current="Sunday"
if current==(1):
    current="Monday"
if current==(2):
    current=("Tuesday")
if current==(3):
    current=("Wednesday")
if current==(4):
    current=("Thursday")
if current==(5):
    current=("Friday")
if current==(6):
    current=("Saturday")

if futureday==0:
    futureday=("Sunday")
if futureday==1:
    futureday=("Monday")
if futureday==2:
    futureday=("Tuesday")
if futureday==3:
    futureday=("Wednesday")
if futureday==4:
    futureday=("Thursday")
if futureday==5:
    futureday=("Friday")
if futureday==6:
    futureday=("Saturday")
print("Today is " + format(current) + " and the future day is",format(futureday))
#compare costs
weight1= float(input(""))
price1=float(input(""))
weight2=float(input(""))
price2=float(input(""))
if ((price1/weight1) < (price2/weight2)):
    print("1")
else:
    print("2")

#perimeter of triangle
edge1= int(input(""))
edge2= int(input(""))
edge3= int(input(""))
if edge1+edge2<=edge3 or edge2+edge3<=edge1 or edge1+edge3<=edge2:
    print("The input is invalid")
elif (edge1<0):
    print("The input is invalid")
elif (edge2<0):
    print("The input is invalid")
elif (edge3<0):
    print("The input is invalid")
else:
    perimeter=edge1+edge2+edge3
    print("The perimeter is {}".format(perimeter))

#point in a circle
import math
x= float(input(""))
y=float(input(""))
distance=math.sqrt((x**2)+(y**2))
if distance <= 10: 
    print("IN")
else:
    distance > 10
    print("OUT")

#point in a rectangle
x= float(input(""))
y=float(input(""))
if (x<= 5) and (y<= 2.5) and (x>= -5) and (y>= -2.5):
    print("IN")
else:
    print("OUT")

#three digit palindrome number
value= int(input(""))
x1=value%10
x2=value//10
x3=x2//10
if (x1==x3):
    print("YES")
else:
    print("NO")

#decimal to hex
hex = int(input(""))
if (hex == 0):
    print("0")
elif (hex == 1):
    print("1")
elif (hex == 2):
    print("2")
elif (hex == 3):
    print("3")
elif (hex == 4):
    print("4")
elif (hex == 5):
    print("5")
elif (hex == 6):
    print("6")
elif (hex ==7):
    print("7")
elif (hex == 8):
    print("8")
elif (hex == 9):
    print("9")
elif (hex == 10):
    print("A")
elif (hex == 11):
    print("B")
elif (hex == 12):
    print("C")
elif (hex == 13):
    print("D")
elif (hex == 14):
    print("E")
elif (hex == 15):
    print("F")

#cosonant or vowel
test= input(str(""))
if (test ==  "a" or test == "e" or test == "i" or test == "o" or test == "u" or test == "A" or test == "E" or test == "I" or test =="O" or test =="U"):
    print("vowel")
else:
    print("consonant")

#name that triangle
a= int(input(""))
b= int(input(""))
c=int(input(""))
a>0
b>0
c>0
if int((a==b and a==c and b==c)):
    print("equilateral")
elif a==b or a==c or b==c:
    print("isosceles")
else:
    print("scalene")

#identify the season
month= str(input(""))
day= int(input(""))
if month == "March" and day >= 20:
    print ("spring")
elif month=="April" and day >= 1:
    print("spring")
elif month=="May" and day>= 1:
    print("spring")
elif month== "June" and day<=20:
    print("spring")
elif month=="June" and day>=21:
    print("summer")
elif month=="July" and day>=1:
    print("summer")
elif month=="August" and day>=1:
    print("summer")
elif month=="September" and day<=21:
    print("summer")
elif month== "September" and day>= 22:
    print("fall")
elif month== "October" and day>=1:
    print("fall")
elif month=="November" and day>=1:
    print("fall")
elif month=="December" and day<=20:
    print("fall")
elif month=="December" and day>= 21:
    print("winter")
elif month=="January" and day>=1:
    print("winter")
elif month=="February" and day>=1:
    print("winter")
elif month=="March"

#shipping costs
country=str(input(""))
state=str(input(""))
if country=="United States" and state!= "Hawaii" and state!="Alaska":
    print("$5")
elif country=="United States" and state=="Hawaii" or state=="Alaska":
    print("$10")
elif country!="United States" and state!= "Hawaii" and state!="Alaska":
    print("$20")

#text abbreviations
abb=str(input(""))
if abb=="LOL":
    print("laugh out loud")
elif abb=="BRB":
    print("be right back")
elif abb=="NBD":
    print("no big deal")
elif abb=="TBH":
    print("to be honest")
elif abb=="IIRC":
    print("if I recall correctly")
elif abb=="UT":
    print("University of Texas")

#ticket pricing
day= str(input(""))
age= int(input(""))
if ((day=="Sunday") or (day=="Tuesday") or (day=="Wednesday") or (day=="Friday") or (day=="Saturday")) and (age>=65): 
    print("$10")
elif ((day=="Thursday") or (day=="Monday")) and (age>=65):
    print("$7")
elif ((day=="Sunday") or (day=="Monday") or (day=="Tuesday") or (day=="Wednesday") or           (day=="Friday") or (day=="Saturday")) and (age<=10):
    print("$10")
elif (day=="Thursday") and (age<=10): 
    print("$5")
else:
    if (day=="Sunday") or (day=="Monday") or (day=="Tuesday") or (day=="Wednesday") or (day=="Thursday") or (day=="Friday") or (day=="Saturday"):
        print("$15")

#overtime
wage=float(input(""))
hours=float(input(""))
if hours<40:
    pay=wage*hours
    print("$",format(pay, ".2f"), sep="")
elif hours>40:
    hours1=hours-40
    overtimepay=(wage*1.5)
    pay=(overtimepay*hours1)+(wage*40)
    print("$",format(pay, ".2f"), sep="")

#convert temp
convo=str(input(""))
temp=float(input(""))
if convo=="F":
    new=(5/9)*(temp-32)
    print(format(new, ".1f"))
elif convo=="C":
    new=((9/5)*(temp))+32
    print(format(new, ".1f"))

#fizzbuzz
n= int(input(""))
if (n%3==0) and (n%5>0):
    print("Fizz")
elif (n%5==0) and (n%3>0):
    print("Buzz")
elif (n%3==0) and (n%5==0):
    print("FizzBuzz")
else:
    print(n)
