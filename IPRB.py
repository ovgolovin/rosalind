#!/usr/bin/env python
from __future__ import division

from collections import Counter
import sys


def get_probability(input):
    k,m,n = map(int, input.strip().split())
    N = k + m + n

    #Let's first pick BB.
    p1 = k / N
    p_total = p1 #with any second pick the outcome will be with dominant with conditional probability 1

    #Let's first pick be Bb
    p1 = m / N
    p2 = (1*k + 0.75*(m-1) + 0.5*(n)) / (N-1) #Second pick BB gives probability 1, Bb - 0.75, bb - 0.5
    p_total += p1 * p2

    #Let's first pick be bb
    p1 = n / N
    p2 = (1*k + 0.5*m) / (N-1) #Second pick BB gives probability 1, Bb - 0.5, bb - 0/
    p_total += p1 * p2

    return p_total

def test():
    test_string = '2 2 2'
    result = get_probability(test_string)
    print(result)
    assert str(result)[:7] == '0.78333'
    print('Test passed!')

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename) as file:
            print(get_probability(file.read()))
    else:
        test()

if __name__ == '__main__':
    main()