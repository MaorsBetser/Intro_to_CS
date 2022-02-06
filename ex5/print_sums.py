

out = []
to_print = {}
i = 0

def print_sums(n,parts):
    '''
     Takes n -> Sum and parts -> list of numbers
     check for the possible combinations to reach the Sum with the given list of numbers by recursivly calling itself
     every time the function is called we deduct from the sum the number currently calcualting
     and only if the sum eventually reaches exactly zero we print the calculations we've made
     otherwise the route in which we calcualted is false and should be terminated
    '''
    global out
    global num
    global to_print
    global i


    if n == 0:
        to_print[i] = [num,'=',' + '.join(out)]
        i += 1
        return n

    if n < 0:
        return n

    for part in parts:
        out.append(str(part))
        print(out)
        result = print_sums((n-part),parts)

        if result == 0:
            if len(out) >= 1:
                out.pop(-1)
        elif result < 0:
            out.pop(-1)

        
    return result


def main():
    '''
    Handles logic of calling all functions neccesary inorder to run print_sums correctly
    iterates over each line in infile and for each line checks if line is valid,
    split in to correct parts
    calls print_sums
    calls write_outfile
    '''
    global num
    global i
    with open('input_ex2.txt','r') as infile:
        data = infile.readlines()
        infile.close()
        
    for line in data:
        if not line_validation(line):
            to_print[i] = str(line) + ' Error'
            i += 1
            continue
        num , parts = split_for_func(line)
        
        sum_of = parts_text(parts)

        to_print[i] = str(num) +' as the sum of' + sum_of
        i += 1
        print_sums(num,parts)
    write_outfile(num,parts)
  

def write_outfile(num,parts):
    '''
    Writes to a file by going over the dictionary where we store all the data
    and writes each line
    '''
    with open('output_ex2.txt','w') as outfile:
        for i in range(len(to_print)):
            print(type(to_print[i]))
            if type(to_print[i]) == str:
                if i == 0:
                    outfile.write(to_print[i])
                    continue
                outfile.write('\n\n')
                outfile.write(to_print[i])
            else:
                for j in to_print[i]:
                    outfile.write(' ' + str(j))
            outfile.write('\n')
    outfile.close()


def line_validation(line):
    '''
    Validate the input given and returns true if the line is valid
    '''
    line = line.split()
    if len(line) < 3:
        return False
    for num in line:
        if not num.isnumeric() or int(num) == 0:
            return False
    return True


def split_for_func(line):
    '''
    split the line in to the required fields for print_sums() func
    '''
    line = line.split()
    n = line[0]
    n = int(n)
    line.pop(0)
    for i in range(len(line)):
        line[i] = int(line[i])
    return n , line

def parts_text(parts):
    '''
    joins a list in to a string with the format required
    which is number, number, number and number
    '''
    parts_text = ''
    for p in parts:
            if p == parts[-1]:
                parts_text += 'and '+ str(p)
            else:
                parts_text += ' ' + str(p) + ' ,'
    return parts_text
if __name__ == '__main__':
    main()