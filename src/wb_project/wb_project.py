from typing import Optional



Vector = list[int]


def find_repeated_number(list1: Vector, list2: Vector) -> Optional[int]:
    """
    Assumption: no cycling over the smallest list

    :param list1:
    :param list2:
    :return:
    """
    result = None

    for i1, i2 in zip(list1, list2):
        if int(i1) == int(i2):
            result = int(i1)
            break

    return result


def find_minimum_permutations(list1: Vector) -> Optional[int]:
    """

    :param list1:
    :return:
    """
    result = None

    if not all([item in [0, 1] for item in list1]):
        raise TypeError('Input must be a list containing only integers'
                        '0 and 1.')

    # Output will be of the type: 01010101 or 10101010
    # If I know the length of the input, I know that the flipped solution
    # will be one of two.
