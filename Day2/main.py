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

candidates = []
for r in ranges:
    start, end = r

    for num in range(start, end + 1):
        str_num = str(num)
        length = len(str_num)
        
        if length % 2 == 0:
            if str_num[:(length // 2)] == str_num[(length // 2):]:
                candidates.append(num)
                logging.info(f'Found candidate: {num} in range {r}')
            else:
                logging.debug(f'Not a candidate: {num} in range {r}')
        else:
            logging.debug(f'Odd length, skipping: {num} in range {r}')


# adding all candidates together
result = sum(candidates)
print(f'final result: {result}')