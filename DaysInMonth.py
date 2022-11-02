print("DaysInMonth")
# File: DaysInMonth.py
# Student: Ginger Hudson 
# UT EID: gsh628
# Course Name: CS303E
# 
# Date: 2/17/22
# Description of Program: Compute days in month froom year and month input

year= int(input("Please enter a year: "))
month= int(input("Please enter a month: "))

if month ==1:
    print("January {} has 31 days".format(year))
if month ==2:
    if((year%4==0) and (year%100!=0)) or (year%400==0):
        print("February {} has 29 days".format(year))
    else:
        print("February {} has 28 days".format(year))
if month ==3:
    print("March {} has 31 days".format(year))
if month ==4:
    print("April {} has 30 days".format(year))
if month ==5:
    print("May {} has 31 days".format(year))
if month ==6:
    print("June {} has 30 days".format(year))
if month ==7:
    print("July {} has 31 days".format(year))
if month ==8:
    print("August {} has 31 days".format(year))
if month ==9:
    print("September {} has 30 days".format(year))
if month ==10:
    print("October {} has 31 days".format(year))
if month ==11:
    print("November {} has 30 days".format(year))
if month ==12:
    print("December {} has 31 days".format(year))

