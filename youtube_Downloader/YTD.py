#!/usr/bin/env python3

from mainInterface import YTD
import sys
from PyQt5.QtWidgets import QApplication
import importlib.util

"""
spec = importlib.util.spec_from_file_location("module.name", "/path/to/file.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)
foo.MyClass()
"""


if __name__ == '__main__':

    app = QApplication(sys.argv)
    obj = YTD()
    obj.show()
    sys.exit(app.exec_())