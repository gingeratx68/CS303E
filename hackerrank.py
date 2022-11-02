print("hackerrank")
#WEEK 2 PRACTICE

#compute simple expression
tot= float(9.5*4.5-2.5*3)/(45.5-3.5)
print(tot)
#powers table
print("a    a^2   a^3")
print("1    1     1  ")
print("2    4     8  ")
print("3    9     27 ")
print("4    16    64 ")

#simple finite series summation
tot2= int(1+2+3+4+5+6+7+8+9)
print(tot2)
#approximate Pi
answer = float(4*(1-1/3+1/5-1/7+1/9-1/11))
print(answer)
answer2 = float(4*(1-1/3+1/5-1/7+1/9-1/11+1/13-1/15))
print(answer2)
#five year population projection
currentpop = int(373582814)
oneyear =  int(int(31536000*((1/6) - (1/15) + (1/45))) + currentpop)
print(oneyear)
secondyear= int(int(31536000*((1/6) - (1/15) + (1/45))) + oneyear)
print(secondyear)
thirdyear=  int(int(31536000*((1/6) - (1/15) + (1/45))) + secondyear)
print(thirdyear)
fourthyear=  int(int(31536000*((1/6) - (1/15) + (1/45))) + thirdyear)
print(fourthyear)
fifthyear=  int(int(31536000*((1/6) - (1/15) + (1/45))) + fourthyear)
print(fifthyear)

#WEEK 3 PRACTICE

#celsius to fahrenheit
celsius = float(input(""))
fahrenheit = (celsius*9/5) + 32
print(format(fahrenheit, ".1f"))

#area and volume of a cylinder
import math
radius= float(input(""))
length= float(input(""))
area=(math.pi*radius**2)
volume=(area*length)
print(format(area, ".2f"))
print(format(volume, ".2f"))

#calculate tips
subtotal = float(input(""))
gratuityrate= float(input(""))
gratuity= subtotal*(gratuityrate/100)
total= subtotal + gratuity
print("$", format(gratuity, ".2f"),sep="")
print("$", format(total, ".2f"),sep="")

#sum digits in an integer
randomnumber= str(input(""))
x1= randomnumber%10
x2= randomnumber//10
x3= x2%10
x4= x2//10
print(x1+x3+x4)

#number of years and days
m= int(input(""))
y= m //(24*60*365)
d = (m%(24*60*365)//(24*60))
print("{} minutes is approximately {} year(s) and {} day(s)". format(m,y,d))

#calculate energy 
kilograms= float(input(""))
initialtemp= float(input(""))
finaltemp= float(input(""))
energy=kilograms*(finaltemp-initialtemp)*4184
print(format(energy, ".1f"))

#windchill temperature
temp=float(input(""))
windspeed=float(input(""))
windchill=(35.74 + (0.6215 * temp) - 35.75 * (windspeed** 0.16) + 0.4275 * temp * (windspeed** 0.16))
print(format(windchill, ".1f"))

#runway length
v= float(input(""))
a=float(input(""))
length=(v**2)/(2*a)
print(format(length, ".3f"))

#split digits
four=int(input(""))
x1=four%10
x2=four//10
x3=x2%10
x4=x2//10
x5=x4%10
x6=x4//10
print(x1)
print(x3)
print(x5)
print(x6)

#calculate area of a triangle
x1=float(input(""))
y1=float(input(""))
x2=float(input(""))
y2=float(input(""))
y3=float(input(""))

#body mass index
weight=float(input(""))
height=float(input(""))
weight2= weight*0.45359237
height2= height*0.0254
bmi= weight2/ height2**2
print(format (bmi, ".1f"))

#compound value
savings=float(input(""))
month1=savings*(1 + 0.00417)
month2=(savings+month1)*(1 + 0.00417)
month3=(savings+month2)*(1 + 0.00417)
month4=(savings+month3)*(1 + 0.00417)
month5=(savings+month4)*(1 + 0.00417)
month6=(savings+month5)*(1 + 0.00417)
print("$",format(month6, ".2f"),sep="")

#arbitrary year population
years= int(input(""))
sample=int(31536000*years*((1/6) - (1/15) + (1/45)) + (373582814))
print(sample)

#area of a pentagon
import math
r= float(input(""))
s=2*r*math.sin(math.pi/5)
area= (3*math.sqrt(3)*(s**2))/2
print(format(area, ".2f"))

#area of a hexagon
import math
s= float(input(""))
area=(3*math.sqrt(3)/(2))*(s**2)
print(format(area, ".4f"))

#calculate area of a triangle
import math
x1=float(input(""))
y1=float(input(""))
x2=float(input(""))
y2=float(input(""))
x3=float(input(""))
y3=float(input(""))
side1=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
side2=math.sqrt(((x2-x3)**2)+((y2-y3)**2))
side3=math.sqrt(((x3-x1)**2)+((y3-y1)**2))
s=(side1+side2+side3)/2
area=(math.sqrt((s*(s-side1))*(s-side2)*(s-side3)))
print(format(area, ".1f"))


