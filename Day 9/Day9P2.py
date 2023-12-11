import re
import sympy
from sympy.polys import specialpolys


def day9p2(path):
    sequences = [re.findall('[^:;\s,]+', line) for line in open(path)]
    total = 0
    for sequence in sequences:
        x = [i + 1 for i, val in enumerate(sequence)]
        y = [int(y) for y in sequence]
        poly = specialpolys.interpolating_poly(len(y), sympy.symbols("x"), x, y)
        result = poly.subs("x", 0)
        total += result
    print(total)


if __name__ == '__main__':
    day9p2('/Users/chelsea/Documents/AdventOfCode2023/Day 9/inputdata.txt')