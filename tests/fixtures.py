import re
import pytest
import os
import platform

from pathlib import Path


@pytest.fixture()
def patch_function_linux(monkeypatch):
    monkeypatch.setattr(Path, "glob", create_files_linux)
    monkeypatch.setattr(os, "access", my_access)
    monkeypatch.setattr(platform, "system", base_os_linux)


@pytest.fixture()
def patch_function_windows(monkeypatch):
    monkeypatch.setattr(Path, "glob", create_files_windows)
    monkeypatch.setattr(os, "access", my_access)
    monkeypatch.setattr(os, "popen",
                        my_windows_get_info)
    monkeypatch.setattr(platform, "system", base_os_windows)


def my_access(file, t):
    if file.exec == t:
        return True


class CmdOutput:
    def __init__(self, w_i):
        self.windows_info = w_i

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def read(self):
        return self.windows_info


def my_windows_get_info(file):
    m = re.match(r'.*/q (.*)', file).group(1)
    return CmdOutput(m)


def base_os_linux():
    return "Linux"


def base_os_windows():
    return "Windows"


def create_files_linux(*args):
    return create_file_helper(base_os='Linux')


def create_files_windows(*args):
    return create_file_helper(base_os='Windows')


class Stats:
    def __init__(self, size):
        self.st_size = size


class MyFile:
    type_map = {
        'executable': os.X_OK,
        'readable': os.R_OK,
        'writable': os.W_OK
    }

    def __init__(self, name, file, exec, owner, size, os, windows_info):
        self.name = name
        self.file = file
        self.exec = exec
        self._owner = owner
        self.size = size
        self.os = os
        self.windows_info = windows_info

    def __repr__(self):
        return self.windows_info

    def is_file(self):
        return self.file

    def owner(self):
        if self.os == 'Windows':
            raise NotImplemented
        else:
            return self._owner

    def stat(self):
        return Stats(self.size)


def create_file_helper(base_os):
    output = []
    # Non files
    output.append(MyFile(name='f0', file=False, exec=os.R_OK, owner='aaa',
                         size=10, os=base_os,
                         windows_info=r"21/09/2022  21:42                 10 "
                                      "admin-PC\\aaa           f0"))
    output.append(MyFile(name='f1', file=False, exec=os.X_OK, owner='aaa',
                         size=10, os=base_os,
                         windows_info=r"22/09/2022  21:42                 10 "
                                      "admin-PC\\aaa           f1"
                         ))
    output.append(MyFile(name='f2', file=False, exec=os.W_OK, owner='admin',
                         size=10, os=base_os,
                         windows_info=r"23/09/2022  21:42                 10 "
                                      "admin-PC\\admin           f2"
                         ))
    output.append(MyFile(name='f3', file=False, exec=os.R_OK, owner='aaa',
                         size=int(15e6), os=base_os,
                         windows_info=r"24/09/2022  21:42                 "
                                      "15.000.000 "
                                      "admin-PC\\aaa           f3"
                         ))

    # Files
    output.append(MyFile(name='f4', file=True, exec=os.X_OK, owner='admin',
                         size=1000, os=base_os,
                         windows_info=r"25/09/2022  21:42                 1000 "
                                      "admin-PC\\admin           f4"))
    output.append(MyFile(name='f5', file=True, exec=os.W_OK, owner='admin',
                         size=10, os=base_os,
                         windows_info=r"26/09/2022  21:42                 10 "
                                      "admin-PC\\admin           f5"
                         ))
    output.append(MyFile(name='f6', file=True, exec=os.R_OK, owner='aaa',
                         size=int(1e6), os=base_os,
                         windows_info=r"27/09/2022  21:42               "
                                      "1.000.000 "
                                      "admin-PC\\aaa           f6"
                         ))
    output.append(MyFile(name='f7', file=True, exec=os.X_OK, owner='aaa',
                         size=10, os=base_os,
                         windows_info=r"28/09/2022  21:42               "
                                      "10 "
                                      "admin-PC\\aaa           f7"
                         ))
    output.append(MyFile(name='f8', file=True, exec=os.X_OK, owner='admin',
                         size=10, os=base_os,
                         windows_info=r"29/09/2022  21:42               "
                                      "10 "
                                      "admin-PC\\admin           f8"
                         ))
    output.append(MyFile(name='f9', file=True, exec=os.X_OK, owner='admin',
                         size=13e6, os=base_os,
                         windows_info=r"30/09/2022  21:42               "
                                      "13.000.000 "
                                      "admin-PC\\admin           f9"
                         ))
    output.append(MyFile(name='f10', file=True, exec=os.X_OK, owner='admin',
                         size=int(15e6), os=base_os,
                         windows_info=r"30/09/2022  21:42               "
                                      "15.000.000 "
                                      "admin-PC\\admin           f10"
                         ))

    return output
