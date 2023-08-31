def remove_duplicates(sequence):
    if type(sequence) == list:
        return list(set(sequence))
    else:
        return tuple(set(sequence))

