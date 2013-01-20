#!/usr/bin/env python

from collections import Counter
import sys

order = 'ACGT'

def get_ordered_counts(input):
    counts = Counter(input)
    return ' '.join(str(counts.get(letter, 0)) for letter in order)

def test():
    test_string = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
    result = get_ordered_counts(test_string)
    assert result == '20 12 17 21'
    print(result)
    print('Test passed!')

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename) as file:
            print(get_ordered_counts(file.read()))
    else:
        test()

if __name__ == '__main__':
    main()