# coding: utf-8
'''# Say we have dir-tree below:
    a / b / c.py
    x / y / z.py

# Now in "z.py", if we want to do this:
    from a.b import c

# We can put the lines below ahead of "z.py"
    from adaptpath import adaptpath
    adaptpath.adapt_from_path(2, __file__)

#
'''
import sys
import os

if sys.version_info[0] == 3:
    import importlib

    reload = importlib.reload


def get_package_path(depth=1):
    ''' find root importing package '''
    s = ''
    for i in range(depth):
        s += '../'
    package_path = os.path.abspath(s)
    return package_path


def adapt(depth=1, auto_reload_sys_path=True):
    if isinstance(depth, str):
        depth = depth.count('..')
    package_path = get_package_path(depth)
    if package_path not in sys.path:
        sys.path.append(package_path)
    if auto_reload_sys_path:
        reload(sys)
    return package_path


def get_package_path_from_path(depth=1, path=__file__):
    ''' find root importing package

     # Say we have dir-tree below:
        a/b/c.py
        x/y/z.py

     # Now in "z.py", if we want to do this:
        from a.b import c

     # We can put the lines below ahead of "z.py"
        from adaptpath import adaptpath
        adaptpath.adapt_from_path(2, __file__)

     #
     '''
    try:
        abs_path = os.path.abspath(path)
        cur_dir = os.path.dirname(abs_path)
    except Exception as e:
        print('Error: Could not get abspath of path: "%s"' % path)
        return None
    s = cur_dir
    while depth > 0:
        s = os.path.dirname(s)
        depth -= 1
    return s


def adapt_from_path(depth=1, path=__file__, auto_reload_sys_path=True):
    """ normally you should set :param path to __file__ """
    package_path = get_package_path_from_path(depth, path)
    if package_path not in sys.path:
        sys.path.append(package_path)
    if auto_reload_sys_path:
        reload(sys)
    return package_path
