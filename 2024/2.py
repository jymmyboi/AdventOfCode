with open("2.txt") as input:
    input_text = input.readlines()
valid_counter = 0

def sanitise_input(line):
    return list(map(int, line.split()))
        
def ascend_check(numbers):
    return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))

def descend_check(numbers):
    return all(numbers[i] >= numbers[i + 1] for i in range(len(numbers) - 1))

def difference_check(numbers):
    return all(1 <= abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(len(numbers) - 1))
            
for line in input_text:
    num_array = sanitise_input(line)
    if (ascend_check(num_array) or descend_check(num_array)) and difference_check(num_array):
            valid_counter += 1

print(valid_counter)
        



    