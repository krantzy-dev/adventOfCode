from pathlib import Path
import logging
logging.basicConfig(level=logging.DEBUG)
script_location = Path(__file__).parent
inputpath = script_location / 'input' / 'input.txt'

with open(inputpath, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    ranges = [(int(line.split('-')[0]), int(line.strip().split('-')[1])) for line in lines if '-' in line]

# sort ranges by start value
ranges.sort(key=lambda x: x[0])


merged = [ranges[0]]
for current_start, current_end in ranges[1:]:
    last_start, last_end = merged[-1]
    if current_start <= last_end:
        merged[-1] = (last_start, max(last_end, current_end))
    else:
        merged.append((current_start, current_end))

fresh_ids = sum(r[1] - r[0] + 1 for r in merged)
print(f'fresh count: {fresh_ids}')

