import numpy as np
import math


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


def Find_Divisors(var):
    divisors = []

    for i in range(2, var+1):
        if var % i == 0:
            divisors.append(i)

    return divisors

def compare_divisors(var1,var2):
    divisors1 = Find_Divisors(var1)
    divisors2 = Find_Divisors(var2)

    best_results = 1
    for one in divisors1:
        if one in divisors2:
            best_results = one

    return best_results


var1, var2 = raw_input("Please enter two integers: ").strip().split()
var1, var2 = int(var1),int(var2)

#run Euclidean algorithm
print "==== Euclid Method ===="
print "Results: ",(EuclidGCD(var1,var2))

#run comparing divisors
print "=== Compare Divisors ==="
print "Results: ",(compare_divisors(var1,var2))

