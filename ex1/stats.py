import math

def max_of_three(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    elif b > a:
        if b > c:
            return b
        else:
            return c

def sd_of_three(a,b,c):
    avg = (a+b+c)/3
    sd = math.sqrt(((a-avg)**2+(b-avg)**2+(c-avg)**2)/3)
    return sd

def main():
    num1 = int(input("Input 1st number: "))
    num2 = int(input("Input 2nd number: "))
    num3 = int(input("Input 3rd number: "))
    print("Maximum: " + str(max_of_three(num1,num2,num3)))
    print("Standard deviation " + str(sd_of_three(num1,num2,num3)))
main()