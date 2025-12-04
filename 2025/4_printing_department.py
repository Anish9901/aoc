with open('4_printing_department.txt') as f:
    inputs = [list(i) for i in f.read().split('\n')]

sum_roll = 0

for i in range(len(inputs)):
    for j in range(len(inputs[i])):
        count = 0
        if inputs[i][j] == '@':
            top = [(i-1, j-1), (i-1, j), (i-1, j+1)]
            mid = [(i, j-1), (i, j+1)]
            bottom = [(i+1, j-1), (i+1, j), (i+1, j+1)]
            sp = top + mid + bottom
            for x, y in sp:
                if x >= 0 and y >= 0 and x < len(inputs) and y < len(inputs[i]) and inputs[x][y] == '@':
                    count +=1
            if count < 4:
                sum_roll += 1

print("Part 1:", sum_roll)

sum_roll = 0
inputs_after = []
for z in range(len(inputs)*len(inputs[i])):
    track_change_flag = 0
    for i in range(len(inputs)):
        for j in range(len(inputs[i])):
            count = 0
            if inputs[i][j] == '@':
                top = [(i-1, j-1), (i-1, j), (i-1, j+1)]
                mid = [(i, j-1), (i, j+1)]
                bottom = [(i+1, j-1), (i+1, j), (i+1, j+1)]
                sp = top + mid + bottom
                for x, y in sp:
                    if x >= 0 and y >= 0 and x < len(inputs) and y < len(inputs[i]) and inputs[x][y] == '@':
                        count +=1
                if count < 4:
                    sum_roll += 1
                    inputs[i][j] = '.'
                    track_change_flag = 1
    if track_change_flag == 0:
        break

# print(inputs)
print("Part 2:", sum_roll)
