import re
def day4(path):
    with open(path) as f:
        scratchcard = {re.findall('[^:;\s,]+', line)[1]: re.findall('[^:;\s,]+', line)[2:] for line in f.readlines()}
    card_nos = {int(k):v for (k,v) in zip(scratchcard.keys(), [0]*len(scratchcard.keys()))}
    for row in scratchcard.keys():
        divider = scratchcard[row].index('|')
        winning_nos = scratchcard[row][0:divider]
        my_nos = scratchcard[row][divider + 1:]
        card_no = int(row)
        for no in my_nos:
            if no in winning_nos:
                card_nos[card_no] += 1
    total_cards = {int(k):v for (k,v) in zip(scratchcard.keys(), [1]*len(scratchcard.keys()))}
    for card in card_nos.keys():
        if card_nos[card] > 0 and total_cards[card] == 1:
            for val in range(card + 1, card + card_nos[card] + 1):
                total_cards[val] += 1
        if card_nos[card] > 0 and total_cards[card] > 1:
            for val in range(card + 1, card + card_nos[card] + 1):
                total_cards[val] += total_cards[card] * 1
    print(sum([total_cards[card] for card in total_cards.keys()]))

if __name__ == '__main__':
    day4('/Users/chelsea/Documents/AdventOfCode2023/Day 4/InputData.txt')