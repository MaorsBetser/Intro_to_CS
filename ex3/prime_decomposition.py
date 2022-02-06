

def decompose(num):
    prime_divs = []
    div = 2
    while num != 1:
        if num % div == 0 :
            num /= div
            prime_divs.append(div)
        else :
            div += 1
    return prime_divs

def print_decomposition(num, prime_divs):
    duplicates = []
    print_list = [str(num),'=']
    count = 0
    
    for n in prime_divs:
        if not n in duplicates:
            times = prime_divs.count(n)
            if count > 0 and count < len(prime_divs):
                print_list.append('*')
            if times > 1:
                print_list.append(str(n) + '^' + str(prime_divs.count(n)))
            else:
                print_list.append(str(n))
            duplicates.append(n)
        count+=1
    print(''.join(print_list))

def prime_decomposition():
    while True:
        user_num = input('Please input a int greater than 1: ')
        if user_num.lower() == 'quit':
            break
        try:
                user_num = int(user_num)
                if user_num > 1:
                    print_decomposition(user_num,decompose(user_num))
        except:
            print('Illegal input. Try again')

def main():
    prime_decomposition()
main()