import re
with open("3.txt") as input:
    input_text = input.read()

end_result = 0

pairs = []
split_input = input_text.split('mul')
for string in split_input:

    match = re.match(r"^\(\d+,\d+\)", string)
    if match:
        pairs.append(match.group(0)) #I hate regex so I asked for help from ChatGPT for this one.


for pair in pairs:
    expression = list(filter(None, re.split("[(,)]", pair)))
    result = int(expression[0]) * int(expression[1])
    end_result += result

print(end_result)



