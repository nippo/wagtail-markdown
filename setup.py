#! /usr/bin/env/python
# vim:sw=4 ts=4 et:
#
# Copyright (c) 2015 Torchbox Ltd.
# felicity@torchbox.com 2015-09-14
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely. This software is provided 'as-is', without any express or implied
# warranty.
#

from setuptools import setup, find_packages

setup(
    name='wagtail-markdown',
    version='0.5.0',
    description='Markdown support for Wagtail',
    long_description="Provides Markdown page field and streamfield block for Wagtail.  More info: "
                     "https://github.com/andrivet/wagtail-markdown/blob/master/README.md",
    author='Felicity Tarnell',
    author_email='felicity@torchbox.com',
    url='https://github.com/andrivet/wagtail-markdown',

    install_requires=[
        'Markdown==2.6.7',
        'bleach==1.5.0', 'django',
    ],
    license='zlib license',

    packages=find_packages(),

    include_package_data=True,
    package_data={
        'wagtailmarkdown': ['static/wagtailmarkdown/*/*'],
    },

    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'License :: OSI Approved :: zlib/libpng License',
    ],
)
