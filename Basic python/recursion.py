
#! normal function 

def greet():
    print("hello asif")


greet()


#! infinite recursion 


def greet1():
    print("hello asif")
    # greet1()

greet1()



#! head recursion 


def func(count):
    
   
    if count == 4:
        return
    print("hey asif hi!")
    
    count +=1
    func(count)
    
func(count = 0)

#! tail recursion 
def func1(count):
    
   
    if count == 4:
        return
    
    count +=1
    func1(count)
    print(" hi!")
    
func1(count = 0)


#! functional recursion  
#? sum of n natural number

def  sumOfN(sum,i,n):
    if i > n:
        print(sum)
        return
    sumOfN(sum+i,i+1,n)

sumOfN(0,1,10)