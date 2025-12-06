import collections

import itertools
with open("2025\\Day5\\5.txt") as input:
    lines = input.readlines()

def part_1_id_check(lines):
    ranges = []
    ids = []
    for line in lines:
        if '-' in line:
            ranges.append(line.strip())
        elif len(line) > 1:
            ids.append(int(line.strip()))
    valid_id_count = 0
    for id in ids:
        is_fresh = False
        for check_range in ranges:
            range_array = check_range.split('-')
            start_number = int(range_array[0])
            end_number = int(range_array[1])
            if id >= start_number and id <= end_number:
                is_fresh = True
        if is_fresh:
            valid_id_count += 1
    
    return valid_id_count

def part_2_id_check(lines):
    ranges = []
    starts = []
    ends = []
    for line in lines:
        if '-' in line:
            ranges.append(line.strip())
    
    for id_range in ranges:
        range_array = id_range.split('-')
        starts.append(int(range_array[0]))
        ends.append(int(range_array[1]))

    clean_ends = list(set(ends))
    sorted_ends = sorted(clean_ends)

    clean_starts = list(set(starts))
    sorted_starts = sorted(clean_starts)

    # print(f"sorted_starts {sorted_starts}")
    # print(f"sorted_ends {sorted_ends}")

    lower_bound = 0
    upper_bound = 0
    id_count = 0
    for start,end in zip(sorted_starts, sorted_ends):
        if start > upper_bound:
            id_count += (upper_bound - (lower_bound - 1)) if upper_bound != 0 else 0
            lower_bound = start
            upper_bound = end
        elif start < upper_bound:
            upper_bound = end
        # print(id_count)
        print(f"{start}, {end}, {lower_bound}, {upper_bound}")
    
    id_count += (upper_bound - (lower_bound - 1))
    # print(id_count)






print(f"Part 1: {part_1_id_check(lines)}")
print(f"Part 2: {part_2_id_check(lines)}")