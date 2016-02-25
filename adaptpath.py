
import sys
import os

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
    ''' find root importing package '''
    s = path
    for i in range(depth):
        s = os.path.dirname(s)
    package_path = os.path.abspath(s)
    return package_path



def adapt_from_path(depth=1, path=__file__, auto_reload_sys_path=True):
    """ normally you should set :param path to __file__ """
    package_path = get_package_path_from_path(depth, path)
    if package_path not in sys.path:
        sys.path.append(package_path)
    if auto_reload_sys_path:
            reload(sys)
    return package_path

