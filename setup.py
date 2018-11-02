from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='shambler',
    version='0.2',
    description="shambler is a pretty simple Python script, that creates a file with JSON's object format from a specified file.",  # Optional
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bruno-chavez/shambler',
    author='Bruno Chavez',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='json parser generator',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    entry_points={
        'console_scripts': [
            'shambler=shambler:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/bruno-chavez/shambler/issues',
        'Source': 'https://github.com/bruno-chavez/shambler',
    },
)
