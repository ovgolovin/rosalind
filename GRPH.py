#!/usr/bin/env python
from __future__ import division

import sys
import re
from collections import Counter, namedtuple, defaultdict

x = 3 #suffix length from the task
ID_string_pair = namedtuple('ID_string_pair', ['ID', 'string'])

def generate_id_string_pairs_from_input(input):
    pattern = re.compile(r'>(?P<ID>Rosalind_\d{4})(?P<string>[^>]+)')
    for match in pattern.finditer(input):
        ID = match.group('ID').strip()
        string = match.group('string').strip().translate(None, '\n\r')
        yield ID_string_pair(ID, string)


def generate_overlapping_pairs(input):
    pairs = list(generate_id_string_pairs_from_input(input))
    beginnings = defaultdict(list)
    for pair in pairs:
        beginnings[pair.string[:x]].append(pair)
    for pair in pairs:
        ending = pair.string[-x:]
        if ending in beginnings:
            for latter_of_pair in beginnings[ending]:
                if pair is not latter_of_pair:
                    yield pair, latter_of_pair


def get_overlap_graphs_string(input):
    return '\n'.join(' '.join([a.ID, b.ID]) for a,b in generate_overlapping_pairs(input))


def test():
    test_string = '''\
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG'''
    result = get_overlap_graphs_string(test_string)
    print(result)
    assert result == '''\
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323'''
    print('Test passed!')

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename) as file:
            print(get_overlap_graphs_string(file.read()))
    else:
        test()

if __name__ == '__main__':
    main()