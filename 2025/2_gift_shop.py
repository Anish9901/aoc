with open('/home/anish/oss/aoc/2025/2_gift_shop.txt') as f:
    inputs = f.read().split(',')

inputs = [i.split('-') for i in inputs]

included_p1 = []
sum_p1 = 0
sum_p2 = 0
included_p2 = []
for i in inputs:
    for j in range(int(i[0]), int(i[1])+1):
        j = str(j)
        if len(j) % 2 == 0 and j[0:len(j)//2] == j[len(j)//2:]:
            sum_p1+=int(j)
            included_p1.append(int(j))
        for k in range(0, len(j)//2):
            if j.count(j[0:k+1]) * (k+1) == len(j) and int(j) not in included_p1:
                included_p2.append(int(j))
                sum_p2 += int(j)
# print(included_p1)
print("Part 1:", sum_p1)
# print(included_p2)
# print(sum_p2)
print("Part 2:", sum_p1+sum_p2)
