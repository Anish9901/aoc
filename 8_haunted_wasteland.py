# problem: https://adventofcode.com/2023/day/8
# input: https://adventofcode.com/2023/day/8/input

with open('8_haunted_wasteland_input.txt') as f:
    inputs = f.read().split('\n')
    directions = inputs[0]
    network = inputs[2:]
# directions = 'LR'
# network = [
# 'BBB = (DDD, EEE)',
# 'AAA = (BBB, CCC)',
# 'CCC = (ZZZ, GGG)',
# 'DDD = (DDD, DDD)',
# 'EEE = (EEE, EEE)',
# 'GGG = (GGG, GGG)',
# 'ZZZ = (ZZZ, ZZZ)'
# ]

# directions = 'LR'
# network = [
# '11A = (11B, XXX)',
# '11B = (XXX, 11Z)',
# '11Z = (11B, XXX)',
# '22A = (22B, XXX)',
# '22B = (22C, 22C)',
# '22C = (22Z, 22Z)',
# '22Z = (22B, 22B)',
# 'XXX = (XXX, XXX)',
# ] 
network_dict = {}
for node in network:
    x, y = node.split(' = ')
    y = y.lstrip('(')
    y = y.rstrip(')')
    y = y.split(', ')
    network_dict[x] = y


dir = {'R': 1, 'L': 0}
ct = 0
i = 0
next = None
while next != 'ZZZ':
    if ct == 0:
        next = network_dict['AAA'][dir[directions[i]]]
        ct += 1 
    else:
        next = network_dict[next][dir[directions[i]]]
        ct += 1
    if next == 'ZZZ':
        print("result =", ct) # 16043
    i += 1
    if i == len(directions):
        i = 0

# part 2

# zlist = ['HJZ', 'ZZZ', 'SBZ', 'RFZ', 'VPZ', 'PQZ']
# alist = ['FDA', 'AAA', 'BPA', 'BVA', 'NDA', 'QCA']
# ct = 0
# i = 0

# for k, v in network_dict.items():
#     if k[-1] == 'A':
#         alist.append(k)
#         print(k)
#     if k[-1] == 'Z':
#         zlist.append(k)
#         # print(k)
# next = []
# while sorted(next) != sorted(zlist):
#     if ct == 0:
#         for j in alist:
#             print(network_dict[j][dir[directions[i]]])
#             next.append(network_dict[j][dir[directions[i]]])
#         ct += 1 
#     else:
#         l = []
#         for j in next:
#             l.append(network_dict[j][dir[directions[i]]])
#         next = l
#         print(next)
#         ct += 1
#     if all([i[-1] == 'Z' for i in next]):
#         print(ct)
#     i += 1
#     if i == len(directions):
#         i = 0

# Found using part 1 for solving part 2
# FDA -> 'HJZ' 19199
# AAA -> 'ZZZ' 16043
# BPA -> 'SBZ' 11309
# BVA -> 'RFZ' 17621
# NDA -> 'VPZ' 20777
# QCA -> 'PQZ' 15517

lcm = 15726453850399 # <- part 2 res (lcm of above values) 
print('result p2 =', lcm)
