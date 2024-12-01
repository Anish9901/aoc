# problem: https://adventofcode.com/2023/day/1
# input: https://adventofcode.com/2023/day/1/input
# sample = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']

with open('1_trebuchet_input.txt') as f:
    inputs = f.read().split('\n')

def trebuchet(input):
    for i in input:
        if i.isdigit():
            for j in input[::-1]:
                if j.isdigit():
                    return int(i+j)

res = 0

for input in inputs:
    res += trebuchet(input)
print('result =', res) # 53386

# part 2
# sample = ['two1nine' ,'eightwothree','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen']

def check_occurance(check_instance, inp_str, storage):
    ct1 = len(check_instance)
    for i in range(0,len(inp_str)):
        ct2 = 0
        for j in check_instance:
            if i < len(inp_str) and j == inp_str[i]:
                ct2 += 1
                i += 1 
            if ct1 == ct2:
                storage.add(i-ct1)

p2_res = 0
instances = [
    'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 
    '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

def curate_res(ins_idx_map):    
    res_idx_map = {}
    for k,v in ins_idx_map.items():
        res_idx_map[min(v)] = k
        res_idx_map[max(v)] = k
    s_idx_map = sorted(res_idx_map)
    res = ''
    res += str(instances.index(res_idx_map[s_idx_map[0]])+1) if not res_idx_map[s_idx_map[0]].isdigit() else res_idx_map[s_idx_map[0]]
    res += str(instances.index(res_idx_map[s_idx_map[-1]])+1) if not res_idx_map[s_idx_map[-1]].isdigit() else res_idx_map[s_idx_map[-1]]
    return int(res)

for inp_str in inputs:
    ins_idx_map = {}
    for inp_ins in instances:
        res_store = set()
        check_occurance(inp_ins, inp_str, res_store)
        if len(res_store) > 0:
            ins_idx_map[inp_ins] = res_store
    p2_res+=curate_res(ins_idx_map)
print('result p2 =', p2_res) # 53312
