import pytest
import timeit

from wb_project import find_file


class TestExpectedLinux:
    """
    Tests mocking Linux behavior
    """

    def test_default(self, patch_function_linux):
        """
        Checks the default inputs
        """
        result = find_file('')
        assert result.name == 'f4', 'File found is not the expected'

    def test_owner(self, patch_function_linux):
        """
        Checks a non-default owner
        """
        result = find_file('', owner='aaa')
        assert result.name == 'f7', 'File found is not the expected'

    def test_type(self, patch_function_linux):
        """
        Checks a non-default type
        """
        result = find_file('',
                           type='writable')
        assert result.name == 'f5', 'File found is not the expected'

    def test_size(selfs, patch_function_linux):
        """
        Checks a non-default max size
        """
        result = find_file('',
                           max_size=int(2e6))
        assert result.name == 'f4', 'File found is not the expected'

    def test_all_parameters(self, patch_function_linux):
        """
        Checks non-default values for all parameters
        """
        result = find_file('',
                           max_size=int(2e6),
                           type='readable',
                           owner='aaa')
        assert result.name == 'f6', 'File found is not the expected'

    def test_input_not_found(self, patch_function_linux):
        """
        Checks the result when no file is matched
        """
        result = find_file('',
                           owner='bbb')
        assert result is None


class TestExpectedWindows:
    """
    Tests mocking Windows behavior
    """

    def test_owner(self, patch_function_windows):
        """
        Checks a non-default owner
        """
        result = find_file('', owner='aaa')
        assert result.name == 'f7', 'File found is not the expected'

    def test_all_parameters(self, patch_function_windows):
        """
        Checks non-default values for all parameters
        """
        result = find_file('',
                           max_size=int(2e6),
                           type='readable',
                           owner='aaa')
        assert result.name == 'f6', 'File found is not the expected'


class TestNotExpected:

    def test_input_path_not_str(self):
        """
        Checks an input that is not a string
        """
        with pytest.raises(TypeError) as excinfo:
            result = find_file(1)
        assert "expected str" \
               in str(excinfo.value)

    def test_input_owner_not_str(self):
        """
        Checks an input that is not a string
        """
        with pytest.raises(TypeError) as excinfo:
            result = find_file('',
                               owner=1)
        assert "Owner must be a string" \
               in str(excinfo.value)

    def test_input_type_not_defined(self):
        """
        Checks an input that is not defined
        """
        with pytest.raises(KeyError) as excinfo:
            result = find_file('',
                               type='other')
        assert "type must be one of: dict_keys(['executable', " \
               "'readable', 'writable'])" \
               in str(excinfo.value)

    def test_input_size_not_int(self):
        """
        Checks an input that is not an int
        """
        with pytest.raises(TypeError) as excinfo:
            result = find_file('',
                               max_size='other')
        assert "max_size must be an int" \
               in str(excinfo.value)


class TestNonFunctional:

    def test_speed(self, patch_function_linux):
        """
        Checks that the result is correct for several executions
        """

        result = timeit.timeit('find_file("", owner="aaa")',
                               number=1000,
                               setup='from wb_project import '
                                     'find_file')
        print(result)
        assert result < 0.05, "Execution performance has decreased"
