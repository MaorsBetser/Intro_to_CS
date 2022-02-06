from random import randint


def is_probably_prime(n):
    '''
        takes in a number and checks the probabilty of being prime by calling is_suspected_prime
    '''
    for i in range(20):
        if not is_suspected_prime(n):
            return False
    return True


def is_suspected_prime(n):
    '''
        checks if a number is prime by calc the modular_power to a random number between 2 - (n-1)
        by calling modular power and returns true if the number returns either 1 or n-1
    '''
    rand = randint(2, (n-1))
    d = modular_power(rand,((n-1)//2),n)
    if d == 1 or d == (n-1):
        return True
    return False


def modular_power(a,b,n):
    '''
        computes the remainder of a**b mod n
    '''
    l=[]
    while b > 0:
        if b % 2 == 1:
            l = [1]+l
        else:
            l = [0]+l
        b //= 2
    result = 1
    for k in l:
        result = (result ** 2) % n
        if k == 1:
            result = (result * a) % n
    return result


def main():
    '''
        Open input file iterate through check for primes by calling
        is_probably_prime for each number in thefile
        writes to outfile "number is / is not prime"
    '''
    results = []
    try:
        with open('input_ex1.txt', 'r') as infile:
            data = infile.readlines()
            for num in data:
                    num = int(num)
                    if num % 2 == 0:
                        results.append(str(num) + ' is not prime')
                        
                    elif is_probably_prime(num):
                        results.append(str(num) + ' is prime')

                    else:
                        results.append(str(num) + ' is not prime')

                        

        infile.close()
        
        with open('output_ex1.txt','w') as outfile:
            for num in results:
                outfile.write(num + '\n')
        outfile.close()

    except:
        print("Error couldn't open given file.")


if __name__ == "__main__":
    main()