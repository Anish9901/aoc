with open('3_lobby.txt') as f:
    inputs = f.read().split('\n')

sum_joltage = 0

for i in inputs:
    temp_list = []
    for j in range(len(str(i))-1):
        for k in range(j+1, len(str(i))):
            temp_list.append(int(str(i)[j] + str(i)[k]))
    sum_joltage += max(temp_list)
# print(inputs)
print(sum_joltage)