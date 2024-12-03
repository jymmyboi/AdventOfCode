with open("1.txt") as input:
    inputText = input.readlines()

firstColumn = []
secondColumn = []
additionVal = 0
total = 0

for line in inputText:
    lineSplit = line.split('   ')
    firstColumn.append(lineSplit[0])
    secondColumn.append(lineSplit[1].strip())

firstColumn.sort()
secondColumn.sort()


for i in range(len(firstColumn)):

    if int(firstColumn[i]) > int(secondColumn[i]):
        additionVal = int(firstColumn[i]) - int(secondColumn[i])
    elif int(firstColumn[i]) < int(secondColumn[i]):
        additionVal = int(secondColumn[i]) - int(firstColumn[i])
    else:
        additionVal = 0
    total += additionVal

print(total)
