
from math import sqrt

def quadratic(a,b,c):
    root_num = (b**2-4*a*c)
    if root_num < 0:
        return "No solution"

    elif root_num == 0:
        return "One solution: " + str((-b+sqrt((b**2)-4*a*c))/2*a)
    
    x1 = (-b+sqrt((b**2)-4*a*c))/2*a
    x2 = (-b-sqrt((b**2)-4*a*c))/2*a

    return "Two solutions: " + str(x1) + " , " + str(x2)

def main():
    a = int(input("Enter 1st parameter (a)"))
    b = int(input("Enter 2nd parameter (b)"))
    c = int(input("Enter 3rd parameter (c)"))
    
    if a == 0:
        print("Parameter (a) can't be 0, it is not a quadratic equation")
        a = int(input("Enter 1st parameter (a) again"))

    print(quadratic(a,b,c))
    
main()