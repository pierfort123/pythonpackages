from setuptools import find_packages
from setuptools import setup


setup(
    name='pythonpackages',
    packages=find_packages(),
    entry_points={
        'paste.app_factory': 'main=pythonpackages:main',
    },
    test_suite = 'pythonpackages.tests.TestSuite',
)
