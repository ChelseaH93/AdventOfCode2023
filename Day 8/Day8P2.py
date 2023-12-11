import tqdm
def day8p2(path):
    input = [''.join(filter(str.isalnum, line)) for line in open(path)]
    dirs = list(input[0].rstrip())
    nodes = input[2:]
    end_nodes = [node[0:3] for node in nodes if node[2] == 'Z']
    start_nodes = [node for node in nodes if node[2] == 'A']
    result = len(dirs)
    for start_node in start_nodes:
        steps = []
        steps.append(start_node[0:3])
        while steps[-1] not in end_nodes:
            for dir in dirs:
                if dir == 'R':
                    next_el = start_node[6:9]
                    steps.append(next_el)
                    start_node = [node for node in nodes if node[0:3] == next_el][0]
                    if start_node[0:3] in end_nodes:
                        break
                elif dir == 'L':
                    next_el = start_node[3:6]
                    steps.append(next_el)
                    start_node = [node for node in nodes if node[0:3] == next_el][0]
                    if start_node[0:3] in end_nodes:
                        break
        result *= (len(steps) - 1)//len(dirs)
    print(result)

if __name__ == '__main__':
    day8p2('/Users/chelsea/Documents/AdventOfCode2023/Day 8/inputdata.txt')