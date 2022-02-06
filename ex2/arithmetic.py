

def is_arithmetic(lst): 
    '''Helper function to test for arithmatic sequence'''
    d = lst[1] - lst[0]
    for i in range(len(lst) - 1):
        if lst[i + 1] - lst[i] != d:
            return False
    return True

def find_arithmetic(lst):
    '''iterates over every subsequence and finds the longest arithmetic sequence'''
    i = 0
    size = 2
    longest_size = 0
    while i < (len(lst) - 1):
        print(size,longest_size)
        if size == (len(lst) + 1):
            break
        
        if is_arithmetic(lst[i:size:]):
            longest_index = i
            longest_size = size
            size += 1

        else:
            i += 1
            size += 1

    return longest_index, longest_size

def main():
    lst = input("Please input numbers seperated by a (,) ")
    lst = lst.split(',')
    for i in range(len(lst)):
        lst[i] = int(lst[i])  

    arithmetic_index,size = find_arithmetic(lst)
    print("longest arithmetic sequence:", lst[arithmetic_index:size])

    
main()