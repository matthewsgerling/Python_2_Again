import re

mobyOldCount = 0
mobyWaterCount = 0

with open('Moby_Dick_Chapter_1.txt','r') as input_file:
    for line in input_file:
        line = line.lower()
        line_clean = re.sub(r'[^\w\s]', '', line)
        line_split = line_clean.split()
        for word in line_split:
            if word == 'old':
                mobyOldCount += 1
            if word == 'water':
                mobyWaterCount += 1

print('Number of times old is said', mobyOldCount)
print('Number of times water is said', mobyWaterCount)

senseWaterCount = 0
senseOldCount = 0


with open('Sense_and_Sensibility_Chapter_1.txt','r') as input_file:
    for line in input_file:
        line = line.lower()
        line_clean = re.sub(r'[^\w\s]', '', line)
        line_split = line_clean.split()
        for word in line_split:
            if word == 'old':
                senseOldCount += 1
            if word == 'water':
                senseWaterCount += 1

print('Number of times old is said', senseOldCount)
print('Number of times water is said', senseWaterCount)
