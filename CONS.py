#!/usr/bin/env python


import sys
from itertools import izip
from collections import Counter


def get_input_column_iterator(input):
    lines = [line.strip() for line in input.strip().split('\n')]
    return izip(*lines)


def get_profile(columns):
    return [Counter(column) for column in columns]


def get_consensus(profile):
    return ''.join(column.most_common(1)[0][0] for column in profile)


def get_string_profile(profile):
    def get_el_counts(el):
        return '{}: {}'.format(el, ' '.join(str(column.get(el,0)) for column in profile))
    return '\n'.join(get_el_counts(el) for el in 'ACGT')


def form_output(input):
    columns = get_input_column_iterator(input)
    profile = get_profile(columns)
    string_profile = get_string_profile(profile)
    consensus = get_consensus(profile)
    return '\n'.join([consensus, string_profile])

def test():
    test_string = '''\
ATCCAGCT
GGGCAACT
ATGGATCT
AAGCAACC
TTGGAACT
ATGCCATT
ATGGCACT'''
    result = form_output(test_string)
    print(result)
    assert result == '''\
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6'''
    print('Test passed!')

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename) as file:
            print(form_output(file.read()))
    else:
        test()

if __name__ == '__main__':
    main()