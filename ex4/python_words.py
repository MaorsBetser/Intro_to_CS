

import keyword
import sys

def remove_from_string(s,start,end):
    #removes substring from a given string from given start(substring) -> given end(substring)
    #everything in the middle is discarded
    start_i = s.find(start)
    end_i = s.find(end,start_i+len(start))
    if start == '#':
        return s[0:start_i]

    elif end_i == -1:
        return s[0:start_i]
    
    sub_s = s[start_i:end_i+len(end)]
    s = s.replace(sub_s,'')

    return s


def split_all(s,str_lst):
    #splits a given string acording to a list of str and return a list of splitted strings
    s_split = []
    for string in str_lst:
        s_split.append(s.split(string))
    return s_split

def findall(s,sub):
    #finds all instances of a certrain substring in a given string
    #made this function to solve egde cases when a keyword is a part of another 
    # word i.e keyword 'or' is inside the word indicator so we can't count it /
    # has any nonalpha chars next ot it ie else: with colon after the e
    result = []
    k = 0
    while k < len(s):
        k = s.find(sub, k)
        if k == -1:
            return len(result)
        else: 
            if k != 0: # if keyword is not at the start of line
                if s[k - 1].isspace() == True and s[k + len(sub)].isalpha() == False: #checks if part of another word like
                    result.append(k)
                    k += (len(sub))
                    continue
            else:
                if s[k + len(sub)].isalpha() == False:
                    result.append(k)
                    k += (len(sub))
                    continue
                
        k += len(sub)

    return len(result)

def main():
    #init for used variables
    comment = False
    kw_dict = {}
    comment_indicator = 0
    c_data = []
    kwl = keyword.kwlist
    fn = input('please input filename (without suffix .py): ')
    # input file name, try and expect for input error
    try:
        pf = open(fn+'.py','r')
        data = pf.readlines()

    except IOError as ex:
        print('Please make sure a proper filename has been inputed' , ex)
        sys.exit()
    
    #iterate line in the given py file checking for '#', '"""', '"'
    for line in data:
        if '#' in line:
            tmp = remove_from_string(line,'#','#')
            c_data.append(tmp)
            continue


        #Multiline comment is tough to take care of, sometimes it will be oneliner and sometimes multiliner
        #my solution is to keep track of how many ive seen and if the number is even means that im not
        #in a multiline comment, otherwise consider as if im in a multiline comment 

        elif '"""' in line:
            comment_indicator += line.count('"""')
            if comment_indicator % 2 == 0:
                comment = False
            if comment_indicator % 2 == 1:
                 comment= True

            tmp = remove_from_string(line,'"""','"""')
            c_data.append(tmp)
            continue

        elif '"' in line:
            tmp = remove_from_string(line,'"','"')
            c_data.append(tmp)
        
        #Checking if im in a multiline comment if not appending to "c_data for clean_data"
        else:
            if comment:
                continue
            c_data.append(line)
    
    
    # reads the "clean data"
    for line in c_data:

        #iterating over keyword list
        for kw in kwl:
            #if key is in the specific line of code 
            if kw in line:
                if kw not in kw_dict:
                    count = findall(line, kw)
                    kw_dict[kw] = count
                    continue

                count = findall(line, kw)
                kw_dict[kw] += count
                
    #iterate over items in keyword dic priniting by the format requested
    for k,v in kw_dict.items():
        if v > 0:
            print('{:8}'.format(k)+':'+'{:2}'.format(v))
    pf.close()
main()