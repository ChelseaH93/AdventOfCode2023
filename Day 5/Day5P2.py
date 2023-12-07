import pandas as pd
def day5p2(path):
    with open(path) as f:
        almanac = [list(line.split()) for line in f]
    dividers = [i for i in range(len(almanac)) if almanac[i] == []]
    seeds = almanac[0]
    mapped_seeds = [int(i) for i in seeds[1:]]
    seed_pairs = [mapped_seeds[i:i + 2] for i in range(0, len(mapped_seeds), 2)]
    seed_ranges = [[s[0], s[0] + s[1]] for s in seed_pairs]
    new_ranges = []
    for rng in seed_ranges:
        current_range = rng
        current_ranges = []
        for div, vals in enumerate(dividers):
            if vals != dividers[-1]:
                current_mapping = almanac[dividers[div] + 2:dividers[div + 1]]
                mapped_range = [[int(i[1]),int(i[1]) + int(i[2])] for i in current_mapping if pd.Interval(current_range[0], current_range[1]).overlaps(pd.Interval(int(i[1]),int(i[1]) + int(i[2])))]
                for map in mapped_range:
                    print(map)
                    # if current_range[0] < map[0] and current_range[1] < map[1]:
                    #     new_ranges = [current_range[0],map[0]]

    print(new_ranges)


if __name__ == '__main__':
    day5p2('/Users/chelsea/Documents/AdventOfCode2023/Day 5/inputdata.text')