def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..
    
        >>> two_oldest_ages([1, 2, 10, 8])
        (10, 8)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (10, 9)

    Even if more than one person has the same oldest age, this should return 
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (5, 2)
    """

    sorted_int = set(ages)

    largest_int = sorted(sorted_int, reverse=True)[0]
    second_largest = sorted(sorted_int, reverse=True)[1]

    return largest_int, second_largest