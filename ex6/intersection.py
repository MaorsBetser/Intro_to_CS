

from random import uniform
from math import *


def derivative(f):
    '''
        find the Derivative of a given function
    '''
    h = 0.000001
    func = eval('lambda x: '+f)
    return (lambda x: (func(x+h) - func(x))/h)


def func_diff(f,g):
    '''
        Returns a concat of two given functions, f and -(g)
        so returns a function that is h(f - (g))
    '''
    return eval('lambda x:' +f+g)


def intersection(fg,dirv,x,n=100):
    '''
    Calculates the intersetion of two functions,
    by Newton raphson's algorithm
    taking X = x - f(x)
                   ----
                   f'(x)
    after a 100 cycles its pretty acurate
    returns the x axis intersection
    '''
    count = 1
    while count <= n:
        x = x - (fg(abs(x))/dirv(abs(x)))
        count += 1
    return x
    

def split_data(data):
    '''
    splits data read from file to the preffered format
    '''
    f = data[0][:-1]
    g = '-(' +data[1][:-1]+')'
    span = data[2].split()
    return f,g,float(span[0]),float(span[1])


def main():
    '''
        Reads input from file
        call split_data
        gets the derivative of f-g as another funciton - > func_derv
        evals the two functions f-g
        calls intersection with all the above data
        checks if the intersection on the x axis is inside the span given
        by the input, if not then prints no intersection
        otherwise calc f(x) and get the y axis value for the intersection
        then print
    '''
    with open('input5.txt','r') as infile:
        data = infile.readlines()
    infile.close()

    f,g,l_lim,h_lim= split_data(data)
    func_derv = derivative((f + g))
    func_fg = eval('lambda x: '+f+g)
    intersection_x = intersection(func_fg,func_derv,abs(h_lim))
    

    if intersection_x < l_lim or intersection_x > h_lim:
        print('No intersection')

    else:
        f_func = eval('lambda x: ' +f)
        intersection_y = f_func(intersection_x)
        print(f'Intersection point: ({intersection_x:.4f},{intersection_y:.4f})')


if __name__ == "__main__":
    main()