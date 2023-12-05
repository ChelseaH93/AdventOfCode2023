import re
bag = {'red': 12, 'green': 13, 'blue': 14}


def day2p1(path):
    with open(path) as f:
        games = {re.findall('[^:;\s,]+', line)[1]: re.findall('[^:;\s,]+', line)[2:] for line in f.readlines()}
    impossible = []
    print(games)
    for game in games.keys():
        blocks = games[game]
        for i, block in enumerate(blocks):
            if block in bag.keys():
                no = blocks[i-1]
                if int(no) > bag[block] and int(game) not in impossible:
                    impossible.append(int(game))
    print(sum([int(g) for g in games.keys() if int(g) not in impossible]))


if __name__ == '__main__':
    day2p1('./inputdata.txt')