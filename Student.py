# File: Student.py
# Student: Ginger Hudson 
# UT EID: gsh628
# Course Name: CS303E
# 
# Date: 3/18/20
# Description of Program: input of student name and 2 exam grades to output student average grade

class Student:
    def __init__(self,name, Exam1Grade=None, Exam2Grade=None):
        self.__name=name
        self.__Exam1Grade= Exam1Grade
        self.__Exam2Grade= Exam2Grade

    def __str__(self):
        return "Student: {} \n  Exam1: {} \n  Exam2: {}".format(self.__name, self.__Exam1Grade, self.__Exam2Grade)    
    def getName(self):
        #retrieve student name
        return self.__name

    def getExam1Grade(self):
        #retrieve exam one grade 
        return self.__Exam1Grade
    def setExam1Grade(self, Exam1Grade):
        #set amd update the exam 1 grade
        self.__Exam1Grade=Exam1Grade
    
    def getExam2Grade(self):
        #retrieve the exam 2 grade
        return self.__Exam2Grade
    def setExam2Grade(self, Exam2Grade):
        #set and update the exam 2 grade
        self.__Exam2Grade=Exam2Grade

    def getAverage(self):
        #if there are two grades, find the average 
        if self.__Exam1Grade== None or self.__Exam2Grade== None:
            print("Some exam grades not available.")
        # when one or more exam grades not available
        else:
            return (self.__Exam1Grade + self.__Exam2Grade)/2
        
        
