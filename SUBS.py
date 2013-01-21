#!/usr/bin/env python

import sys
import re


def parse_input(input):
    return map(lambda x: x.strip(), input.split('\n'))[0:2]

def get_substring_locations(input):
    print(input)
    s,t = parse_input(input)
    pattern = re.compile(r'(?=({}))'.format(t))
    start_indices = (str(match.start() + 1) for match in pattern.finditer(s))
    return ' '.join(start_indices)

def test():
    test_string = '''\
GATATATGCATATACTT
ATAT'''
    result = get_substring_locations(test_string)
    print(result)
    assert result == '2 4 10'
    print('Test passed!')

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename) as file:
            print(get_substring_locations(file.read()))
    else:
        test()

if __name__ == '__main__':
    main()