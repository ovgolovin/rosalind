#!/usr/bin/env python
from __future__ import division

import sys
import re
from collections import Counter, namedtuple

def get_gc_content(string):
    counter = Counter(string)
    return sum(counter.get(letter, 0) for letter in 'GC') / sum(counter.values())

ID_string_pair = namedtuple('ID_string_pair', ['ID', 'string'])

def generate_id_string_pairs_from_input(input):
    pattern = re.compile(r'>(?P<ID>Rosalind_\d{4})(?P<string>[^>]+)')
    for match in pattern.finditer(input):
        ID = match.group('ID').strip()
        string = match.group('string').strip().translate(None, '\n\r')
        yield ID_string_pair(ID, string)


def get_string_id_pair_with_max_gc_content(input):
    return max(generate_id_string_pairs_from_input(input), key=lambda x: get_gc_content(x.string))


def get_string_ID_with_the_max_gc_content_formatted(input):
    pair = get_string_id_pair_with_max_gc_content(input)
    return '{0}\n{1:%}'.format(pair.ID, get_gc_content(pair.string))


def test():
    test_string = '''\
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT'''
    result = get_string_ID_with_the_max_gc_content_formatted(test_string)
    print(result)
    assert result == '''\
Rosalind_0808
60.919540%'''
    print('Test passed!')

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename) as file:
            print(get_string_ID_with_the_max_gc_content_formatted(file.read()))
    else:
        test()

if __name__ == '__main__':
    main()