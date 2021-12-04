def count_it(sequence):
    return dict([int(num) for num in sequence].most_common(3))
