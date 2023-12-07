import math


def day6p1(path):
    with open(path) as f:
        times = [list(line.split()) for line in f]
    time = times[0][1:]
    distances = times[1][1:]
    no_of_wins = []
    for i, t in enumerate(time):
        wins = []
        max_t = int(t)
        possible_wins = range(1, int(t) + 1)
        for win in possible_wins:
            speed = win
            moved = (max_t - win)*speed
            if moved > int(distances[i]):
                wins.append(moved)
        no_of_wins.append(len(wins))
    print(math.prod(no_of_wins))


if __name__ == '__main__':
    day6p1('/Users/chelsea/Documents/AdventOfCode2023/Day 6/inputdata.txt')