# This time we are given ranges of numbers.
# The input contains these ranges in the format "a-b", separated by commas.
# Our task is to find all the numbers in each range that consist of two repeating numbers.
# In the end we add all these numbers together to get our final result.
# The input is a .txt file in ./input/input.txt

from pathlib import Path
import logging

logging.basicConfig(level=logging.ERROR, format='%(levelname)s:%(message)s')

script_location = Path(__file__).parent
inputpath = script_location / 'input' / 'input.txt'

# fetch file and parse ranges
with open(inputpath, 'r', encoding='utf-8') as file:
    tmp = file.readline().strip().split(',') #file has only one line
    ranges = [(int(i.split('-')[0]), int(i.split('-')[1])) for i in tmp]

# a few observations:
# numbers with a repitition must have an even number of digits
# e.g. 11, 1221, 5544, 6788
# we can determine all numbers with repititions by splitting the number in half and checking if both halves are the same


# we collect candidates by generating all numbers between the first half of the digits of start and end of each range.
candidates = []
for r in ranges:
    start, end = r

    len_start = len(str(start))
    len_end = len(str(end))

    if len_start < 2 and end < 11:
        continue # no candidates possible
    
    print(f'checking range: {start}-{end}')

    half_start = int(str(start)[:(len_start//2)]) if len_start > 1 else 1 # at least two digits needed
    half_end = int(str(end)[:((len_end+1)//2)])

    for i in range(len_start, len_end+1):
        
        if i%2 != 0:
            continue # skip odd lengths

        half_len = i//2

        for j in range(half_start, half_end+1):

            num = int(str(j)*2)
            if num >= start and num <= end:
                candidates.append(num)
                logging.debug(f'found candidate: {num} in range {start}-{end}')
            else:
                logging.debug(f'skipping candidate: {num} in range {start}-{end}')
                continue



# adding all candidates together
result = sum(candidates)
print(f'final result: {result}')