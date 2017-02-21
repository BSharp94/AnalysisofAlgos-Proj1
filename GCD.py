import numpy as np


var1, var2 = input("Please enter two integers: ").split()
var1, var2 = int(var1),int(var2)


def EuclidGCD(var1,var2):

    # return other value if one is zero
    if var1 == 0:
        return var2
    if var2 == 0:
        return var1
   
   #switch values so var1 is graeter
    if var2 > var1:
        temp = var1
        var1 = var2
        var2 = temp

    #put in form A = (B * Q) + r
    Q = var1 / var2
    r = var1 % var2

    return EuclidGCD(var2,r)


#run Euclidean algorithm
print(EuclidGCD(var1,var2))




