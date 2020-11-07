from abc import ABC, abstractmethod

from . import validate


class State(ABC):

    def __init__(self):
        self._funds = None
        self._entry_price = None
        self._risk = None
        self._trailing_stop = None
        self._stop_price = None

        self._shares = None
        self._equity_at_risk = None

    @abstractmethod
    def set_values(self, funds, entry_price, risk, trailing_stop, stop_price):
        pass

    @abstractmethod
    def calculate_shares(self):
        pass

    @abstractmethod
    def calculate_position_value(self):
        pass

    @abstractmethod
    def calculate_equity_at_risk(self):
        pass

    @abstractmethod
    def calculate_stop_price(self):
        pass


class StateA(State):
    """
    Strategy: Fixed Cash Amount
    Stop type: Trailing stop
    """

    def set_values(self, funds, entry_price, risk, trailing_stop, stop_price):
        self._funds = funds
        self._entry_price = entry_price
        self._risk = None
        self._trailing_stop = trailing_stop
        self._stop_price = None

        validate_result = validate.validate_state_a_values(self._funds, self._entry_price, self._trailing_stop)
        if validate_result.get('status') == 'error':
            return validate_result.get('error_message')

        self._stop_price = self.calculate_stop_price()
        self._shares = self.calculate_shares()

    def calculate_shares(self):
        return int(float(self._funds) / float(self._entry_price))

    def calculate_position_value(self):
        return float(self._shares) * float(self._entry_price)

    def calculate_equity_at_risk(self):
        return None

    def calculate_stop_price(self):
        return float(self._entry_price) * ((100 - float(self._trailing_stop)) / 100)


class StateB(State):
    """
    Strategy: Fixed Cash Amount
    Stop type: Stop price
    """

    def set_values(self, funds, entry_price, risk, trailing_stop, stop_price):
        self._funds = funds
        self._entry_price = entry_price
        self._risk = None
        self._trailing_stop = None
        self._stop_price = stop_price

        validate_result = validate.validate_state_b_values(funds, entry_price, stop_price)
        if validate_result.get('status') == 'error':
            return validate_result.get('error_message')

        self._shares = self.calculate_shares()

    def calculate_shares(self):
        return int(float(self._funds) / float(self._entry_price))

    def calculate_position_value(self):
        return float(self._shares) * float(self._entry_price)

    def calculate_equity_at_risk(self):
        return None

    def calculate_stop_price(self):
        return self._stop_price


class StateC(State):
    """
    Strategy: Fixed Risk
    Stop type: Trailing stop
    """

    def set_values(self, funds, entry_price, risk, trailing_stop, stop_price):
        self._funds = funds
        self._entry_price = entry_price
        self._risk = risk
        self._trailing_stop = trailing_stop
        self._stop_price = None

        validate_result = validate.validate_state_c_values(funds, entry_price, risk, trailing_stop)
        if validate_result.get('status') == 'error':
            return validate_result.get('error_message')

        self._equity_at_risk = self.calculate_equity_at_risk()
        self._stop_price = self.calculate_stop_price()
        self._shares = self.calculate_shares()

    def calculate_shares(self):
        return int(float(self._equity_at_risk) / (float(self._entry_price) - float(self._stop_price)))

    def calculate_position_value(self):
        return int(self._shares) * float(self._entry_price)

    def calculate_equity_at_risk(self):
        return float(self._funds) * (float(self._risk) / 100)

    def calculate_stop_price(self):
        return float(self._entry_price) * ((100 - float(self._trailing_stop)) / 100)


class StateD(State):
    """
    Strategy: Fixed Risk
    Stop type: Stop price
    """

    def set_values(self, funds, entry_price, risk, trailing_stop, stop_price):
        self._funds = funds
        self._entry_price = entry_price
        self._risk = risk
        self._trailing_stop = trailing_stop
        self._stop_price = stop_price

        validate_result = validate.validate_state_d_values(funds, entry_price, risk, stop_price)
        if validate_result.get('status') == 'error':
            return validate_result.get('error_message')

        self._equity_at_risk = self.calculate_equity_at_risk()
        self._shares = self.calculate_shares()

    def calculate_shares(self):
        return int(float(self._equity_at_risk) / (float(self._entry_price) - float(self._stop_price)))

    def calculate_position_value(self):
        return int(self._shares) * float(self._entry_price)

    def calculate_equity_at_risk(self):
        return float(self._funds) * (float(self._risk) / 100)

    def calculate_stop_price(self):
        return self._stop_price
