# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="jsonpoint",
    version=":versiontools:jsonpoint:",
    description="",
    long_description="",
    author='Dougal Matthews',
    author_email='dougal85@gmail.com',
    setup_requires=[
    ],
    test_suite="runtests.runtests",
    tests_require=[
    ],
    packages=find_packages(exclude=('docs', )),
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'jsonpoint = jsonpoint.__main__:main',
        ]
    }
)
