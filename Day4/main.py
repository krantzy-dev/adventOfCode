from pathlib import Path
import logging
logging.basicConfig(level=logging.DEBUG)
script_location = Path(__file__).parent
inputpath = script_location / 'input' / 'input.txt'



def check_position(grid, r, c, break_on_number=4, return_number=False, grid_buffered=False, logs=False):
    """
    Check all adjacent positions of (r, c) in grid.
    """
    logging.debug(f'checking position r:{r}, c:{c}') if logs else None
    offsets = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    # add buffer to avoid checking bounds every time
    if not grid_buffered:
        zero_row = [0 for _ in range(len(grid[0])+2)]
        middle_rows = [[0]+row+[0] for row in grid]
        buffered_grid = [zero_row]+middle_rows+[zero_row]
    else:
        buffered_grid = grid

    adj_sum = 0

    for dy, dx in offsets:
        val = buffered_grid[r+dy][c+dx]
        
        adj_sum += val
        if adj_sum >= break_on_number and not return_number:
            return True
    
    return False if not return_number else adj_sum


with open(inputpath, 'r', encoding='utf-8') as file:
    lines = [[int(x) for x in list(line.strip().replace('.','0').replace('@','1'))] for line in file.readlines()]


# We got a two dimensional array with 0 and 1 values now.
# Our task is to find all the 1s with no more than 4 adjacent 1s (horizontally and vertically) and count them.

print(f'grid size: {len(lines)} x {len(lines[0])}')

zero_row = [0 for _ in range(len(lines[0])+2)]
middle_rows = [[0]+row+[0] for row in lines]
buffered_grid = [zero_row]+middle_rows+[zero_row]


count = 0
for r in range(1, len(buffered_grid)-1):
    for c in range(1, len(buffered_grid[0])-1):
        if buffered_grid[r][c] == 1:
            logs = True if r < 3 and c < 3 else False
            if not check_position(buffered_grid, r, c, break_on_number=4, grid_buffered=True, logs=logs):
                count += 1

print(f'result: {count}')

