#!/usr/bin/env python3

def main():
  index = 0
  systemID = 1
  firstParam = 0
  secondParam = 0

  with open('input.txt') as f:
    for line in f:
      instructions = line.split(',')
  instructions = [int(x) for x in instructions]
  while True:
    if (instructions[index] % 100) in (1, 2):
      firstParam = instructions[index+1] if (instructions[index] // 100) % 10 == 0 else (index+1)
      secondParam = instructions[index+2] if (instructions[index] // 1000) % 10 == 0 else (index+2)
    if (instructions[index] % 100) == 1:
      instructions[instructions[index+3]] = instructions[firstParam] + instructions[secondParam]
      index += 4
    elif (instructions[index] % 100) == 2:
      instructions[instructions[index+3]] = instructions[firstParam] * instructions[secondParam]
      index += 4
    elif (instructions[index] % 100) == 3:
      instructions[instructions[index+1]] = systemID
      index += 2
    elif (instructions[index] % 100) == 4:
      print(instructions[instructions[index+1]])
      index += 2
    elif (instructions[index] % 100) == 99:
      print("Halted")
      break

main()
