with open("2025/Day2/2.txt") as file:
    raw_input = file.read()
    input = raw_input.split(',')
    
total = 0

def repeat_check(id_range):
    range_total = 0
    range_values = id_range.split('-')
    print(range_values)
    for number in range(int(range_values[0]), (int(range_values[1]) + 1)):
        num_string = str(number)
        firstpart, secondpart = num_string[:len(num_string)//2], num_string[len(num_string)//2:]
        if firstpart == secondpart:
            range_total += int(number)
            print(number)
    print(f"Range total {range_total}")
    return range_total
    

for number in input:
    total += repeat_check(number)

print(total)