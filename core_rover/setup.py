import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test

def get_requirements(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path) as f:
        file_contents = f.read().strip('\n')
    return strip_requirements_comments(file_contents)

def strip_requirements_comments(contents):
    return [line.split()[0] for line in contents.split('\n')
            if line != '' and not line.startswith('#')]

class Tests(test):

    def finalize_options(self):
        test.finalize_options(self)
        self.test_args = ['server/tests']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    name = "Project Phoenix",
    version = "0.1",
    install_requires = get_requirements('requirements.txt'),
    packages = find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]
    ),
    cmdclass={'test': Tests},
)