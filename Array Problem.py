# FDS_Array_Problem

'''Write a Python program to store marks scored in subject "FDS" by N student in the class. Write functions to compute following: 
a) The average score of class 
b) Highest score and lowest score of class 
c) Count of students who were absent for the test 
d) Display marks with highest frequency using array in python'''


import array as ar

# Funcion to count no of Students absent for test 

def absentSC(listOfStudent, numberOfStudent):

    count = 0

    for i in range(numberOfStudent):

        if listOfStudent[i]==0:

            count +=1

    return count
  
  # Function for Calculating Average

 def averageOfMarks(listOfStudent, numberOfStudent):

    sumInitialize = 0

    for i in range(numberOfStudent):

        sumInitialize += listOfStudent[i]



    return (sumInitialize/numberOfStudent)
  
  
