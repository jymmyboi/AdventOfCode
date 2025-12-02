with open("2025/Day2/2.txt") as file:
    raw_input = file.read()
    input = raw_input.split(',')
    
part_1 = 0
part_2 = 0

def part_1_repeat_check(id_range):
    range_total = 0
    range_values = id_range.split('-')
    for number in range(int(range_values[0]), (int(range_values[1]) + 1)):
        num_string = str(number)
        firstpart, secondpart = num_string[:len(num_string)//2], num_string[len(num_string)//2:]
        if firstpart == secondpart:
            range_total += int(number)
    return range_total

def part_2_repeat_check(id_range):
    range_total = 0
    range_values = id_range.split('-')
    for number in range(int(range_values[0]), (int(range_values[1]) + 1)):
        repeats = (str(number) + str(number)).find(str(number), 1) != len(str(number))
        if repeats:
            range_total += int(number)
    return range_total
    

for number in input:
    part_1 += part_1_repeat_check(number)
    part_2 += part_2_repeat_check(number)

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")