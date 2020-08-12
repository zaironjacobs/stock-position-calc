Stock Position Calculator
=================
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/stock-position-calc?color=blue)](https://pypi.python.org/pypi/stock-position-calc)
[![PyPI](https://img.shields.io/pypi/v/stock-position-calc?color=blue)](https://pypi.python.org/pypi/stock-position-calc)
[![PyPI - Status](https://img.shields.io/pypi/status/stock-position-calc)](https://pypi.python.org/pypi/stock-position-calc)
[![PyPI - License](https://img.shields.io/pypi/l/stock-position-calc)](https://pypi.python.org/pypi/stock-position-calc)

A simple program to manage risk and calculate the right amount of shares to buy.

Install with pip
-----

To install:
```bash
$ pip install stock-position-calc
```

For some Linux distributions you will need to install the tkinter package:
```bash
$ sudo apt update
$ sudo apt install python3-tk
```

Launch tool:
```bash
$ stock-position-calc
```

Create an executable to run the program:
-----

Windows:
```bash
$ git clone https://github.com/zaijacobs/stock-position-calc.git
$ cd stock-position-calc
$ pipenv install
$ pipenv run pyinstaller stock_position_calc/app.py --onefile --windowed
```

Linux:
```bash
$ git clone https://github.com/zaijacobs/stock-position-calc.git
$ cd stock-position-calc
$ pipenv install
$ pipenv run pyinstaller stock_position_calc/app.py --onefile --windowed
$ sudo chmod +x dist/app
```

Check for the executable in the created dist directory.

------

#### Fixed Cash Amount: 
Will calculate the number of shares solely based on the amount you want to invest in a trade.
Example: You have $10,000 to invest in a stock and you would like to buy shares of that stock when the price falls down to $20.
The amount of shares you will buy will be 500 ($10,000 / $20).

#### Fixed Risk:
Will calculate the number of shares based on how much you are willing to risk.
Example: You have an account size of $10,000 and you would like to buy shares of a stock when the price falls down to $20.
You decide on a stop loss of 15% ($17) and you want to risk only 1% ($100) of your account size.
The amount of shares you will buy will be 33 ($100 / ($20 - $17)).

\
<img src="https://i.imgur.com/ZxZ0UOu.png" width="450">