import pytest
import timeit

from wb_project import find_repeated_number


class TestExpected:

    def test_repeated_number_beginning(self):
        """
        Checks an input with an even number of items
        """
        input1 = [10, 9, 7, 3, 1, 3, 6, 3]
        input2 = [10, 1, 2, 3, 4, 5, 6, 1]
        result = find_repeated_number(input1, input2)
        assert result == 10
        assert isinstance(result, int)

    def test_repeated_number_end(self):
        """
        Checks an input with an odd number of items
        """
        input1 = [1, 9, 7, 3, 1, 3, 7, 1]
        input2 = [10, 1, 2, 13, 4, 5, 6, 1]
        result = find_repeated_number(input1, input2)
        assert result == 1
        assert isinstance(result, int)

    def test_repeated_number_middle(self):
        """
        Checks an empty input
        """
        input1 = [1, 9, 2, 13, 1, 3, 7, 1]
        input2 = [10, 1, 2, 13, 4, 5, 6, 1]
        result = find_repeated_number(input1, input2)
        assert result == 2
        assert isinstance(result, int)

    def test_no_repeated_number(self):
        """
        Checks an input that is one of the exact patterns requiring no flips
        """
        input1 = [1, 9, 2, 3, 1, 3, 7, 1]
        input2 = [10, 1, 12, 13, 4, 5, 6, 9, 1]
        result = find_repeated_number(input1, input2)
        assert result is None

    def test_empty_list(self):
        """
        Checks an input that is one of the exact patterns requiring no flips
        """
        input1 = []
        input2 = [10, 1, 12, 13, 4, 5, 6, 11]
        result = find_repeated_number(input1, input2)
        assert result is None

    def test_two_empty_lists(self):
        """
        Checks an input that is one of the exact patterns requiring no flips
        """
        input1 = []
        input2 = []
        result = find_repeated_number(input1, input2)
        assert result is None


class TestNotExpected:

    def test_input_not_list(self):
        """
        Checks an input that is not a list
        """
        input1 = [0, 1, 2, 3, 4, 5]
        input2 = (1, 0, 2, 3, 4, 5)
        with pytest.raises(TypeError) as excinfo:
            find_repeated_number(input1, input2)
        assert "Input must be a list containing only integers" \
               in str(excinfo.value)

    def test_input_not_int(self):
        """
        Checks an input that does not contain ints
        """
        input1 = [0, 1, 2, 3, 4, 5]
        input2 = [1, 0, 'a', 3, 4, 5]
        with pytest.raises(ValueError) as excinfo:
            find_repeated_number(input1, input2)
        assert "invalid literal for int() with base 10: 'a'" \
               in str(excinfo.value)


class TestNonFunctional:

    def test_speed(self):
        """
        Checks that the result is correct for big numbers, and that
        performance is maintained
        """
        # Input length: 27122
        input1 = [1] * 1000000
        input2 = ['2'] * 1000000
        input2[:-1] = '1'
        result = find_repeated_number(input1, input2)
        # For big numbers, the result approaches input_length/2
        assert result == 1
        result = timeit.timeit(f'find_repeated_number({input1}, {input2})',
                               number=1000,
                               setup='from wb_project import '
                                     'find_repeated_number')
        assert result < 6.0, "Execution performance has decreased"
