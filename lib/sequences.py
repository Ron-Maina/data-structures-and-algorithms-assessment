#!/usr/bin/env python3
import ipdb;

def remove_duplicates(sequence):
    if type(sequence) == list:
        return list(set(sequence))
    else:
        return tuple(set(sequence))


# remove_duplicates()