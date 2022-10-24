#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    
    for i in range(0,len(grades)):
        x = 5 * math.ceil(grades[i] / 5)
        diffy = x - grades[i]
        
        if grades[i] < 38 or diffy >= 3:
            grades[i] = grades[i]
        elif diffy < 3:
            grades[i] = x
        else:
            grades[i] = grades[i]
        
    return grades
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
