from pathlib import Path
import logging
logging.basicConfig(level=logging.DEBUG)
script_location = Path(__file__).parent
inputpath = script_location / 'input' / 'input.txt'


with open(inputpath, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    ranges = [(int(line.split('-')[0]), int(line.strip().split('-')[1])) for line in lines if '-' in line]
    ids = [int(line.strip()) for line in lines if '-' not in line and line.strip() != '']

fresh_count = 0
not_fresh_count = 0

for i in ids:
    logging.debug(f'processing id: {i}')
    for r in ranges:
        if r[0] <= i <= r[1]:
            fresh_count += 1
            logging.debug(f'processed id: {i} is in range: {r}, fresh count increased to {fresh_count}')
            break

print(f'fresh count: {fresh_count}')
