from word2number import w2n
def split_number_words(input_string):
    number_words = [
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    input_string_lower = input_string.lower()
    number_matches = []
    for start in range(len(input_string)):
        for end in range(start + 1, len(input_string) + 1):
            current_word = input_string_lower[start:end]
            if current_word in number_words:
                number_matches.append(str(w2n.word_to_num(current_word)))
            elif current_word.isnumeric():
                number_matches.append(current_word)
    return number_matches
def day1(path):
    with open(path) as f:
        lines = [split_number_words(line) for line in f.readlines()]
        vals = [[(num[0]),(num[-1])] for num in lines]
        numbers = [int(''.join(num)) for num in vals]
    print(sum(numbers))

if __name__ == '__main__':
    day1('/Users/chelsea/Documents/AdventOfCode2023/Day 1/inputdata.txt')