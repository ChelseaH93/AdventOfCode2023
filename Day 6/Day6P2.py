import math


def day6p1(path):
    with open(path) as f:
        times = [list(line.split()) for line in f]
    time = times[0][1:]
    distances = times[1][1:]
    total_time = int(''.join(time))
    total_distance = int(''.join(distances))
    wins = []
    possible_wins = range(1, total_time)
    for win in possible_wins:
        speed = win
        moved = (total_time - win)*speed
        if moved > total_distance:
            wins.append(speed)
    print(len(wins))


if __name__ == '__main__':
    day6p1('/Users/chelsea/Documents/AdventOfCode2023/Day 6/inputdata.txt')