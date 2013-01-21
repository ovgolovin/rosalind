#!/usr/bin/env python

import itertools
import sys


def split_input(input):
    return map(lambda x: x.strip(), input.split('\n'))[:2]


def get_hamming_distance(input):
    a,b = split_input(input)
    return sum(x != y for x,y in itertools.izip(a,b))

def test():
    test_string = '''\
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT'''
    result = get_hamming_distance(test_string)
    print(result)
    assert result == 7
    print('Test passed!')

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename) as file:
            print(get_hamming_distance(file.read()))
    else:
        test()

if __name__ == '__main__':
    main()