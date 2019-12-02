#!/usr/bin/env python3

def main():
  with open('input.txt') as f:
    for line in f:
      instructions = line.split(',')
  instructions = [int(x) for x in instructions]
  for i in range(0, len(instructions), 4):
    if instructions[i] == 1:
      instructions[instructions[i+3]] = instructions[instructions[i+1]] + instructions[instructions[i+2]]
    elif instructions[i] == 2:
      instructions[instructions[i+3]] = instructions[instructions[i+1]] * instructions[instructions[i+2]]
    elif instructions[i] == 99:
      print(f'result: {instructions[0]}')

main()
