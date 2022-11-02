# File: Payroll.py
# Student: Ginger Hudson
# UT EID: gsh628
# Course Name: CS303E
# 
# Date: 2/8/22
# Description of Program: reads in employee information to write a payroll

#print("Payroll")
print()
#Employee's name (e.g., Smith)
employeename= str(input("Enter employee's name: "))
#Number of hours worked in a week (e.g., 10)
hoursworked= float(input("Enter number of hours worked in a week: "))
#Hourly pay rate (e.g., 9.75
hourlyrate= float(input("Enter hourly pay rate: "))
#Federal tax withholding rate (e.g., 20%)
federaltax= float(input("Enter federal tax withholding rate: "))
#State tax withholding rate (e.g., 9%)
statetax= float(input("Enter state tax withholding rate: "))
print()
grosspay = float(hoursworked*hourlyrate)
federaltaxamount = float(grosspay * federaltax)
statetaxamount = float(grosspay * statetax)
netpay = float(grosspay - statetaxamount - federaltaxamount)
netdeduction = float(statetaxamount + federaltaxamount)
print("Employee Name:", employeename)
print("Hours Worked:", hoursworked)
print("Pay Rate: $",hourlyrate, sep="")
print("Gross Pay: $",format(grosspay, ".2f"), sep="")
print("Deductions: ")
print("  Federal Withholding: $",format(federaltaxamount,".2f"), sep="")
print("  State Withholding: $",format(statetaxamount,".2f"), sep="")
print("  Total Deduction: $",format(netdeduction, ".2f"), sep="")
print("Net Pay: $",format(netpay, ".2f"), sep="")

