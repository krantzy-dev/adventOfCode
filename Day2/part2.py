from pathlib import Path
import logging

logging.basicConfig(level=logging.ERROR, format='%(levelname)s:%(message)s')

script_location = Path(__file__).parent
inputpath = script_location / 'input' / 'input.txt'

# fetch file and parse ranges
with open(inputpath, 'r', encoding='utf-8') as file:
    tmp = file.readline().strip().split(',') #file has only one line
    ranges = [(int(i.split('-')[0]), int(i.split('-')[1])) for i in tmp]




candidates = set() # using set to avoid duplicates (like '1111' with '11'+'11' and '1'+'1'+'1'+'1')
for r in ranges:
    start, end = r

    len_start = len(str(start))
    len_end = len(str(end))


    # get all eligible lengths between start and end
    eligible_lengths = [i for i in range(len_start, len_end+1)]
    # get all divisors for each length
    divisor_lengths = {}
    for l in eligible_lengths:
        divisors = set()
        for i in range(1, l//2+1):
            if l % i == 0:
                divisors.add(i)
        divisor_lengths[l] = divisors
    

    # generate all candidates for each length and divisor
    for key in divisor_lengths:
        divisors = divisor_lengths[key]

        # now generate all numbers with length of divisor (d) and repeat them to get the full number (of length key)
        for d in divisors:
            repeat_count = key / d # d must be divisible by key

            for i in range(10**(d-1), 10**(d)):
                num = int(str(i)*int(repeat_count))
                if num >= start and num <= end:
                    candidates.add(num)
                    logging.debug(f'found candidate: {num} in range {start}-{end}')
                else:
                    logging.debug(f'skipping candidate: {num} in range {start}-{end}')
                    continue

for i in candidates:
    logging.debug(f'candidate: {i}')

result = sum(candidates)
print(f'final result: {result}')
