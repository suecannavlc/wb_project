import pytest
import timeit

from wb_project import find_minimum_permutations


class TestExpected:

    def test_even(self):
        """
        Checks an input with an even number of items
        """
        input = [1, 0, 0, 1, 1, 0, 0, 0]
        result = find_minimum_permutations(input)
        assert result == 3

    def test_odd(self):
        """
        Checks an input with an odd number of items
        """
        input = [1, 0, 0, 1, 1, 0, 0]
        result = find_minimum_permutations(input)
        assert result == 3

    def test_null_length(self):
        """
        Checks an empty input
        """
        input = []
        with pytest.raises(TypeError) as excinfo:
            find_minimum_permutations(input)
        assert "Input must be a list containing only integers 0 and 1." \
               in str(excinfo.value)

    def test_exact_1(self):
        """
        Checks an input that is one of the exact patterns requiring no flips
        """
        input = [1, 0, 1, 0, 1, 0, 1, 0]
        result = find_minimum_permutations(input)
        assert result == 0

    def test_exact_2(self):
        """
        Checks an input that is one of the exact patterns requiring no flips
        """
        input = [0, 1, 0, 1, 0, 1, 0, 1, 0]
        result = find_minimum_permutations(input)
        assert result == 0


class TestNotExpected:

    def test_not_list(self):
        """
        Checks an input that is not a list
        """
        input = (1, 0)
        with pytest.raises(TypeError) as excinfo:
            find_minimum_permutations(input)
        assert "Input must be a list containing only integers 0 and 1." \
               in str(excinfo.value)

    def test_not_int(self):
        """
        Checks an input that does not contain ints
        """
        input = ['1', '0', '0', '1']
        with pytest.raises(TypeError) as excinfo:
            find_minimum_permutations(input)
        assert "Input must be a list containing only integers 0 and 1." \
               in str(excinfo.value)

    def test_not_zero_one(self):
        """
        Checks an input that contains other types
        """
        input = [2, 'a', 2, '1']
        with pytest.raises(TypeError) as excinfo:
            find_minimum_permutations(input)
        assert "Input must be a list containing only integers 0 and 1." \
               in str(excinfo.value)


class TestNonFunctional:

    def test_speed(self):
        """
        Checks that the result is correct for big numbers, and that
        performance is maintained
        """
        # Input length: 27122
        input = [int(x) for x in [*bin(123456789**1009)][2:]]
        result = find_minimum_permutations(input)
        # For big numbers, the result approaches input_length/2
        assert result == 13543
        result = timeit.timeit(f'find_minimum_permutations({input})',
                               number=1000,
                               setup='from wb_project import '
                                     'find_minimum_permutations')
        assert result < 4.0, "Execution performance has decreased"
