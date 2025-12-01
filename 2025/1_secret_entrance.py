with open('1_secret_entrance.txt') as f:
    inputs = f.read().split('\n')

###### PART 1 ######
start = 50
zero_counter = 0
track_hand = start
for i in inputs:
    if i.startswith('L'):
        track_hand = (track_hand - int(i[1:])) % 100
    elif i.startswith('R'):
        track_hand = (track_hand + int(i[1:])) % 100
    if track_hand == 0:
        zero_counter += 1

print(zero_counter)

###### PART 2 ######

### BRUTE FORCE ###
""" track_hand = start
zero_pass_counter = 0
l = [i for i in range(0, 100)]
for i in inputs:
    stop = int(i[1:])
    if i.startswith('L') :
        for j in range(1, stop):
            if l[(track_hand-j)%100] == 0:
                zero_pass_counter +=1
        track_hand = (track_hand - stop) % 100
    elif i.startswith('R') :
        for j in range(1, stop):
            if l[(track_hand+j)%100] == 0:
                zero_pass_counter +=1
        track_hand = (track_hand + stop) % 100
    print('track hand:', track_hand, "zero_pass_counter", zero_pass_counter)
print(zero_pass_counter+zero_counter) """

### EFFICIENT ###
track_hand = start
zero_pass_counter = 0
for i in inputs:
    stop = int(i[1:])
    if i.startswith('L'):
        zero_pass_counter += abs((track_hand - stop)//100)
        if (track_hand) % 100 == 0:
            zero_pass_counter -= 1
        track_hand = (track_hand - stop) % 100
    elif i.startswith('R'):
        zero_pass_counter += abs((track_hand + stop)//100)
        if (track_hand + stop) % 100 == 0:
            zero_pass_counter -= 1
        track_hand = (track_hand + stop) % 100
    # print('track hand:', track_hand, "zero_pass_counter", zero_pass_counter)
print(zero_pass_counter + zero_counter)
