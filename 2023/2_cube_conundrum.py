# problem: https://adventofcode.com/2023/day/2
# input: https://adventofcode.com/2023/day/2/input

with open('2_cube_conundrum_input.txt') as f:
    inputs = f.read().split('\n')
   
sample = [
'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
]

def populate_rgb(round):
    round = round.lstrip().split(' ')
    r, g, b = (0, 0, 0)
    for i in range(1, len(round), 2):
        if round[i][0] == 'r':
            r = round[i -1]
        elif round[i][0] == 'g':
            g = round[i - 1]
        else:
            b = round[i - 1]
    # print(r,g,b)
    return (int(r), int(g), int(b))


def get_input_dict():
    input_dict = {}
    # id: [(r,g,b), (r,g,b), ...]
    for game in inputs:
        # print(game)
        game = game.split(':')
        gameid = int(game[0].split('Game ')[-1])
        rgb_val = list()
        for round in game[1].split(';'):
            # get r,g,b values.
            rgb = populate_rgb(round)
            rgb_val.append(rgb)
        # if len(rgb_val) > 0:
        input_dict[gameid] = rgb_val
    return input_dict
# print(input_dict)


def part1(input_dict):
    res = 0
    check = (12, 13, 14)
    bad_games = set()
    for k, v in input_dict.items():
        for rgb in v:
            if check[0] - rgb[0] < 0 or check[1] - rgb[1] < 0 or check[2] - rgb[2] < 0:
                bad_games.add(k)
    for i in bad_games:
        input_dict.pop(i)
    for k, v in input_dict.items():
        res += k
    return res
print("result =", part1(get_input_dict())) 
# 2169

def part2(input_dict):
    res_pow = 0
    for k, v in input_dict.items():
        r, g, b = (0, 0, 0)
        for rgb in v:
            if rgb[0] > r:
                r = rgb[0]
            if rgb[1] > g:
                g = rgb[1]
            if rgb[2] > b:
                b = rgb[2]
        res_pow += r*g*b
    return res_pow

print("result p2 =", part2(get_input_dict()))
# 60948