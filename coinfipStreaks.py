import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    sample = []

    for sampleNumber in range(100): # Flip a coin a 100 times, registering H or T in sample list
        if random.randint(0,1) == 0:
            sample.append('H')
        else:
            sample.append('T')

    for i in range(100 - 6):
        if sample[i] == sample[i+1] == sample[i+2] == sample[i+3] == sample[i+4] == sample[i+5]:
            numberOfStreaks += 1
            break

print('Chance of streak: %s%%' % (numberOfStreaks / 100))