from setuptools import setup, find_packages, Command
import os

from adaptpath.version import __version__

DESCRIPTION = "convinent script to adapt python's sys.path"

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.md').read()
except:
    pass


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet',
    'Topic :: Software Development :: Libraries :: Python Modules',
]




# https://pytest.org/latest/goodpractises.html
setup(name='adaptpath',
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
)
