#!/usr/bin/env python3

def main():
  index = 0
  initialInput = 1
  firstParam = 0
  secondParam = 0
  thirdParam = 0
  relativeBase = 0

  with open('input.txt') as f:
    for line in f:
      instructions = line.split(',')
  instructions = [int(x) for x in instructions]
  for _ in range(50000000):
    instructions.append(0)

  while True:
    if (instructions[index] % 100) not in (3, 99):
      if (instructions[index] // 100) % 10 == 0:
        firstParam = instructions[index+1]
      elif (instructions[index] // 100) % 10 == 1:
        firstParam = (index+1)
      elif (instructions[index] // 100) % 10 == 2:
        firstParam = relativeBase + instructions[index+1]
      if (instructions[index] // 1000) % 10 == 0:
        secondParam = instructions[index+2]
      elif (instructions[index] // 1000) % 10 == 1:
        secondParam = (index+2)
      elif (instructions[index] // 1000) % 10 == 2:
        secondParam = relativeBase + instructions[index+2]
      if (instructions[index] // 10000) % 10 == 0:
        thirdParam = instructions[index+3]
      elif (instructions[index] // 10000) % 10 == 1:
        thirdParam = (index+3)
      elif (instructions[index] // 10000) % 10 == 2:
        thirdParam = relativeBase + instructions[index+3]
    if (instructions[index] % 100) == 1:
      instructions[thirdParam] = instructions[firstParam] + instructions[secondParam]
      index += 4
    elif (instructions[index] % 100) == 2:
      instructions[thirdParam] = instructions[firstParam] * instructions[secondParam]
      index += 4
    elif (instructions[index] % 100) == 3:
      instructions[firstParam] = initialInput
      index += 2
    elif (instructions[index] % 100) == 4:
      print(f'Result: {instructions[firstParam]}')
      index += 2
    elif (instructions[index] % 100) == 5:
      index = instructions[secondParam] if instructions[firstParam] > 0 else index + 3
    elif (instructions[index] % 100) == 6:
      index = instructions[secondParam] if instructions[firstParam] == 0 else index + 3
    elif (instructions[index] % 100) == 7:
      instructions[thirdParam] = 1 if instructions[firstParam] < instructions[secondParam] else 0
      index += 4
    elif (instructions[index] % 100) == 8:
      instructions[thirdParam] = 1 if instructions[firstParam] == instructions[secondParam] else 0
      index += 4
    elif (instructions[index] % 100) == 9:
      relativeBase += instructions[firstParam]
      index += 2
    elif (instructions[index] % 100) == 99:
      break

main()
