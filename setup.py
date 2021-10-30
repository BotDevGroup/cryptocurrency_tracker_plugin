#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'marvinbot'
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='cryptocurrency_tracker_plugin',
    version='0.1.0',
    description="A plugin for marvinbot to track the exchange rate data of cryptocurrencies",
    long_description=readme,
    author="Ricardo Arturo Cabral Mejia",
    author_email='me@ricardocabral.io',
    url='https://github.com/Cameri/cryptocurrency_tracker_plugin',
    packages=[
        'cryptocurrency_tracker_plugin',
    ],
    package_dir={'cryptocurrency_tracker_plugin':
                 'cryptocurrency_tracker_plugin'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='cryptocurrency_tracker_plugin',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    dependency_links=[
        'git+ssh://git@github.com:BotDevGroup/marvin.git#egg=marvinbot',
    ],
)
