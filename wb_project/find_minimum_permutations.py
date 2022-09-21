Vector = list[int]


def find_minimum_permutations(list1: Vector) -> int:
    """
    Finds the minimum number of permutations needed to convert
    the input in an alternate list of 1 and 0.

    :param list1: List of integers, containing only 0 or 1 in any order
    :return: (int) Minimum number of flips
    :raises TypeError: If input is not as expected
    """
    # Checks to determine that input is as expected
    if not list1:
        raise TypeError('Input must be a list containing only integers'
                        ' 0 and 1.')

    if not isinstance(list1, list):
        raise TypeError('Input must be a list containing only integers'
                        ' 0 and 1.')

    if not all([item in [0, 1] for item in list1]):
        raise TypeError('Input must be a list containing only integers'
                        ' 0 and 1.')

    # The problem consists of checking the flips needed to convert the input
    # into one of these patterns:
    #   0, 1, 0, 1, ...
    #   1, 0, 1, 0, ...
    # The flips needed to convert the input to the first pattern are exactly
    # complementary to the flips needed to convert to the second. Thus, it is
    # enough to check the flips needed to convert to the first pattern, and
    # calculate the flips needed to convert to the second pattern as a
    # subtraction.

    input_length = len(list1)
    flips = 0

    #
    for i in range(0, input_length, 2):

        # If there is a 1 on the even positions, we need a flip to convert
        # to the first pattern
        if list1[i] == 1:
            flips += 1

    for i in range(1, input_length, 2):

        # If there is 0 on the odd positions, we need a flip to convert
        # to the first pattern
        if list1[i] == 0:
            flips += 1

    return min(flips, input_length - flips)
