def day1p1(path):
    with open(path) as f:
        lines = [''.join(filter(str.isdigit, line)) for line in f.readlines()]
        vals = [[(num[0]),(num[-1])] for num in lines]
        numbers = [int(''.join(num)) for num in vals]
    print(sum(numbers))

if __name__ == '__main__':
    day1p1('./inputdata.txt')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
