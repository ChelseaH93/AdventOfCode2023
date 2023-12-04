def day3(path):
    with open(path) as f:
        symbols = [list(line.rstrip()) for line in f]
    print(symbols)
    special_chars = []
    for i, lst in enumerate(symbols):
        for j, val in enumerate(lst):
            if not symbols[i][j].isdigit() and symbols[i][j] != '.':
                special_chars.append([i,j])
    numbers = []
    whole_num_coords = []
    for i, lst in enumerate(symbols):
        for j, val in enumerate(lst):
            if symbols[i][j].isdigit():
                whole_num_coords.append([i,j])
    for i, lst in enumerate(symbols):
        for j, val in enumerate(lst):
            if symbols[i][j].isdigit():
                neighbours = [[i-1, j-1], [i-1, j], [i-1, j+1], [i, j-1], [i, j+1], [i+1, j-1], [i+1, j], [i+1, j+1]]
                preds = [[i, j-2], [i, j-1]]
                succ = [[i, j+1], [i, j+2]]
                if len([n for n in neighbours if n in special_chars]) > 0 and not symbols[i][j-1].isdigit() and not symbols[i][j+1].isdigit():
                    numbers.append(int(symbols[i][j]))
                if len([n for n in neighbours if n in special_chars]) > 0 and symbols[i][j-1].isdigit() and not symbols[i][j+1].isdigit():
                    predecessor = [symbols[n[0]][n[1]] for n in preds if n in whole_num_coords]
                    values = [''.join(predecessor),symbols[i][j]]
                    value = ''.join(values)
                    if len(numbers) == 0:
                        numbers.append(int(value))
                    elif int(value) != numbers[-1]:
                        numbers.append(int(value))
                elif len([n for n in neighbours if n in special_chars]) > 0 and symbols[i][j+1].isdigit() and not symbols[i][j-1].isdigit():
                    successor = [symbols[n[0]][n[1]] for n in succ if n in whole_num_coords]
                    values = [symbols[i][j], ''.join(successor)]
                    value = ''.join(values)
                    if len(numbers) == 0:
                        numbers.append(int(value))
                    elif int(value) != numbers[-1]:
                        numbers.append(int(value))
                elif len([n for n in neighbours if n in special_chars]) > 0 and symbols[i][j+1].isdigit() and symbols[i][j-1].isdigit():
                    predecessor = [symbols[n[0]][n[1]] for n in preds if n in whole_num_coords]
                    successor = [symbols[n[0]][n[1]] for n in succ if n in whole_num_coords]
                    values = [''.join(predecessor), symbols[i][j], ''.join(successor)]
                    value = ''.join(values)
                    if len(numbers) == 0:
                        numbers.append(int(value))
                    elif int(value) != numbers[-1]:
                        numbers.append(int(value))

    print(numbers)
    print(sum(numbers))


if __name__ == '__main__':
    day3('/Users/chelsea/Documents/AdventOfCode2023/Day 3/InputData.txt')