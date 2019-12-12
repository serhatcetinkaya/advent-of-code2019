#!/usr/bin/env python3

from itertools import permutations

def amplify(instructions, index, inputList):
    out_P = []
    if index == -1:
        return -1, -1
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
            if len(inputList) == 0:
                return (index), out_P
            instructions[instructions[index+1]] = inputList.pop(0)
            index += 2
        elif (instructions[index] % 100) == 4:
            out_P.append(instructions[instructions[index+1]])
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
            return -1, out_P


def main():
    result = 0
    with open('input.txt') as f:
        for line in f:
            instructions = line.split(',')
    instructions = [int(x) for x in instructions]

    phaseSequenceList = list(permutations([5, 6, 7, 8, 9]))

    for phaseSeq in phaseSequenceList:
        idx0, idx1, idx2, idx3, idx4, out0, out1, out2, out3, out4 = 0,0,0,0,0,0,0,0,0,0
        inputs0 = [phaseSeq[0]]
        inputs1 = [phaseSeq[1]]
        inputs2 = [phaseSeq[2]]
        inputs3 = [phaseSeq[3]]
        inputs4 = [phaseSeq[4]]

        ins0 = list(instructions)
        ins1 = list(instructions)
        ins2 = list(instructions)
        ins3 = list(instructions)
        ins4 = list(instructions)

        while idx4 != -1:
            if isinstance(out4, list):
                for i in out4:
                    inputs0.append(i)
            else:
                inputs0.append(out4)
            idx0, out0 = amplify(ins0, idx0, inputs0)
            if isinstance(out0, list):
                for i in out0:
                    inputs1.append(i)
            else:
                inputs1.append(out0)
            idx1, out1 = amplify(ins1, idx1, inputs1)
            if isinstance(out1, list):
                for i in out1:
                    inputs2.append(i)
            else:
                inputs2.append(out1)
            idx2, out2 = amplify(ins2, idx2, inputs2)
            if isinstance(out2, list):
                for i in out2:
                    inputs3.append(i)
            else:
                inputs3.append(out2)
            idx3, out3 = amplify(ins3, idx3, inputs3)
            if isinstance(out3, list):
                for i in out3:
                    inputs4.append(i)
            else:
                inputs4.append(out3)
            idx4, out4 = amplify(ins4, idx4, inputs4)
            if isinstance(out4, list):
                result = max(result, out4[0])
            else:
                result = max(result, out4)

    print(f'Result: {result}')



main()