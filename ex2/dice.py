
from random import randrange
def throw_dice(n):
    pos_throws = [0]*11
    throw = 0
    while throw < n:
        d1 = randrange(1,7)
        d2 = randrange(1,7)
        for i in range(len(pos_throws)):
            if (d1+d2) == i+2:
                pos_throws[i] += 1
        throw += 1
    return pos_throws

def main():
    n = int(input('Enter number of throws: '))

    throw_chart = throw_dice(n)
    throw_max = max(throw_chart)

    for i in range(throw_max):

        tmp_chart = [' ']*11

        for j in range(len(throw_chart)):
            if throw_chart[j] >= throw_max:
                tmp_chart[j] = 'x'

        throw_max -= 1

        # formats the list to small strings with equal spacing
        spaced_chart = "{:>3}"*len(tmp_chart) 
        print(spaced_chart.format(*tmp_chart))

    scores = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    spaced_scores = "{:>3}" *len(scores)
    print(spaced_scores.format(*scores))
    
main()