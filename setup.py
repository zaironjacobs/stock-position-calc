from setuptools import setup
from setuptools import find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

version = '1.0.5'

requires = []

setup(
    name='stock-position-calc',
    version=version,
    author='Zairon Jacobs',
    author_email='zaironjacobs@gmail.com',
    description='A simple program to calculate the right amount of shares to buy while limiting risk.',
    long_description=long_description,
    url='https://github.com/zaironjacobs/stock-position-calc',
    download_url='https://github.com/zaironjacobs/stock-position-calc/archive/v' + version + '.tar.gz',
    keywords=['stock', 'market', 'price', 'calculation', 'investment', 'tool'],
    packages=find_packages(),
    entry_points={
        'console_scripts': ['stock-position-calc' + '=stock_position_calc.app:main'],
    },
    install_requires=requires,
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Natural Language :: English'
    ],
    python_requires='>=3.8',
)
