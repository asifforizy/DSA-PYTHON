# brute force

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]


for i in  m:
    count = 0
    for x in n:
        if x == i:
            count+= 1
    print(count)
    


# optimal
    
hashList =[0]*11

for num in n:
    hashList[num] +=1
    
for num in m:
    if num<1 or num> 10:
        print(0)
    else:
        print(hashList[num])