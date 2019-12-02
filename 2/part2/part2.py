#!/usr/bin/env python3

def calc(instructions):
  for i in range(0, len(instructions), 4):
    if instructions[i] == 1:
      instructions[instructions[i+3]] = instructions[instructions[i+1]] + instructions[instructions[i+2]]
    elif instructions[i] == 2:
      instructions[instructions[i+3]] = instructions[instructions[i+1]] * instructions[instructions[i+2]]
    elif instructions[i] == 99:
      return instructions[0]

def main():
  with open('input.txt') as f:
    for line in f:
      instructions = line.split(',')
  instructions = [int(x) for x in instructions]
  for i in range(len(instructions)):
    for j in range(len(instructions)):
      s = [x for x in instructions]
      s[1] = i
      s[2] = j
      if calc(s) == 19690720:
        print(f'result: {i * 100 + j}')

main()
