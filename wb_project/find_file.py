import os
import re
import platform

from pathlib import Path


def find_file(input_path: str,
              owner: str = 'admin',
              type: str = 'executable',
              max_size: int = 14680064):

    """
    A function that given a path of the file system finds the first file
    that meets the requirements passed as parameters.

    :param input_path: (str) path to the file system
    :param owner: (str) owner name. 'admin' by default
    :param type: (str) permissions. Can be 'executable', 'readable' or
    'writable'. 'executable' by default.
    :param max_size: (int) max file size in bytes. 14680064 by default.
    :return: file name or None if not found
    """
    type_map = {
        'executable': os.X_OK,
        'readable': os.R_OK,
        'writable': os.W_OK
    }

    if not isinstance(owner, str):
        raise TypeError("Owner must be a string")

    if type not in type_map:
        raise KeyError(f"type must be one of: {type_map.keys()}")

    if not isinstance(max_size, int):
        raise TypeError('max_size must be an int')

    path = Path(input_path)

    for f in path.glob('**/*'):
        if f.is_file() and \
                os.access(f, type_map[type]) and \
                _get_owner(f) == owner and \
                f.stat().st_size < max_size:
            return f


def _windows_get_info(file):
    """
    Get Windows file information.

    :param file: file name
    :return: windows file info
    """
    with os.popen(f'cmd /c "dir /q {file}"') as cmd:
        return cmd.read()


def _get_owner(file):
    """
    Returns the owner, depending on the OS
    :param file: File object
    :return:
    """
    if platform.system() == 'Windows':
        w_i = _windows_get_info(file)
        m = re.search(r'(\d{2}/\d{2}/\d{4})\s+(\d{2}:\d{2})\s+(\S+)\s+('
                      r'\S+\\)(\w+).+', w_i)
        return m.group(5)
    # Assuming the OS lib will work with other OS systems
    else:
        return file.owner()
