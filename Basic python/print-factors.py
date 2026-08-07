def factors(num):
    result = []
    for i in range(1,num+1):
        if num % i == 0:
            result.append(i)
    
    return result

num = 20

print(factors(num))