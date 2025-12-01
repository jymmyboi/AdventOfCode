
with open("2024\\Day5\\5.txt") as input:
    lines = input.readlines()


valid_numbers = []
comparison_numbers = []

for line in lines:
    if "|" in line:
        valid_numbers.append(line.strip())
    else:
            comparison_numbers.append(line.strip())

def check_line(comparison_line):
    valid = True
    while valid == True:
        for i in range(len(comparison_line) - 1):
            invalid_order = f"{comparison_line[i + 1]}|{comparison_line[i]}"
            print(f"checking {invalid_order}")
            if invalid_order in valid_numbers:
                print("invalid")
                valid = False    
                           

def line_array(line):
        comparison_values = line.split(",")
        if len(comparison_values) > 1:
            return comparison_values

for line in comparison_numbers:
    result = line_array(line)
    if result:
        print(result)
    