from setuptools import find_packages
from setuptools import setup


setup(
    name='pythonpackages',
    entry_points={
        'paste.app_factory': 'main=pythonpackages:main',
    },
    install_requires=[
        'pyramid',
        'pyramid_redis_sessions==1.0a1',
        'pyramid_mako',
        'redis',
        'requests',
    ],
    packages=find_packages(),
    test_suite = 'pythonpackages.tests.TestPythonPackages',
)
