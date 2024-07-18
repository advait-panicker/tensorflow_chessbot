# setup.py
from setuptools import setup, find_packages

setup(
    name='tensorflow_chessbot',  # Replace with your project name
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4>=4.6.3,<5',
        'lxml>=4.2.4,<5',
        'Pillow>=5.2.0,<6',
        'tensorflow>=2,<3',
        'requests>=2.21.0,<3',
    ],
)