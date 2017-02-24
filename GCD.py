import numpy as np
import math
import datetime as dt
import sys
from bokeh.plotting import figure,show,output_file,save
from bokeh.layouts import row,Spacer

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


#used to print bokeh report
def print_bar_chart_bokeh(data_x,data_y,title_):

    assert len(data_x) == len(data_y), "Critical Error, data_x and data_y different size when printing to bokeh graph"

    p = figure( title=title_, x_axis_label='Data size', y_axis_label='Average times( milisecond)')
    p.line(data_x,data_y)
    return p

#used to print bokeh report
def print_to_bokeh(graph1_x,graph1_y,graph2_x,graph2_y):
    output_file('Average-times.html', title="GCD - Problem 12")

    horizontal_spacer = Spacer(width=100)
    euclids_graph = print_bar_chart_bokeh(graph1_x,graph1_y,"Euclids Method")
    compare_divisors_graph = print_bar_chart_bokeh(graph2_x,graph2_y,"Compare Divisors Method")

    data = row(euclids_graph,horizontal_spacer,compare_divisors_graph)
    save(data)



if __name__ == "__main__":
    #if benchmark flag, run benchmark
    if "--benchmark" in sys.argv:

        sample_size = 100

        values = [10e1,10e2,10e3,10e4,10e5,10e6]

        print "==== Average Time for Euclids Algorithm ====="
        record_data_x_euclid = []
        record_data_y_euclid = []
        for index in range(len(values)-1):
            val1,val2 = values[index],values[index+1] #get range values
            record_data_x_euclid.append(val1)
            avg_time = get_average_time_euclid(val1,val2,sample_size)
            record_data_y_euclid.append(avg_time)
            print "Range {} to {}: avg_time {} milisecond".format(val1,val2,avg_time)

        print "==== Average Time for Compare Divisors Algorithm ====="
        record_data_x_compare_divisors = []
        record_data_y_compare_divisors = []
        for index in range(len(values)-1):
            val1,val2 = values[index],values[index+1] #get range values
            record_data_x_compare_divisors.append(val1)
            avg_time = get_average_time_compare_divisors(val1,val2,sample_size)
            record_data_y_compare_divisors.append(avg_time)
            print "Range {} to {}: avg_time {} milisecond".format(val1,val2,avg_time)

        if "--print-to-bokeh" in sys.argv:
            print_to_bokeh(record_data_x_euclid,record_data_y_euclid,record_data_x_compare_divisors,record_data_y_compare_divisors)

    # run user inputs
    else:
        var1, var2 = raw_input("Please enter two integers: ").strip().split()
        var1, var2 = int(var1),int(var2)

        #run Euclidean algorithm
        print "==== Euclid Method ===="
        n1 = dt.datetime.now()
        results = (EuclidGCD(var1,var2))
        n2 = dt.datetime.now()
        print "Results: ", results, " milisecond"
        print "Time: ", (n2-n1).microseconds, " milisecond"


        #run comparing divisors
        print "=== Compare Divisors ==="
        n1 = dt.datetime.now()
        results = (compare_divisors(var1,var2))
        n2 = dt.datetime.now()
        print "Results: ",results, " milisecond"
        print "Time: ", (n2-n1).microseconds, " milisecond"
