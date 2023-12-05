import math
from itertools import combinations


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def day3p2(path):
    with open(path) as f:
        symbols = [list(line.rstrip()) for line in f]
    whole_num_coords = []
    for i, lst in enumerate(symbols):
        for j, val in enumerate(lst):
            if symbols[i][j].isdigit():
                whole_num_coords.append([i,j])
    special_chars = []
    gear_nums = []
    for i, lst in enumerate(symbols):
        for j, val in enumerate(lst):
            if symbols[i][j] == '*':
                special_chars.append([i,j])
                neighbours = [[i - 1, j - 1], [i - 1, j], [i - 1, j + 1], [i, j - 1], [i, j + 1], [i + 1, j - 1],
                              [i + 1, j], [i + 1, j + 1]]
                num_neighbours = [n for n in neighbours if n in whole_num_coords]
                if len(num_neighbours) <= 1:
                    continue
                else:
                    distances = [distance(*combo) for combo in combinations(num_neighbours,2) if distance(*combo) >= 2]
                    if len(distances) >= 1:
                        gear_nums.append(num_neighbours)
    gear_ratios = []
    for coord_lst in gear_nums:
        gear_ratio = []
        for coord in coord_lst:
            i = coord[0]
            j = coord[1]
            preds = [[i, j-2], [i, j-1]]
            succ = [[i, j+1], [i, j+2]]
            if not symbols[i][j-1].isdigit() and not symbols[i][j+1].isdigit():
                gear_ratio.append(int(symbols[i][j]))
            if symbols[i][j-1].isdigit() and not symbols[i][j+1].isdigit():
                predecessor = [symbols[n[0]][n[1]] for n in preds if n in whole_num_coords]
                values = [''.join(predecessor), symbols[i][j]]
                value = ''.join(values)
                if len(gear_ratio) == 0:
                    gear_ratio.append(int(value))
                elif int(value) != gear_ratio[-1]:
                    gear_ratio.append(int(value))
            elif symbols[i][j+1].isdigit() and not symbols[i][j-1].isdigit():
                successor = [symbols[n[0]][n[1]] for n in succ if n in whole_num_coords]
                values = [symbols[i][j], ''.join(successor)]
                value = ''.join(values)
                if len(gear_ratio) == 0:
                    gear_ratio.append(int(value))
                elif int(value) != gear_ratio[-1]:
                    gear_ratio.append(int(value))
            elif symbols[i][j+1].isdigit() and symbols[i][j-1].isdigit():
                predecessor = [symbols[n[0]][n[1]] for n in preds if n in whole_num_coords]
                successor = [symbols[n[0]][n[1]] for n in succ if n in whole_num_coords]
                values = [''.join(predecessor), symbols[i][j], ''.join(successor)]
                value = ''.join(values)
                if len(gear_ratio) == 0:
                    gear_ratio.append(int(value))
                elif int(value) != gear_ratio[-1]:
                    gear_ratio.append(int(value))
        if len(gear_ratio) > 1:
            gear_ratios.append(math.prod(gear_ratio))
    print(sum(gear_ratios))


if __name__ == '__main__':
    day3p2('./InputData.txt')