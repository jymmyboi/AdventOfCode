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
    max_index = num_list.index(max(num_list[:(index_amt - 1)]))
    digit_list.append(num_list[max_index])
    print(digit_list)
    for i in range(index_amt):
        print(digit_list)
        max_index = num_list.index(max(num_list[max_index+1:((index_amt-1) - i) if (index_amt-1) > 0 else 1]))
        digit_list.append(num_list[max_index])
        

total = 0

for line in raw_input:
    total += int(highest_check_part_1(line))
    highest_check_part_2(line, 12)

print(f"Part 1: {total}")
