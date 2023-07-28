from setuptools import setup

setup(
    name = 'rescan',

    version = '1.0.0',

    description = 'A modern port scanner for recon written in python',

    py_modules = ["rescan"],

    package_dir = {'':'src'},

    author = 'SnowKluster',

    long_description = open('README.md').read(),
    long_description_content_type = "text/markdown",

    url='https://github.com/snowkluster/rescan',

    include_package_data=True,

    classifiers  = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        'Intended Audience :: Developers',
        'Topic :: Port Scanner',
        'Operating System :: OS Independent',
    ],

    install_requires = [

        'rich~=13.4.2',
        'typer~=0.9.0'
    ],

    keywords = ['Port Scanner', 'Modern'],
)