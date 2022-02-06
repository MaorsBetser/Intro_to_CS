
def print_triangle(height,dlr,spc_times):
    i = 1
    dlr_cnt = 0

    while i <= height:
        j = height
        #print spaces
        while j > i-5:
            print(' ', end=' '*spc_times)
            j -= 1

        #starter *
        print('*', end=(' ')*spc_times)

        #print inside of triangle
        t = 1
        while t < 2 * (i - 1):

            if dlr_cnt == dlr:
                dlr_cnt = 0
                print(' ' * spc_times ,end=' ')
            else:
                print('$',end=(' ')*spc_times)
                dlr_cnt += 1
            t += 1

        if i == 1:
            print()

        else:
            #closing *
            print('*')

        i += 1

    #correct spacing
    j = height
    while j > i-5:
        print(' ', end=' '*spc_times)
        j -= 1
    k = 1

    #print '*' last line
    while k < 2 * (i):
        print('*', end=' '* spc_times)
        k += 1
    print()

def main():
    height = int(input('Enter height: '))
    while height < 2:
        height = int(input('Enter height value larger than 2: '))
    dlrs= int(input('Enter number of $: '))
    spaces = int(input('Enter number of spaces: '))
    print_triangle(height,dlrs,spaces)
main()