#!/usr/bin/env python
# coding: utf-8
#

""" module docstring: module description title

module description details.
"""


# -------------- import starts -------------------------
# import standard libs here. (eg: import sys)

# import 3rd libs here

# import app modules here

# -------------- import ends ---------------------------


# put vars you want to export here
# __all__ = []


# -------------- globals starts ------------------------
# put global constants here

# put global vars here
# -------------- global ends ---------------------------


# bellow is the main module body
# ======================================================
MAIN = 0
MINOR = 3
MICRO = 1
commit_hash = ''
# commit_hash = 'dac4a317976354339ea66942477'
if commit_hash:
    MAIN = commit_hash
    MINOR = MICRO = ''

version_tuple = (MAIN, MINOR, MICRO)
VERSION = version = __version__ = '.'.join([str(i) for i in version_tuple]).strip('.')


def get_version_tuple():
    return version_tuple

def get_version():
    return version

if __name__ == '__main__':
    print(version_tuple)
    print(get_version_tuple())
    print(version)
    print(get_version())


