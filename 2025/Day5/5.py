import collections
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
    for line in lines:
        if '-' in line:
            ranges.append(line.strip())
    range_dict = {}
    for check_range in ranges:
        range_array = check_range.split('-')
        range_dict[int(range_array[0])] = 0
        range_dict[int(range_array[1])] = 1
        
    ordered_range = collections.OrderedDict(sorted(range_dict.items()))
    result = range_count(ordered_range)
    # print(result)
    return result

def range_count(range_dict):
    print(range_dict)
    
    previous_value = 0
    start_val = 0
    end_val = []
    for id in range_dict:
        
        # if range_dict[(range_dict.index(id) - 1)] == 0 and range_dict[id] == 0:
        #     continue
        if range_dict[id] == 0:
            print(start_val, previous_value)
            end_val.append((previous_value - (start_val+1)) if previous_value != 0 else 0)
            start_val = id
        else:
            previous_value = id
            previous_key = range_dict[id]
    
    result = 0
    for i in end_val:
        # print(i)
        result += i

    return result
        


    



print(f"Part 1: {part_1_id_check(lines)}")
print(f"Part 2: {part_2_id_check(lines)}")