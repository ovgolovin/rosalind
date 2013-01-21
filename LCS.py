#!/usr/bin/env python
from __future__ import division

from collections import Counter
import sys

def moving_window(string, n):
    for i in range(0, len(string) - n):
        yield string[i:i+n]


def get_common_substring(input):
    strings = map(lambda x: x.strip(), input.strip().split("\n"))
    smallest_string = min(strings, key = lambda x: len(x))
    for n in range(len(smallest_string), 0, -1):
        for substring in moving_window(smallest_string, n):
            if all(substring in string for string in strings):
                return substring
    return None

def test():
    test_string = '''\
GATTACA
TAGACCA
ATACA'''
    result = get_common_substring(test_string)
    print(result)
    assert result == 'AC'
    print('Test passed!')

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename) as file:
            print(get_common_substring(file.read()))
    else:
        test()

if __name__ == '__main__':
    main()