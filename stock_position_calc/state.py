from tkinter import messagebox
from abc import ABC, abstractmethod

from stock_position_calc import validate
from stock_position_calc import currency_formatter


class State(ABC):

    def __init__(self):
        self.__context = None

    @property
    def context(self):
        return self.__context

    @context.setter
    def context(self, context):
        self.__context = context

    @abstractmethod
    def calculate(self, funds, entry_price, risk, trailing_stop, stop_price):
        pass


class StateA(State):
    """
    Strategy: Fixed Dollar
    Stop type: Trailing stop
    """

    def calculate(self, funds, entry_price, risk, trailing_stop, stop_price):
        results_stringvars_dict = self.context.get_results_stringvars_dict()
        current_currency = self.context.get_current_currency()
        currency_symbol = self.context.get_current_currency_symbol()

        validate_result = validate.validate_state_a_values(funds, entry_price, trailing_stop)
        if validate_result.get('status') == 'error':
            error_message = validate_result.get('error_message')
            messagebox.showerror('Error', error_message)
            return

        shares = int(float(funds) / float(entry_price))
        results_stringvars_dict.get('shares').set(str(shares))
        position_value = float(shares) * float(entry_price)
        results_stringvars_dict.get('position_value').set(
            currency_symbol + currency_formatter.float_to_currency(position_value, current_currency))
        equity_at_risk = '-'
        results_stringvars_dict.get('equity_at_risk').set(equity_at_risk)
        stop_price = float(entry_price) * ((100 - float(trailing_stop)) / 100)
        results_stringvars_dict.get('stop_price').set(
            currency_symbol + currency_formatter.float_to_currency(stop_price, current_currency))


class StateB(State):
    """
    Strategy: Fixed Dollar
    Stop type: Stop price
    """

    def calculate(self, funds, entry_price, risk, trailing_stop, stop_price):
        results_stringvars_dict = self.context.get_results_stringvars_dict()
        current_currency = self.context.get_current_currency()
        currency_symbol = self.context.get_current_currency_symbol()

        validate_result = validate.validate_state_b_values(funds, entry_price, stop_price)
        if validate_result.get('status') == 'error':
            error_message = validate_result.get('error_message')
            messagebox.showerror('Error', error_message)
            return

        shares = int(float(funds) / float(entry_price))
        results_stringvars_dict.get('shares').set(str(shares))
        position_value = float(shares) * float(entry_price)
        results_stringvars_dict.get('position_value').set(
            currency_symbol + currency_formatter.float_to_currency(position_value, current_currency))
        equity_at_risk = '-'
        results_stringvars_dict.get('equity_at_risk').set(equity_at_risk)
        results_stringvars_dict.get('stop_price').set(
            currency_symbol + currency_formatter.float_to_currency(float(stop_price), current_currency))


class StateC(State):
    """
    Strategy: Fixed Risk
    Stop type: Trailing stop
    """

    def calculate(self, funds, entry_price, risk, trailing_stop, stop_price):
        results_stringvars_dict = self.context.get_results_stringvars_dict()
        current_currency = self.context.get_current_currency()
        currency_symbol = self.context.get_current_currency_symbol()

        validate_result = validate.validate_state_c_values(funds, entry_price, risk, trailing_stop)
        if validate_result.get('status') == 'error':
            error_message = validate_result.get('error_message')
            messagebox.showerror('Error', error_message)
            return

        equity_at_risk = float(funds) * (float(risk) / 100)
        results_stringvars_dict.get('equity_at_risk').set(
            currency_symbol + currency_formatter.float_to_currency(equity_at_risk, current_currency))
        stop_price = float(entry_price) * ((100 - float(trailing_stop)) / 100)
        results_stringvars_dict.get('stop_price').set(
            currency_symbol + currency_formatter.float_to_currency(stop_price, current_currency))
        shares = float(equity_at_risk) / (float(entry_price) - float(stop_price))
        results_stringvars_dict.get('shares').set(str(int(shares)))
        position_value = int(shares) * float(entry_price)
        results_stringvars_dict.get('position_value').set(
            currency_symbol + currency_formatter.float_to_currency(position_value, current_currency))


class StateD(State):
    """
    Strategy: Fixed Risk
    Stop type: Stop price
    """

    def calculate(self, funds, entry_price, risk, trailing_stop, stop_price):
        results_stringvars_dict = self.context.get_results_stringvars_dict()
        current_currency = self.context.get_current_currency()
        currency_symbol = self.context.get_current_currency_symbol()

        validate_result = validate.validate_state_d_values(funds, entry_price, risk, stop_price)
        if validate_result.get('status') == 'error':
            error_message = validate_result.get('error_message')
            messagebox.showerror('Error', error_message)
            return

        equity_at_risk = float(funds) * (float(risk) / 100)
        results_stringvars_dict.get('equity_at_risk').set(
            currency_symbol + currency_formatter.float_to_currency(equity_at_risk, current_currency))
        results_stringvars_dict.get('stop_price').set(currency_symbol + str(stop_price))
        shares = float(equity_at_risk) / (float(entry_price) - float(stop_price))
        results_stringvars_dict.get('shares').set(str(int(shares)))
        position_value = int(shares) * float(entry_price)
        results_stringvars_dict.get('position_value').set(
            currency_symbol + currency_formatter.float_to_currency(position_value, current_currency))
