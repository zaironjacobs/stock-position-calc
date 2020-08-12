usd_str = 'USD'
eur_str = 'EUR'
unable_to_identify_float_decimal_str = 'unable to identify float decimal point'


class UnknownCurrencyError(Exception):
    pass


def float_to_currency(float_value, currency, decimal=2):
    """
    Formats a float to currency string
    USD example: 10000.0 -> '10,000.00'
    EUR example: 10000.0 -> '10.000,00'
    """

    float_value_str = format(float_value, '.' + str(decimal) + 'f')

    # USD
    if currency.lower() == usd_str.lower():
        if float_value_str.count('.') == 1:
            after_decimal_str = float_value_str.rsplit('.', 1)[1]
        else:
            identifier = unable_to_identify_float_decimal_str
            raise ValueError(identifier)

        before_decimal_str = float_value_str.split('.', 1)[0]
        formatted_before_decimal_str = ''
        for idx, char in enumerate(reversed(before_decimal_str)):
            if idx != 0 and idx % 3 == 0:
                formatted_before_decimal_str = ',' + formatted_before_decimal_str
            formatted_before_decimal_str = char + formatted_before_decimal_str
        formatted_value = formatted_before_decimal_str + '.' + after_decimal_str
        return formatted_value

    # EUR
    elif currency.lower() == eur_str.lower():
        if float_value_str.count('.') == 1:
            float_value_str = float_value_str.replace('.', ',')
            after_decimal_str = float_value_str.rsplit(',', 1)[1]
        else:
            identifier = unable_to_identify_float_decimal_str
            raise ValueError(identifier)

        before_decimal_str = float_value_str.split(',', 1)[0]
        formatted_before_decimal_str = ''
        for idx, char in enumerate(reversed(before_decimal_str)):
            if idx != 0 and idx % 3 == 0:
                formatted_before_decimal_str = '.' + formatted_before_decimal_str
            formatted_before_decimal_str = char + formatted_before_decimal_str
        formatted_value = formatted_before_decimal_str + ',' + after_decimal_str
        return formatted_value

    else:
        identifier = "unknown currency " + "'" + currency + "'"
        raise UnknownCurrencyError(identifier)


def currency_to_float(currency_value, currency, decimal=2):
    """
    Formats a currency string to float
    USD example: '10,000.00' -> 10000.0
    EUR example: '10.000,00' -> 10000.0
    """

    # USD
    if currency.lower() == usd_str.lower():
        if currency_value.count(',') > 0:
            try:
                value = format(float(currency_value.replace(',', '')), '.' + str(decimal) + 'f')
                return float(value)
            except ValueError:
                return currency_value
        else:
            try:
                value = format(float(currency_value), '.' + str(decimal) + 'f')
                return float(value)
            except ValueError:
                return currency_value

    # EUR
    elif currency.lower() == eur_str.lower():
        try:
            value = format(float(currency_value.replace('.', '').replace(',', '.')), '.' + str(decimal) + 'f')
            return float(value)
        except ValueError:
            return currency_value

    # Unknown currency
    else:
        identifier = "unknown currency " + "'" + currency + "'"
        raise UnknownCurrencyError(identifier)
