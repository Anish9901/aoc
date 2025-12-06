with open('/home/anish/oss/aoc/2025/6_trash_compactor.txt') as f:
    inputs = f.read().split('\n')
inputs_2 = inputs
inputs = [i.strip() for i in inputs]
inputs_cleaned = []
operations = [i for i in inputs[-1].split(' ') if not i.isspace() and not i=='']

for i in range(len(inputs) - 1):
    inputs_cleaned.append([x for x in inputs[i].split(' ') if x.isnumeric()])

sum = []
mul = []

for i in range(len(operations)):
    if operations[i] == '*':
        mul.append([x[i] for x in inputs_cleaned])
    if operations[i] == '+':
        sum.append([x[i] for x in inputs_cleaned])

mul_list_result = 0
sum_list_result = 0

for i in mul:
    y = 1
    for x in i:
        y *= int(x)
    mul_list_result += y

for i in sum:
    y = 0
    for x in i:
        y += int(x)
    sum_list_result += y

print("Part 1:", sum_list_result + mul_list_result)


count = 0
operations_2 = []
inputs_2 = [list(x) for x in inputs_2]
for i in range(len(inputs_2[-1]) - 1):
    if inputs_2[-1][i+1] == '*' or inputs_2[-1][i+1] == '+':
        operations_2.append(count)
        count = 0
    else:
        count+=1

#### Part 2 ####

operations_2.append(count+1)
inputs_2 = inputs_2[0:-1]
sum_2 = []
mul_2 = []
for i in range(len(operations_2)):
    x = []
    offset = 0
    if i > 0:
        for j in operations_2[:i]:
            offset+=j
        offset += len(operations_2[:i])
    for m in range(0 + offset, operations_2[i] + offset):
        z = ''
        for y in inputs_2:
            if y[m] != ' ':
                z += y[m]
        x.append(z)
    if operations[i] == '*':
        mul_2.append(x)
    elif operations[i] == '+':
        sum_2.append(x)

mul_2_list_result = 0
sum_2_list_result = 0

for i in mul_2:
    y = 1
    for x in i:
        y *= int(x)
    mul_2_list_result += y

for i in sum_2:
    y = 0
    for x in i:
        y += int(x)
    sum_2_list_result += y

print("Part 2:", sum_2_list_result + mul_2_list_result)
