def factors(num):
    result = []
    for i in range(1,num+1):
        if num % i == 0:
            result.append(i)
    
    return result

num = 20

print(factors(num))


#! better  solution

def betterFactors(num):
    result = []
    for i in range(1,num // 2):
        if num % i == 0:
            result.append(i)
    result.append(num)
    return result

num = 30

print(betterFactors(num))


#! optimal solution

from math import sqrt

def optimalFactors(num):
    result = []
    for i in range(1, int(sqrt(num))+1):
        if num % i == 0:
            result.append(i)
            
            if num//i !=i:
                result.append(num//i)
    result.sort()
    return result

num = 36

print(optimalFactors(num))
