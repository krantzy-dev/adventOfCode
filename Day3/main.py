# This time we got a txt file with mulitple lines of long numbers.
# Our task is to find the highest combination of two digits per line and sum them up.
# Our digits must be in order though. So having "8888888891" would yield 91 as the highest combination even though 8 is higher than 1.
from pathlib import Path
import logging
logging.basicConfig(level=logging.DEBUG)
script_location = Path(__file__).parent
inputpath = script_location / 'input' / 'input.txt'


with open(inputpath, 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file.readlines()]

pairs = []


for l in lines:
    logging.debug(f'processing line: {l}')
    digits = [int(d) for d in l]

    highest = 0
    second_highest = 0

    # plan is to iterate over the digits and compare each number with the second highest digit.
    # If we find a higher number, we check if it's also higher than the highest number.
    # When its higher than the highest number we reset the second highest number and set the highest number to the current number.
    # We need to look out for the edge case where the highest number is at the end of the line. Then the highest numer cannot be our first digit.
    for i in range(len(digits)):
        d = digits[i]
        if d > second_highest:

            if i == len(digits)-1 or d <= highest:
                second_highest = d
            elif d > highest:
                second_highest = 0
                highest = d
    
    logging.debug(f'found highest combination: {highest}, {second_highest}')
    pairs.append(10*highest+second_highest)
result = sum(pairs)

print(f'result: {result}')