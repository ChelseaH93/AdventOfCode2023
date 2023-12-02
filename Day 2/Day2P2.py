import re
import math
def day2(path):
    with open(path) as f:
        games = {re.findall('[^:;\s,]+', line)[1]: re.findall('[^:;\s,]+', line)[2:] for line in f.readlines()}
    powers = []
    for game in games.keys():
        bag = {'red': 0, 'green': 0, 'blue': 0}
        blocks = games[game]
        for i, block in enumerate(blocks):
            if block in bag.keys():
                no = int(blocks[i-1])
                if bag[block] < no:
                    bag[block] = no
        powers.append(math.prod([bag[b] for b in bag.keys()]))
    print(sum(powers))

if __name__ == '__main__':
    day2('/Users/chelsea/Documents/AdventOfCode2023/Day 2/inputdata.txt')