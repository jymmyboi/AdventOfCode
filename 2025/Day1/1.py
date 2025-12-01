import math

with open("2025\\Day1\\1.txt") as input:
    raw_lines = input.readlines()
    lines = [line.strip() for line in raw_lines]

def rotation_check(direction_number):
    direction = direction_number[0]
    amount = direction_number[1:]
    return [direction, amount]

def zero_check(remainder):
    if remainder == 0:
        return 1
    else:
        return 0

def calc_new_pos_part_1(start, lines):  
    zero_amt = 0
    for line in lines:
        input = rotation_check(line)
        if input[0] == "R":
            start += int(input[1])
            start = start % 100
            zero_amt += zero_check(start)
        else:
            start -= int(input[1])
            start = start % 100
            zero_amt += zero_check(start)
    return zero_amt

def calc_new_pos_part_2(start, lines):  
    print(lines)
    zero_amt = 0
    for line in lines:
        print(f"current value is {start}")
        input = rotation_check(line)
        if input[0] == "R":
            print(f"adding {input[1]}")
            difference = int(input[1])
            zero_amt += positive_zero_check(start, difference)
            print(f"zero amt is {zero_amt}")
            start += difference
            start = start % 100
        else:
            print(f"subtracting {input[1]}")
            difference = int(input[1])
            zero_amt += negative_zero_check(start, difference)
            print(f"zero amt is {zero_amt}")
            start -= difference
            start = start % 100
        print(zero_amt)
    return zero_amt

def positive_zero_check(start, difference):
    result = start + difference
    zero_click_amount = 0
    zero_click_amount = math.trunc(result / 100)
    print(f"{result} and {zero_click_amount}")
    return zero_click_amount

def negative_zero_check(start, difference):
    result = start - difference
    zero_click_amount = 0
    if result <= 0:
        zero_click_amount = math.trunc((abs(result) + 100) / 100)
        if start == 0:
            zero_click_amount -= 1
    print(f"{result} and {zero_click_amount}")
    return zero_click_amount

part_1 = calc_new_pos_part_1(50, lines)
print(part_1)

part_2 = calc_new_pos_part_2(50, lines)
print(part_2)