#!/usr/bin/env python3

from collections import defaultdict

def path(obj, objectMap):
    parent = objectMap.get(obj)
    if not parent:
        return []
    else:
        return [parent] + path(parent, objectMap)

def main():
    orbitMap = {}
    orbitMap = defaultdict(list)

    with open('input.txt') as f:
        for line in f:
            objects = line.rstrip('\n').split(')')
            orbitMap[objects[1]] = objects[0]

    trip = [set(path(planet, orbitMap)) for planet in ['YOU', 'SAN']]

    print(f'Result: {len(set.symmetric_difference(*trip))}')

main()