#!/usr/bin/env python3

def main():
    orbitMap = {}
    numberOfOrbits = 0

    with open('input.txt') as f:
        for line in f:
            objects = line.rstrip('\n').split(')')
            orbitMap[objects[1]] = objects[0]

    for obj in orbitMap:
        while obj in orbitMap:
            numberOfOrbits += 1
            obj = orbitMap[obj]

    print(f'Result: {numberOfOrbits}')

main()