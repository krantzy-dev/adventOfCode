from pathlib import Path
import logging
logging.basicConfig(level=logging.DEBUG)
script_location = Path(__file__).parent
inputpath = script_location / 'input' / 'input.txt'


with open(inputpath, 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file.readlines()]

pairs = []
target_length = 12

for l in lines:
    logging.debug(f'processing line: {l}')
    digits = [int(d) for d in l]

    top12_stack = []
    drop_count = len(digits) - target_length # maximum amount of digits we can drop to get to target length

    for i in range(len(digits)):
        d = digits[i]

        while top12_stack and d > top12_stack[-1] and drop_count > 0:
            top12_stack.pop()
            drop_count -= 1

        top12_stack.append(d)
    top12_digits = top12_stack[:target_length]
    sol = int(''.join(str(d) for d in top12_digits))
    logging.debug(f'found highest combination: {sol}')
    pairs.append(sol)
result = sum(pairs)

print(f'result: {result}')