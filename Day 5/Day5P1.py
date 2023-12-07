def day5p1(path):
    with open(path) as f:
        almanac = [list(line.split()) for line in f]
    dividers = [i for i in range(len(almanac)) if almanac[i] == []]
    seeds = almanac[0]
    mapped_seeds = seeds[1:]
    locations = []
    for seed in mapped_seeds:
        seed_updated = int(seed)
        for div, vals in enumerate(dividers):
            if vals != dividers[-1]:
                current_mapping = almanac[dividers[div] + 2:dividers[div + 1]]
                seed_range = [((int(seed_updated) - int(i[1])) + int(i[0])) for i in current_mapping if int(seed_updated) >= int(i[1]) and int(seed_updated) < int(i[1]) + int(i[2])]
                if len(seed_range) > 0:
                    seed_updated = seed_range[0]
            elif vals == dividers[-1]:
                current_mapping = almanac[dividers[div] + 2:]
                seed_range = [((int(seed_updated) - int(i[1])) + int(i[0])) for i in current_mapping if int(seed_updated) >= int(i[1]) and int(seed_updated) < int(i[1]) + int(i[2])]
                if len(seed_range) > 0:
                    seed_updated = seed_range[0]
            print(seed_updated)
        locations.append(seed_updated)
    print(min(locations))

if __name__ == '__main__':
    day5p1('/Users/chelsea/Documents/AdventOfCode2023/Day 5/inputdata.text')