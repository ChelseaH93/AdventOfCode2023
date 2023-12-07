import tqdm
def day5p2(path):
    with open(path) as f:
        almanac = [list(line.split()) for line in f]
    dividers = [i for i in range(len(almanac)) if almanac[i] == []]
    seeds = almanac[0]
    mapped_seeds = [int(i) for i in seeds[1:]]
    seed_pairs = [mapped_seeds[i:i + 2] for i in range(0, len(mapped_seeds), 2)]
    seed_ranges = [[int(s[0]), int(s[0]) + int(s[1])] for s in seed_pairs]
    locations = []
    print(f"total ranges to loop through {len(seed_ranges)}")
    for rng in seed_ranges:
        for seed in tqdm.tqdm(range(rng[0], rng[1]), total =(rng[1]-rng[0])):
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
            locations.append(seed_updated)
    print(min(locations))


if __name__ == '__main__':
    day5p2('/Users/chelsea/Documents/AdventOfCode2023/Day 5/inputdata.text')