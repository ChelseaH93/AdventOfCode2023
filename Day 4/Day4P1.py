import re
def day4(path):
    with open(path) as f:
        scratchcard = {re.findall('[^:;\s,]+', line)[1]: re.findall('[^:;\s,]+', line)[2:] for line in f.readlines()}
    scratchcard_worth = []
    for row in scratchcard.keys():
        divider = scratchcard[row].index('|')
        winning_nos = scratchcard[row][0:divider]
        my_nos = scratchcard[row][divider + 1:]
        points = 0
        for no in my_nos:
            if no in winning_nos and points <= 1:
                points += 1
            elif no in winning_nos and points > 1:
                points = points*2
        scratchcard_worth.append(points)
    print(sum(scratchcard_worth))



if __name__ == '__main__':
    day4('/Users/chelsea/Documents/AdventOfCode2023/Day 4/InputData.txt')