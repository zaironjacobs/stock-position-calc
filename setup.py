from setuptools import setup
from setuptools import find_packages
from app_info import __app_name__
from app_info import __app_version__

with open('README.md', 'r') as fh:
    long_description = fh.read()

requires = []

setup(
    name=__app_name__,
    version=__app_version__,
    author='Zairon Jacobs',
    author_email='zaironjacobs@gmail.com',
    description='A simple program to calculate the right amount of shares to buy while limiting risk.',
    long_description=long_description,
    url='https://github.com/zaironjacobs/stock-position-calc',
    download_url='https://github.com/zaironjacobs/stock-position-calc/archive/v' + __app_version__ + '.tar.gz',
    keywords=['stock', 'market', 'price', 'calculation', 'investment', 'tool'],
    packages=find_packages(),
    entry_points={
        'console_scripts': [__app_name__ + '=stock_position_calc.app:main'],
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
