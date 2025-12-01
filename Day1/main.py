# We are tasked with finding the password to a save secured by a lock. 
# The locking mechanism is a wheel with the numbers 0-99 on it. If it reaches under 0 or over 99 there is an overflow to 99 or 0 respectively.
# We will get a list of instructions that outline a direction to turn the wheel (L -> - ; R -> +) and the number of turns made (example L23; R12)
# The wheel starts at the number 50. Our objective is to find how many times we turn the wheel to the number 0.
# The input is a .txt file in ./input/input.txt
from pathlib import Path

script_location = Path(__file__).parent
inputpath = script_location / 'input' / 'input.txt'

map={'R':'+', 'L':'-'}
with open(inputpath, 'r', encoding='utf-8') as file:
    lines = [int(map[line[0]]+line.strip()[1:]) for line in file]


result = 50
zeroes = 0
for i in lines:
    result = (result+i)%100
    zeroes+=1 if result==0 else 0
    print(f'num: {i}; result: {result}; zeroes: {zeroes}')

print(f'final number: {zeroes}')