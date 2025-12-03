from pathlib import Path

script_location = Path(__file__).parent
inputpath = script_location / 'input' / 'input.txt'

map={'R':'+', 'L':'-'}
with open(inputpath, 'r', encoding='utf-8') as file:
    lines = [int(map[line[0]]+line.strip()[1:]) for line in file]


start = 50
result = start
zeroes = 0


for l in lines:
    start = result
    result =  start + l


    if l > 0:
        zeroes += (result // 100) - (start // 100)
    elif l < 0:
        zeroes += ((start-1) // 100) - ((result-1) // 100)


print(f'final number: {zeroes}')