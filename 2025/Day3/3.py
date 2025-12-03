with open("2025/Day3/3.txt") as file:
    raw_input = file.readlines()

def highest_check_part_1(line):
    num_list = [int(i) for i in str(line).strip()]

    max_1 = num_list.index(max(num_list[:-1]))
    
    max_2 = num_list.index(max(num_list[max_1 + 1:]))

    return f"{num_list[max_1]}{num_list[max_2]}"

def highest_check_part_2(line, index_amt):
    num_list = [int(i) for i in str(line).strip()]
    digit_list = []
    index_start = 0
    for i in range(index_amt):
        max_i, max_num = highest_check(num_list, index_start, (index_amt-1) - i)
        index_start += max_i + 1
        digit_list.append(max_num)
    print(''.join(str(item) for item in digit_list))
    return int(''.join(str(item) for item in digit_list))

        
def highest_check(lst, start, end):
    temp_highest = 0
    highest_index = None
    list_check = lst[start:-end] if end != 0 else lst[start:]

    for i, value in enumerate(list_check):
        if value > temp_highest:
            temp_highest = value
            highest_index = i
    return highest_index, temp_highest


part_1_total = 0
part_2_total = 0

for line in raw_input:
    part_1_total += int(highest_check_part_1(line))
    part_2_total += highest_check_part_2(line, 12)

print(f"Part 1: {part_1_total}")
print(f"Part 2: {part_2_total}")