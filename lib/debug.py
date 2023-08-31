#!/usr/bin/env python3
import ipdb;
from sequences import remove_duplicates
from dictionaries import word_frequency
from stacks import is_balanced

if __name__ == '__main__':
    # Example tests
    ## Sequences (Lists/Tuples)
    remove_duplicates([2, 3, 2, 4, 5, 3, 6, 7, 5])
    remove_duplicates((2, 3, 2, 4, 5, 3, 6, 7, 5))

    ## Stacks
    is_balanced("([]{})")
    is_balanced("([)]")
    is_balanced("{[]()}")
    is_balanced("{[](]}")



    word_frequency("This is a test sentence. This sentence is a test.")

    ipdb.set_trace()