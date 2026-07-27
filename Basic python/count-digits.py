n = 7645763

num = n 
count = 0
while num>0:
    last_digit = num % 10
    count +=1
    num = num // 10


print("total count ", count)


# use logarithm 
from math import *

def countDigits(num1):
    result = log10(num1)+1
    
    return result // 1


num1 =766776434
print(countDigits(num1))