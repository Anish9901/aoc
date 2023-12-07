# problem: https://adventofcode.com/2023/day/7
# input: https://adventofcode.com/2023/day/7/input

with open('7_camel_cards_input.txt') as f:
    inputs = f.read().split('\n')

sample = [
'32T3K 765',
'T55J5 684',
'KK677 28',
'KTJJT 220',
'QQQJA 483',
]

def hand_parser_part1():
    vok,ivok,fh,tok,tp,op,hc = {},{},{},{},{},{},{}
    for hands in inputs:
        hand, bid = hands.split(' ')
        set_hand = len(set(hand))
        if set_hand == 1:
            vok[hand] = bid
        elif set_hand == 2:
            ct = 0
            for i in hand:
                if hand[0] == i:
                    ct += 1
            if ct == 4 or ct == 1:
                ivok[hand] = bid
            else:
                fh[hand] = bid
        elif set_hand == 3:
            # could be 3 of a kind or 2 pair
            ct = 0
            ct2 = 0
            a,b,_ = set(hand)
            for i in hand:
                if a == i:
                    ct += 1
                if b == i:
                    ct2 += 1
            if (ct == 1 and ct2 == 2) or (ct == 2 and ct2 == 1) or (ct == 2 and ct2 == 2):
                tp[hand] = bid
            else:
                tok[hand] = bid

        elif set_hand == 4:
            op[hand] = bid
        else:
            hc[hand] = bid
    return vok,ivok,fh,tok,tp,op,hc



def rank(x):
    rankmap = {
        'A': 1,
        'K': 2,
        'Q': 3,
        'J': 4,
        'T': 5,
        '9': 6,
        '8': 7,
        '7': 8,
        '6': 9,
        '5': 10,
        '4': 11,
        '3': 12,
        '2': 13
    }
    return rankmap[x]


srtd = [*hand_parser_part1()]
for i in range(7):
    srtd[i] = dict(sorted(srtd[i].items(), key=lambda x: [rank(x[0][i]) for i in range(len(x[0]))]))

bidsinorder = []
res = 0 
for i in srtd:
    for k, v in i.items():
        bidsinorder.append(int(v))
bidsinorder.reverse()

for i in range(len(bidsinorder)):
    res += bidsinorder[i] * (i + 1)

print("result = ", res)
# 253954294

# part 2:
def j_hand_parser(hand, bid, vok, ivok, fh, tok, tp, op, hc):
    set_hand = len(set(hand))
    ctj = 0
    for i in hand:
        if i == 'J':
            ctj += 1
    if ctj == 5 or ctj == 4:
        vok[hand] = bid
    if ctj == 3:
        if set_hand == 2:
            #JJJQQ
            vok[hand] = bid
        if set_hand == 3:
            #JJJQK
            ivok[hand] = bid
    if ctj == 2:
        if set_hand == 2:
            #JJAAA
            vok[hand] = bid
        if set_hand == 3:
            #JJAQQ
            ivok[hand] = bid
        if set_hand == 4:
            #JJAQK
            tok[hand] = bid
    if ctj == 1:
        if set_hand == 2:
            # JAAAA
            vok[hand] = bid
        if set_hand == 3:
            ct = 0
            ct2 = 0
            a, b, _ = set(hand)
            for i in hand:
                if a == i:
                    ct += 1
                if b == i:
                    ct2 += 1
            if (ct == 1 and ct2 == 2) or (ct == 2 and ct2 == 1) or (ct == 2 and ct2 == 2):
                # TAJAT full house
                fh[hand] = bid
            else: # JQAAA
                ivok[hand] = bid
        if set_hand == 4:
            # JQAKQ
            tok[hand] = bid
        if set_hand == 5:
            # JQAKT
            op[hand] = bid
        
        
            
def hand_parser_part2():
    vok,ivok,fh,tok,tp,op,hc = {},{},{},{},{},{},{}
    for hands in inputs:
        hand, bid = hands.split(' ')
        set_hand = len(set(hand))
        if 'J' in hand:
            j_hand_parser(hand, bid, vok, ivok, fh, tok, tp, op, hc)
        else:
            if set_hand == 1:
                vok[hand] = bid
            elif set_hand == 2:
                ct = 0
                for i in hand:
                    if hand[0] == i:
                        ct += 1
                if ct == 4 or ct == 1:
                    ivok[hand] = bid
                else:
                    fh[hand] = bid
            elif set_hand == 3:
                # could be 3 of a kind or 2 pair
                ct = 0
                ct2 = 0
                a,b,_ = set(hand)
                for i in hand:
                    if a == i:
                        ct += 1
                    if b == i:
                        ct2 += 1
                if (ct == 1 and ct2 == 2) or (ct == 2 and ct2 == 1) or (ct == 2 and ct2 == 2):
                    tp[hand] = bid
                else:
                    tok[hand] = bid
            elif set_hand == 4:
                op[hand] = bid
            else:
                hc[hand] = bid
    return vok,ivok,fh,tok,tp,op,hc

srtdp2 = [*hand_parser_part2()]
def rankp2(x):
    rankmap = {
        'A': 1,
        'K': 2,
        'Q': 3,
        'T': 4,
        '9': 5,
        '8': 6,
        '7': 7,
        '6': 8,
        '5': 9,
        '4': 10,
        '3': 11,
        '2': 12,
        'J': 13
    }
    return rankmap[x]

for i in range(7):
    srtdp2[i] = dict(sorted(srtdp2[i].items(), key=lambda x: [rankp2(x[0][i]) for i in range(len(x[0]))]))

bidsinorderp2 = []
resp2 = 0 
for i in srtdp2:
    for k, v in i.items():
        bidsinorderp2.append(int(v))
bidsinorderp2.reverse()
for i in range(len(bidsinorderp2)):
    resp2 += bidsinorderp2[i] * (i + 1)

print("result p2 = ", resp2)
# 254837398