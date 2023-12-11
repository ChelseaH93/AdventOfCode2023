def day8p1(path):
    input = [''.join(filter(str.isalpha, line)) for line in open(path)]
    dirs = list(input[0].rstrip())
    nodes = input[2:]
    end_node = [node[0:3] for node in nodes if node[0:3] == 'ZZZ'][0]
    steps = []
    start_node = [node for node in nodes if node[0:3] == 'AAA'][0]
    steps.append(start_node[0:3])
    while steps[-1] != end_node:
        for dir in dirs:
            if dir == 'R':
                next_el = start_node[6:9]
                steps.append(next_el)
                start_node = [node for node in nodes if node[0:3] == next_el][0]
                if start_node == end_node:
                    break
            elif dir == 'L':
                next_el = start_node[3:6]
                steps.append(next_el)
                start_node = [node for node in nodes if node[0:3] == next_el][0]
                if start_node == end_node:
                    break
    print(len(steps) - 1)

if __name__ == '__main__':
    day8p1('/Users/chelsea/Documents/AdventOfCode2023/Day 8/inputdata.txt')