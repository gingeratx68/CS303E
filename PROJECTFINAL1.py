# File: Project1.py
# Student: Ginger Hudson
# UT EID: gsh628
# Course Name: CS303E
# 
# Date: 2/4/22
# Description of Program: Metric/English length converter

import sys
""" assorted unit conversions used later
"""
feet_to_meter= .3048
meter_to_feet= 3.28084
mile_to_feet= 5280
feet_to_miles= float(1/5280)
feet_to_inch= 12
meter_to_cm=100
cm_to_meter= float(1/100)
inches_to_feet= float(1/12)
kilo_to_meters= 1000
feet_to_kilo=1
feet_to_cm=1
meter_to_kilo= float(1/1000)

def intro():
    """
    print intro statement x1
    """
    print("Welcome to the English/Metric conversion utility.\n")
    print("This utility allows you to convert between English units")
    print("(miles, feet, inches) and metric units (kilometers, meters,")
    print("centimeters)\n")
    print("-" *60)
   
def step1():
    """
    enter first conversion level of 1, 2, or 3 (quit)
    """
    print("\nWhich direction would you like to convert:")
    print("   For English to Metric type: 1")
    print("   For Metric to English type: 2")
    print("   To Quit type:               3\n")
    return input("   Input your answer (1, 2 or 3): ")
    

def check_input(_user_input):
    """
    check if the input is= 1, 2, or 3
    """
    if _user_input in ["1","2","3"]:
        return int(_user_input)
    print()
    print("ERROR: Answer must be 1, 2 or 3. Try again.")
    return 0
    
def englishMetric():
    """
    if the input in check_input is 1, english units to metric 
    """
    print("\nSelect English units to convert to metric equivalent:")
    print("   For miles type:  1")
    print("   For feet type:   2")
    print("   For inches type: 3\n")
    return input("   Choose English units to convert (1, 2 or 3): ")

def cnvrtMetric():
    """
    check_input = 1 and now where are we converting to in the metric units
    """
    print("\nConvert to which metric units:")
    print("   For kilometers type:  1")
    print("   For meters type:      2")
    print("   For centimeters type: 3\n")
    return input("   Choose target metric units (1, 2 or 3): ")

def metricEnglish():
    """
    if the input in check_input is 2, metric units to english
    """

    print("\nSelect metric units to convert to English equivalent:")
    print("   For kilometers type:  1")
    print("   For meters type:      2")
    print("   For centimeters type: 3\n")
    return input("   Choose metric units to convert (1, 2 or 3): ")

def cnvrtEnglish():
    """
    check_input = 2 and now where are we converting to in the english units
    """
    print("\nConvert to which English units:")
    print("   For miles type:  1")
    print("   For feet type:   2")
    print("   For inches type: 3\n")
    return input("   Choose target English units (1, 2 or 3): ")  

def calc_englishtoM(_eng_type, _met_type):
    """
    convert everything to FEET first and then metric
    """
    engname=get_engname(_eng_type)
    metname=get_metname(_met_type)
    con_num=float(input("\nEnter the number of %s to convert to %s: " % (engname,metname)))
    num_feet= con_num
    #conversions to feet 
    if _eng_type == 1:
        num_feet=con_num*mile_to_feet
    elif _eng_type == 3:
        num_feet=con_num*inches_to_feet

    #conversions from feet to metric system     
    result=num_feet*feet_to_meter
    if _met_type== 1:
        result=result*meter_to_kilo
    elif _met_type==3:
        result=result*meter_to_cm

    print("\nRESULT: %s %s = %.3f %s" %(con_num, engname, result, metname))
        
def calc_metrictoE(_eng_type, _met_type):
    """
    convert everything to METERS first then metric
    """
    engname=get_engname(_eng_type)
    metname=get_metname(_met_type)
    con_num= float(input("\nEnter the number of %s to convert to %s: " % (metname,engname)))
    num_meters= con_num
    #conversion to meters
    if _met_type == 1:
        num_meters= con_num*kilo_to_meters
    elif _met_type== 3:
        num_meters= con_num*cm_to_meter
    
    #conversion from meters to english system

    result=num_meters*meter_to_feet
    if _eng_type==1:
        result=result*feet_to_miles
    elif _eng_type==3:
        result=result*feet_to_inch

    
    print("\nRESULT: %s %s = %.3f %s" %(con_num, metname, result, engname))
    
      
def get_engname(_eng_type):
    """
    establishing in english to metric, what measurment name that 1,2, and 3 stand for
    so that it can be used in the RESULT print statement 
    """
    if _eng_type==1:
        return "miles"
    elif _eng_type==2:
        return "feet"
    elif _eng_type==3:
        return "inches"
    
    
def get_metname(_met_type):
    """
    establishing in metric to english, what measurment name that 1,2, and 3 stand for
    so that it can be used in the RESULT print statement 
    """
    if _met_type==1:
        return "kilometers"
    elif _met_type==2:
        return "meters"
    elif _met_type==3:
        return "centimeters"
    
def main():
    intro()
    while True:
        cnvrt_type=0
        eng_type=0
        met_type=0
        #setting to zero ensures that the code repeats converting after one conversion is performed 
        while cnvrt_type==0:
            cnvrt_type = check_input(step1())
            #so that converter continues to repeat after first conversion
        if cnvrt_type==3:
            print("\nThanks for using our converter. Goodbye!")
            return 0
            #converter quit 
        elif cnvrt_type==1:
            while eng_type==0:
                eng_type = check_input(englishMetric())
            while met_type==0:
                met_type = check_input(cnvrtMetric())
            calc_englishtoM(eng_type, met_type)
            #converter english to metric 
        elif cnvrt_type==2:
            while met_type==0:
                met_type= check_input(metricEnglish())
            while eng_type==0:
                eng_type = check_input(cnvrtEnglish())
            calc_metrictoE(eng_type, met_type)
            #converter metric to english
        print("\n%s" % str("-"*60))
        #reseting cnvrt_type back to zero so that program keeps running

        #cnvrt_type=0
        #met_type=0
        #eng_type=0

if __name__== "__main__":
    sys.exit(main())
