
#! normal function 

def greet():
    print("hello asif")


greet()


#! infinite recursion 


def greet1():
    print("hello asif")
    # greet1()

greet1()



#! recursion 


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
