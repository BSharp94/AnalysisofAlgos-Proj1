import numpy as np
import math
import datetime as dt

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

'''
var1, var2 = raw_input("Please enter two integers: ").strip().split()
var1, var2 = int(var1),int(var2)

#run Euclidean algorithm
print "==== Euclid Method ===="
n1 = dt.datetime.now()
results = (EuclidGCD(var1,var2))
n2 = dt.datetime.now()
print "Results: ", results
print "Time: ", (n2-n1).microseconds

#run comparing divisors
print "=== Compare Divisors ==="
n1 = dt.datetime.now()
results = (compare_divisors(var1,var2))
n2 = dt.datetime.now()
print "Results: ",results
print "Time: ", (n2-n1).microseconds
'''
def get_average_time_euclid(min_val,max_val,sample_size):
    #record time taken against different sizes of inputs
    data_0_to_100_val1 = [ np.random.randint(min_val,max_val) for i in range(sample_size)]
    data_0_to_100_val2 = [ np.random.randint(min_val,max_val) for i in range(sample_size)]

    global_sum = 0
    for index in range(0,sample_size):
        n1 = dt.datetime.now()
        results = (EuclidGCD(data_0_to_100_val1[index],data_0_to_100_val2[index]))
        n2 = dt.datetime.now()
        global_sum += (n2-n1).microseconds
    return (global_sum/sample_size)


def get_average_time_compare_divisors(min_val,max_val,sample_size):
    #record time taken against different sizes of inputs
    data_0_to_100_val2 = [ np.random.randint(min_val,max_val) for i in range(sample_size)]
    data_0_to_100_val1 = [ np.random.randint(min_val,max_val) for i in range(sample_size)]

    global_sum = 0
    for index in range(0,sample_size):
        n1 = dt.datetime.now()
        results = (compare_divisors(data_0_to_100_val1[index],data_0_to_100_val2[index]))
        n2 = dt.datetime.now()
        global_sum += (n2-n1).microseconds
    return (global_sum/sample_size)


if __name__ == "__main__":
    sample_size = 100

    values = [10e1,10e2,10e3,10e4,10e5,10e6,10e7]

    print "==== Average Time for Euclids Algorithm ====="

    for index in range(len(values)-1):
        val1,val2 = values[index],values[index+1] #get range values
        avg_time = get_average_time_euclid(val1,val2,sample_size)
        print "Range {} to {}: avg_time {}".format(val1,val2,avg_time)

    print "==== Average Time for Compare Divisors Algorithm ====="

    for index in range(len(values)-1):
        val1,val2 = values[index],values[index+1] #get range values
        avg_time = get_average_time_compare_divisors(val1,val2,sample_size)
        print "Range {} to {}: avg_time {}".format(val1,val2,avg_time)
