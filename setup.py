#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="fypbjchina",
    author_email='fypbjchina@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="R03M1",
    entry_points={
        'console_scripts': [
            'a_pythoncrashcourse_cn=a_pythoncrashcourse_cn.cli:main',
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='a_pythoncrashcourse_cn',
    name='a_pythoncrashcourse_cn',
    packages=find_packages(include=['a_pythoncrashcourse_cn', 'a_pythoncrashcourse_cn.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/fypbjchina/a_pythoncrashcourse_cn',
    version='0.1.0',
    zip_safe=False,
)
