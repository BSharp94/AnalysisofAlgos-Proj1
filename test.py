from GCD import *


var1, var2 = raw_input("Please enter two integers: ").split()
var1, var2 = int(var1),int(var2)

#run Euclidean algorithm
print(EuclidGCD(var1,var2))


