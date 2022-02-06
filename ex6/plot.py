

import matplotlib.pyplot as plt
from math import *


def get_xy_vals(funcs,a,b,h=0.01):
    '''
        given list of functions and range of x values
        calc x values in the given range, with intervals of 0.01
        and then places said x vals in the current given function
        to calc the y values for given function
        stores all y values in dictonary, then returns
        x values from a - b and y values for each function in given range
        
    '''
    y_dict = {}
    x_vals = [a+i*h for i in range(int((b-a)/h))]
    for f in funcs:
        f = eval('lambda x:'+f)
        y_dict[f] = [f(x) for x in x_vals]
    return x_vals,y_dict


def plot(x_vals,y_dict):
    '''
        gets x values and a dict holding y values for each function
        calc the min y and max value for setting the scale of the graph
        iterates over each y values of each function and plots in on graph

    '''
    min_y = 0
    max_y = 0

    for value in y_dict.values():
        if min_y == 0 and max_y == 0:
            min_y = min(value)
            max_y = max(value)
        if min(value) < min_y:
            min_y = min(value)
        if max(value) > max_y:
            max_y = max(value)

        plt.plot(x_vals,value,color='red')

    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis([min(x_vals),max(x_vals),min_y,max_y])
    plt.grid(True)
    plt.show()


def main():
    '''
        open functions file read data and gets the span which is located
        at the last line
        iterate over lines and appends each functions to a list removing the last char
        to get rid of new line char.
        then splits the span into a,b where a is low value and b is high
        calls get_xy_vals and then plot to plot the graph
    '''
    with open('functions.txt','r') as infile:
        data = infile.readlines()
        span = data[-1]
    infile.close()
    funcs = []
    for func in data:
        if func != span:
            funcs.append(func[:-1])
    span = span.split()
    a,b = float(span[0]),float(span[1])

    x_vals,y_dict = get_xy_vals(funcs,a,b)
    plot(x_vals, y_dict)
    

if __name__ == "__main__":
    main()