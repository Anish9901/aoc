with open('5_cafeteria.txt') as f:
    inputs1, inputs2 = f.read().split('\n\n')
inputs1 = [i.split('-') for i in inputs1.split('\n')]
inputs2 = [i for i in inputs2.split('\n')]

fresh = 0
for x in inputs2:
    for i, j in inputs1:
        if int(i) <= int(x) <= int(j):
            fresh += 1
            break

inputs1 = [[int(i), int(j)] for i, j in inputs1]
inputs1 = sorted(inputs1, key=lambda x: x[0])

for i in range(len(inputs1)-1):
    if inputs1[i][1] >= inputs1[i+1][1]:
        inputs1[i+1][1] = inputs1[i][1]
        inputs1[i+1][0] = inputs1[i][1] + 1
    elif inputs1[i][1] >= inputs1[i+1][0]:
        inputs1[i+1][0] = inputs1[i][1] + 1

count = 0
for i, j in inputs1:
    count += j-i+1

print("Part 1:", fresh)
print("Part 2:", count)
