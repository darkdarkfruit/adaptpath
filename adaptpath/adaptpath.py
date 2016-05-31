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
import traceback

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
    elif isinstance(depth, int):
        package_path = get_package_path_from_path(depth)
    else:
        package_path = get_package_path(depth)
    if package_path not in sys.path:
        sys.path.append(package_path)
    if auto_reload_sys_path:
        reload(sys)
    return package_path


def get_package_path_from_path(depth=1, path=None):
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
    if not path:
        path = get___file__()

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


def get___file__():
    # infos = traceback.format_stack()
    # for i in infos:
    #     print(i)

    # traceback.extract_tb(traceback[, limit])
    # Return a list of up to limit “pre-processed” stack trace entries extracted from the traceback object traceback.
    # It is useful for alternate formatting of stack traces. If limit is omitted or None, all entries are extracted.
    # A “pre-processed” stack trace entry is a 4-tuple (filename, line number, function name, text) representing the information that is usually printed for a stack trace.
    # The text is a string with leading and trailing whitespace stripped; if the source is not available it is None.
    #

    # stacks = traceback.extract_stack(limit=2)
    stacks = traceback.extract_stack()
    files = [stack[0] for stack in stacks]
    files_ = []
    for f in files:
        # todo: find a better way to get right caller path.
        # note: some platform(eg: some centos) will only give a file name, not file path!
        # 'adaptpath.py' match -> this is just a rough solution.
        f2 = f
        if '/' in f:
            f2 = f.split('/')[-1]
        elif '\\' in f:
            f2 = f.split('\\')[-1] # windows: E:/config/config.py
        else:
            pass
        if f2 == 'adaptpath.py':
            break
        files_.append(f)
    fpath =  files_[-1]
    if os.path.isabs(fpath):
        return fpath
    else:
        try:
            return os.path.abspath(fpath)
        except Exception as e:
            return fpath


def adapt_from_path(depth=1, path=None, auto_reload_sys_path=True):
    """ normally you should set :param path to __file__ """
    if not path:
        path = get___file__()
    package_path = get_package_path_from_path(depth, path)
    if package_path not in sys.path:
        sys.path.append(package_path)
    if auto_reload_sys_path:
        reload(sys)
    return package_path


if __name__ == '__main__':
    package_path = adapt(0)
    print('package_path is: %s' % package_path)
    package_path = adapt(1)
    print('package_path is: %s' % package_path)
    package_path = adapt(2)
    print('package_path is: %s' % package_path)
