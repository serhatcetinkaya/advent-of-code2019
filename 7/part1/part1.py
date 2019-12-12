#!/usr/bin/env python3

from itertools import permutations

def amplify(initialInstructions, phaseSeq, initialInput):
    index = 0
    firstParam = 0
    secondParam = 0
    output = [initialInput]
    for phase in phaseSeq:
        output.append(phase)
        instructions = [x for x in initialInstructions]
        index = 0
        while True:
            if (instructions[index] % 100) not in (3, 4, 99):
                firstParam = instructions[index+1] if (instructions[index] // 100) % 10 == 0 else (index+1)
                secondParam = instructions[index+2] if (instructions[index] // 1000) % 10 == 0 else (index+2)
            if (instructions[index] % 100) == 1:
                instructions[instructions[index+3]] = instructions[firstParam] + instructions[secondParam]
                index += 4
            elif (instructions[index] % 100) == 2:
                instructions[instructions[index+3]] = instructions[firstParam] * instructions[secondParam]
                index += 4
            elif (instructions[index] % 100) == 3:
                instructions[instructions[index+1]] = output.pop()
                index += 2
            elif (instructions[index] % 100) == 4:
                output.append(instructions[instructions[index+1]])
                index += 2
            elif (instructions[index] % 100) == 5:
                index = instructions[secondParam] if instructions[firstParam] != 0 else index + 3
            elif (instructions[index] % 100) == 6:
                index = instructions[secondParam] if instructions[firstParam] == 0 else index + 3
            elif (instructions[index] % 100) == 7:
                instructions[instructions[index+3]] = 1 if instructions[firstParam] < instructions[secondParam] else 0
                index += 4
            elif (instructions[index] % 100) == 8:
                instructions[instructions[index+3]] = 1 if instructions[firstParam] == instructions[secondParam] else 0
                index += 4
            elif (instructions[index] % 100) == 99:
                break
    
    return output[0]

def main():
    result = 0

    with open('input.txt') as f:
        for line in f:
            instructions = line.split(',')
    instructions = [int(x) for x in instructions]

    phaseSequenceList = list(permutations([0, 1, 2, 3, 4]))
    for phaseSeq in phaseSequenceList:
        copyInstructions = [x for x in instructions]
        result = amplify(copyInstructions, phaseSeq, 0) if amplify(copyInstructions, phaseSeq, 0) > result else result

    print(f'Result: {result}')



main()