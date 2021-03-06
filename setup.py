from setuptools import setup, find_packages, Command
from adaptpath import __version__

DESCRIPTION = "convinent script to adapt python's sys.path"

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.md').read()
except:
    pass

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries',
    'Topic :: Utilities',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

# https://pytest.org/latest/goodpractises.html
setup_params_dict = dict(name='adaptpath',
                         version=__version__,
                         packages=find_packages(),
                         author='darkdarkfruit',
                         author_email='darkdarkfruit@{nospam}gmail.com',
                         url='https://github.com/darkdarkfruit/adaptpath',
                         license='MIT',
                         include_package_data=True,
                         description=DESCRIPTION,
                         long_description=LONG_DESCRIPTION,
                         platforms=['any'],
                         setup_requires=['pytest-runner'],
                         tests_require=['pytest'],
                         classifiers=CLASSIFIERS,
                         keywords='adaptpath adaptedpath adapt-path adapt path')
setup(**setup_params_dict)
