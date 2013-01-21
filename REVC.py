#!/usr/bin/env python

import sys
import string

def get_reverse_complement(input):
    return input.translate(string.maketrans('ATCG','TAGC'))[::-1]

def test():
    test_string = 'AAAACCCGGT'
    result = get_reverse_complement(test_string)
    assert result == 'ACCGGGTTTT'
    print(result)
    print('Test passed!')

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename) as file:
            print(get_reverse_complement(file.read()))
    else:
        test()

if __name__ == '__main__':
    main()