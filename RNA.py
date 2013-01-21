#!/usr/bin/env python

import sys

def get_RNA(input):
    return input.replace('T','U')

def test():
    test_string = 'GATGGAACTTGACTACGTAAATT'
    result = get_RNA(test_string)
    assert result == 'GAUGGAACUUGACUACGUAAAUU'
    print(result)
    print('Test passed!')

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename) as file:
            print(get_RNA(file.read()))
    else:
        test()

if __name__ == '__main__':
    main()