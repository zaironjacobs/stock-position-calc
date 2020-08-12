status_str = 'status'
success_str = 'success'

error_str = 'error'
error_message_str = 'error_message'

enter_numeric_value_str = 'Please enter a numeric value.'
entry_price_not_zero_str = 'Entry price cannot be 0.'
trailing_stop_not_zero_str = 'Trailing stop cannot be 0.'
entry_price_no_more_than_funds_str = 'Entry price cannot be more than funds.'
stop_price_less_than_entry_str = 'Stop price has to be less than entry price.'
no_negative_numbers_str = 'Negative numbers are not allowed.'


def validate_state_a_values(funds, entry_price, trailing_stop):
    try:
        funds = float(funds)
        entry_price = float(entry_price)
        trailing_stop = float(trailing_stop)
    except ValueError:
        return {status_str: error_str, error_message_str: enter_numeric_value_str}
    if __value_is_zero(entry_price):
        return {status_str: error_str, error_message_str: entry_price_not_zero_str}
    if not __value1_is_less_than_or_equal_to_value2(entry_price, funds):
        return {status_str: error_str, error_message_str: entry_price_no_more_than_funds_str}
    if __value_is_negative(trailing_stop):
        return {status_str: error_str, error_message_str: no_negative_numbers_str}
    if __value_is_zero(trailing_stop):
        return {status_str: error_str, error_message_str: trailing_stop_not_zero_str}
    return {status_str: success_str}


def validate_state_b_values(funds, entry_price, stop_price):
    try:
        funds = float(funds)
        entry_price = float(entry_price)
        stop_price = float(stop_price)
    except ValueError:
        return {status_str: error_str, error_message_str: enter_numeric_value_str}
    if __value_is_zero(entry_price):
        return {status_str: error_str, error_message_str: entry_price_not_zero_str}
    if not __value1_is_less_than_or_equal_to_value2(entry_price, funds):
        return {status_str: error_str, error_message_str: entry_price_no_more_than_funds_str}
    if __value1_is_less_than_or_equal_to_value2(entry_price, stop_price):
        return {status_str: error_str, error_message_str: stop_price_less_than_entry_str}
    if __value_is_negative(stop_price):
        return {status_str: error_str, error_message_str: no_negative_numbers_str}
    return {status_str: success_str}


def validate_state_c_values(funds, entry_price, risk, trailing_stop):
    try:
        funds = float(funds)
        entry_price = float(entry_price)
        risk = float(risk)
        trailing_stop = float(trailing_stop)
    except ValueError:
        return {status_str: error_str, error_message_str: enter_numeric_value_str}
    if __value_is_zero(entry_price):
        return {status_str: error_str, error_message_str: entry_price_not_zero_str}
    if not __value1_is_less_than_or_equal_to_value2(entry_price, funds):
        return {status_str: error_str, error_message_str: entry_price_no_more_than_funds_str}
    if __value_is_negative(risk) or __value_is_negative(trailing_stop):
        return {status_str: error_str, error_message_str: no_negative_numbers_str}
    if __value_is_zero(trailing_stop):
        return {status_str: error_str, error_message_str: trailing_stop_not_zero_str}
    return {status_str: success_str}


def validate_state_d_values(funds, entry_price, risk, stop_price):
    try:
        funds = float(funds)
        entry_price = float(entry_price)
        risk = float(risk)
        stop_price = float(stop_price)
    except ValueError:
        return {status_str: error_str, error_message_str: enter_numeric_value_str}
    if __value_is_zero(entry_price):
        return {status_str: error_str, error_message_str: entry_price_not_zero_str}
    if not __value1_is_less_than_or_equal_to_value2(entry_price, funds):
        return {status_str: error_str, error_message_str: entry_price_no_more_than_funds_str}
    if __value1_is_less_than_or_equal_to_value2(entry_price, stop_price):
        return {status_str: error_str, error_message_str: stop_price_less_than_entry_str}
    if __value_is_negative(risk) or __value_is_negative(stop_price):
        return {status_str: error_str, error_message_str: no_negative_numbers_str}
    return {status_str: success_str}


def __value1_is_less_than_or_equal_to_value2(value1, value2):
    return value1 <= value2


def __value1_is_less_than_value2(value1, value2):
    return value1 < value2


def __value_is_zero(value):
    return value == 0


def __value_is_negative(value):
    return value < 0
