from setuptools import find_packages
from setuptools import setup
import os


# The version of the wrapped library is the starting point for the
# version number of the python package.
# In bugfix releases of the python package, add a '-' suffix and an
# incrementing integer.
# For example, a packaging bugfix release version 1.4.4 of the
# js.jquery package would be version 1.4.4-1 .

version = '1.68.dev0'


def read(*rnames):
    """Read file content."""
    with open(os.path.join(os.path.dirname(__file__), *rnames))as f:
        return f.read()


long_description = (
    read('README.rst')
    + '\n' +
    read('js', 'jquery_tinyscrollbar', 'test_jquery_tinyscrollbar.rst')
    + '\n' +
    read('CHANGES.rst'))

setup(
    name='js.jquery_tinyscrollbar',
    version=version,
    description="Fanstatic packaging of jQuery Tiny Scrollbar",
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords='',
    author='gocept Developers',
    author_email='mail@gocept.com',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    url='https://github.com/gocept/js.jquery_tinyscrollbar',
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'setuptools',
        'js.jquery'
    ],
    entry_points={
        'fanstatic.libraries': [
            'jquery_tinyscrollbar = js.jquery_tinyscrollbar:library',
        ],
    },
)
