# ** -- coding: utf-8 -- **
# !/usr/bin/env python
#
# Copyright (c) 2011 darkdarkfruit <darkdarkfruit@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

'''
test
==========
You should have py.test installed first.
pip install -U pytest

Then, run
>> py.test test_*


'''
import sys
import os
from pprint import pprint
import unittest
from unittest import TestCase

abs_path = os.path.abspath(__file__)
# print('abs_path is: %s' % abs_path)
TEST_PATH = os.path.split(abs_path)[0]
PACKAGE_PATH = os.path.split(TEST_PATH)[0]
# PACKAGE_PATH = os.path.split(PACKAGE_PATH)[0]
# print('package path is: %s' % PACKAGE_PATH)
if PACKAGE_PATH not in sys.path:
    sys.path.insert(0, PACKAGE_PATH)
# pprint(sys.path)
import adaptpath
# pprint('1: %s' % adaptpath)

from adaptpath import adaptpath


# pprint('2: %s' % adaptpath)

def test_adaptpath():
    assert True


class TestAdaptPath(TestCase):
    def test_get_package_path_from_path(self):
        path = __file__
        expected_path = os.path.dirname(os.path.dirname(os.path.abspath(path)))
        package_path = adaptpath.get_package_path_from_path(1, path)
        print('expected_path is: %s' % expected_path)
        print('package_path is: %s' % package_path)
        self.assertTrue(expected_path == package_path)

    def test_get_package_path_from_path_without___file__(self):
        path = __file__
        expected_path = os.path.dirname(os.path.dirname(os.path.abspath(path)))
        package_path = adaptpath.get_package_path_from_path(1)
        print('expected_path is: %s' % expected_path)
        print('package_path is: %s' % package_path)
        self.assertTrue(expected_path == package_path)


if __name__ == '__main__':
    # print(adaptpath)
    unittest.main()
