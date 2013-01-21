#!/usr/bin/env python
from __future__ import division

import sys
import math
import itertools


def get_permutations(input):
    n = int(input.strip())
    number_of_permutations = str(math.factorial(n))
    permutations = '\n'.join(' '.join(map(str,permutation)) for permutation in itertools.permutations(list(range(1, n+1))))
    return '\n'.join([number_of_permutations, permutations])


def test():
    test_string = '3'
    result = get_permutations(test_string)
    print(result)
    assert result == '''\
6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1'''
    print('Test passed!')

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename) as file:
            print(get_permutations(file.read()))
    else:
        test()

if __name__ == '__main__':
    main()