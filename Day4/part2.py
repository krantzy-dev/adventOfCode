from pathlib import Path
import logging
logging.basicConfig(level=logging.DEBUG)
script_location = Path(__file__).parent
inputpath = script_location / 'input' / 'input.txt'



def check_position(grid, r, c, break_on_number=4, return_number=False, grid_buffered=False, logs=False):
    """
    Check all adjacent positions of (r, c) in grid.
    """
    #logging.debug(f'checking position r:{r}, c:{c}') if logs else None
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
    base_grid = [[int(x) for x in list(line.strip().replace('.','0').replace('@','1'))] for line in file.readlines()]

# we add a buffer of 0s around the grid to avoid checking bounds every time
zero_row = [0 for _ in range(len(base_grid[0])+2)]
middle_rows = [[0]+row+[0] for row in base_grid]
grid = [zero_row]+middle_rows+[zero_row]


changes = -1
replace_ones = []
sum_changes = 0
# we optimize it until no more changes happen
while changes != 0:
    changes = 0

    # we iterate over all (inner) positions of the grid
    for r in range(1, len(grid)-1):
        for c in range(1, len(grid[0])-1):

            if grid[r][c] == 1 and not check_position(grid, r, c, break_on_number=4, grid_buffered=True):
                replace_ones.append((r, c))
    
    for r, c in replace_ones:
        grid[r][c] = 0
        changes += 1
    
    replace_ones = []
    sum_changes += changes
    logging.debug(f'completed iteration with {changes} changes. TOTAL changes so far: {sum_changes}')


    