from builtins import isinstance
from typing import Optional

Vector = list[int]


def find_repeated_number(list1: Vector, list2: Vector) -> Optional[int]:
    """
    Finds the first repeated integer in the two lists passed as parameter.

    The function checks for matches for the size of the smallest list.

    :param list1: List of integers, any size
    :param list2: List of integers, any size
    :return: First repeated number, or None if no repetition
    :raises TypeError if inputs are not lists
    :raises ValueError if input lists do not contain integers or values
            convertible to integers
    """

    result = None

    if not isinstance(list1, list):
        raise TypeError('Input must be a list containing only integers.')

    if not isinstance(list2, list):
        raise TypeError('Input must be a list containing only integers.')

    for i1, i2 in zip(list1, list2):
        # Raises a TypeError if the input is not convertible to integers
        if int(i1) == int(i2):
            result = int(i1)
            break

    return result
