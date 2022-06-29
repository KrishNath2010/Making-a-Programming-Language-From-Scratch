def multiply(x, y):
    z = 0
    for i in range(x):
        z+=y
    return z

def subtration(x, y):
    for i in range(y):
        z = 0
        for i in range(1,x):
            z = z + 1
        x=z
    return x

def division(x, y):
    count = 0
    for i in range(y, x+1, y):
        count +=1
    return count
    
#print(division(19,20))
