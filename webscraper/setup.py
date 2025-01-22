from setuptools import setup, find_packages

setup(
    name='webscraper',
    version='0.0.1',
    author='Shubhadeep Naskar',
    description='A Python web scraping application using Pandas =)',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4>=4.9.3',
        'requests>=2.25.1',
        'pandas>=1.2.4'
    ],
    entry_points={
        'console_scripts': [
            'webscraper=webscraper.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)