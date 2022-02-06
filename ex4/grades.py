

import sys
def read_students():
    #opens students file and parse to dict return dictionary -> {"id":"name"}
    #try to open file if fail then exit program
    #catches when id is not correct length, when name is not filled correctly
    id__name_dic = {}
    try:
        f = open('students2.txt','r')
        data = f.readlines()
        for line in data:

            line = line.split()
            id = line[0]

            if len(id) != 9:
                raise ValueError("id is not correct",id)

            line.pop(0)

            if len(line) < 1:
                raise ValueError("no name following id check id num:",id)
            
            name = ' '.join(line)
            id__name_dic[id] = name
            f.close()
        return id__name_dic

    except:
        print('Could not find "students.txt" file')
        sys.exit()

def read_grades():
    #opens grade file and parse to dict return dictionary -> {"id":"[grades]"}
    #try to open file if fail then exit program
    #catches when id is not correct length, and when grades not listed
    id_grade_dic = {}
    try:
        f = open('grades2.txt','r')
        data = f.readlines()

        for line in data:
            line = line.split()
            id = line[0]

            if len(id) != 9:
                raise ValueError("id is not correct",id)

            line.pop(0)

            if len(line) < 1:
                raise ValueError("no grade following id check id num:",id)

            line = [int(l) for l in line]
            id_grade_dic[id] = line
            f.close()
        return id_grade_dic

    except:
        print('Could not find "grades.txt" file')
        sys.exit()

def main():
    #parse files to dicts -> copmares two dicts for same id's 
    id_name = read_students()
    id_grade = read_grades()
    for k in id_name:
        if k not in id_grade:
            raise ValueError("id's dosen't match across dictonarys please check files")

    #calculates the highest average grade
    highest = [0,0]
    all_grades = []
    for key, value in id_grade.items():
        for i in range(len(value)):
            all_grades.append(value[i])
        
        grade_avg = sum(value)/len(value)
        if grade_avg > highest[1]:
            highest[0] = key
            highest[1] = grade_avg

    #gets the most occouring grade loops 1-100 count how many times a certain grade appeared
    #gets grades that did not appeared in all grades
    not_found_grade = []
    most_occoring = {}
    for grade in range(1,101):
        if grade not in all_grades:
            not_found_grade.append(grade)
            
        time_repeated = all_grades.count(grade)
        most_occoring[grade] = time_repeated
    #gets the most repeated grade and checks with other grade to
    # see if there are equal ones 
    # -> if there are appends to list
    max_times_repeated = max(most_occoring.values())
    most_achived_grades = [k for k,v in most_occoring.items() if v == max_times_repeated]
    most_achived_grades = str(most_achived_grades)

    #print by format requested
    print('Best student:',id_name[highest[0]]+',\n' "average: {:.2f}".format(highest[1]))
    print('the grade',most_achived_grades[1:-1],'appeared',max_times_repeated,'times')
    print('the grades that did not \nappear: '+'{}'.format(not_found_grade))       
main()