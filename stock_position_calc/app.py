from tkinter import *
from tkinter import messagebox

from . import state as app_state
from . import currency_formatter


def main():
    App()


class App:

    def __init__(self):
        self.__root = Tk()
        self.__root.title('Stock Position Calculator')
        self.__root.geometry('525x685')
        self.__root.resizable(False, False)

        self.__state = None

        self.__currencies_dict = {'USD': '$', 'EUR': '€'}
        self.__current_currency_stringvar = StringVar()
        self.__current_currency_stringvar.set('USD')
        self.__current_currency_symbol_stringvar = StringVar()

        self.__strategies_dict = {'fixed_risk': 'Fixed Risk',
                                  'fixed_cash': 'Fixed Cash Amount'}
        self.__current_strategy_stringvar = StringVar()
        self.__current_strategy_stringvar.set(self.__strategies_dict.get('fixed_risk'))

        self.__stop_types_dict = {'trailing_stop': 'Trailing Stop', 'stop_price': 'Stop Price'}
        self.__current_stop_type_stringvar = StringVar()
        self.__current_stop_type_stringvar.set(self.__stop_types_dict.get('trailing_stop'))

        self.__fixed_dollar_strategy = self.__strategies_dict.get('fixed_cash')
        self.__fixed_risk_strategy = self.__strategies_dict.get('fixed_risk')
        self.__trailing_stop_stop_type = self.__stop_types_dict.get('trailing_stop')
        self.__stop_price_stop_type = self.__stop_types_dict.get('stop_price')

        self.__default_font_style = 'Helvetica'
        self.__default_font_size = 14
        self.__default_font_weight = ''

        self.__default_button_width = 18

        self.__form_entries_dict = self.__create_form()
        self.__create_buttons()
        self.__results_stringvars_dict = self.__create_results()

        self.__refresh_ui_strategy()
        self.__refresh_ui_currency()
        self.__refresh_ui_stop_type()

        self.__root.mainloop()

    def __get_current_currency(self):
        return self.__current_currency_stringvar.get()

    def __get_current_currency_symbol(self):
        return self.__current_currency_symbol_stringvar.get()

    def __init_calculation(self):
        """ Initialize the calculation """

        current_strategy = self.__current_strategy_stringvar.get()
        current_stop_type = self.__current_stop_type_stringvar.get()

        if current_strategy == self.__fixed_dollar_strategy and current_stop_type == self.__trailing_stop_stop_type:
            self.__change_state(app_state.StateA())
        elif current_strategy == self.__fixed_dollar_strategy and current_stop_type == self.__stop_price_stop_type:
            self.__change_state(app_state.StateB())
        elif current_strategy == self.__fixed_risk_strategy and current_stop_type == self.__trailing_stop_stop_type:
            self.__change_state(app_state.StateC())
        elif current_strategy == self.__fixed_risk_strategy and current_stop_type == self.__stop_price_stop_type:
            self.__change_state(app_state.StateD())

        funds = currency_formatter.currency_to_float(self.__form_entries_dict.get(
            'funds').get(), self.__get_current_currency())
        entry_price = currency_formatter.currency_to_float(self.__form_entries_dict.get(
            'entry_price').get(), self.__get_current_currency())
        risk = currency_formatter.currency_to_float(self.__form_entries_dict.get(
            'risk').get(), self.__get_current_currency())
        trailing_stop = currency_formatter.currency_to_float(self.__form_entries_dict.get(
            'trailing_stop').get(), self.__get_current_currency())
        stop_price = currency_formatter.currency_to_float(self.__form_entries_dict.get(
            'stop_price').get(), self.__get_current_currency())

        error_message = self.__state.set_values(funds, entry_price, risk, trailing_stop, stop_price)
        if error_message:
            messagebox.showerror('Error', error_message)
            return

        calculated_shares = self.__state.calculate_shares()
        self.__results_stringvars_dict.get('shares').set(str(calculated_shares))

        calculated_position_value = self.__state.calculate_position_value()
        self.__results_stringvars_dict.get('position_value').set(
            self.__get_current_currency_symbol() + currency_formatter.float_to_currency(
                calculated_position_value, self.__get_current_currency()))

        calculated_equity_at_risk = self.__state.calculate_equity_at_risk()
        if calculated_equity_at_risk is not None:
            self.__results_stringvars_dict.get('equity_at_risk').set(
                self.__get_current_currency_symbol() + currency_formatter.float_to_currency(
                    calculated_equity_at_risk, self.__get_current_currency()))
        else:
            self.__results_stringvars_dict.get('equity_at_risk').set('-')

        calculated_stop_price = self.__state.calculate_stop_price()
        self.__results_stringvars_dict.get('stop_price').set(
            self.__get_current_currency_symbol() + currency_formatter.float_to_currency(
                calculated_stop_price, self.__get_current_currency()))

    def __change_state(self, state):
        """ Change to given state """

        self.__state = state

    def __refresh_ui_currency(self):
        """ UI changes concerning the current currency  """

        currency_symbol = self.__currencies_dict.get(self.__current_currency_stringvar.get())
        self.__current_currency_symbol_stringvar.set(currency_symbol)

        for key, value in self.__form_entries_dict.items():
            if key == 'funds' or key == 'entry_price' or key == 'stop_price':
                value.delete(0, END)

        for value in self.__results_stringvars_dict.values():
            value.set('')

    def __refresh_ui_strategy(self):
        """ UI changes concerning the current strategy  """

        if self.__current_strategy_stringvar.get() == self.__strategies_dict.get('fixed_cash'):
            self.__form_entries_dict.get('risk').delete(0, END)
            self.__form_entries_dict.get('risk').config(state='disabled')
        elif self.__current_strategy_stringvar.get() == self.__strategies_dict.get('fixed_risk'):
            self.__form_entries_dict.get('risk').config(state='normal')

    def __refresh_ui_stop_type(self):
        """ UI changes concerning the current stop type  """

        if self.__current_stop_type_stringvar.get() == self.__stop_types_dict.get('trailing_stop'):
            self.__form_entries_dict.get('trailing_stop').config(state='normal')
            self.__form_entries_dict.get('stop_price').delete(0, END)
            self.__form_entries_dict.get('stop_price').config(state='disabled')
        elif self.__current_stop_type_stringvar.get() == self.__stop_types_dict.get('stop_price'):
            self.__form_entries_dict.get('stop_price').config(state='normal')
            self.__form_entries_dict.get('trailing_stop').delete(0, END)
            self.__form_entries_dict.get('trailing_stop').config(state='disabled')

    def __create_form(self):
        """ Create the form UI """

        form_entries_dict = {}

        form_fields_dict = {}
        form_fields_dict.update({'strategy': 'Strategy'})
        form_fields_dict.update({'currency': 'Currency'})
        form_fields_dict.update({'funds': 'Funds'})
        form_fields_dict.update({'entry_price': 'Entry Price'})
        form_fields_dict.update({'risk': 'Risk'})
        form_fields_dict.update({'stop_type': 'Stop Type'})
        form_fields_dict.update({'trailing_stop': 'Trailing Stop'})
        form_fields_dict.update({'stop_price': 'Stop Price'})

        for key, value in form_fields_dict.items():
            row = Frame(self.__root)
            row.pack(side=TOP, fill=X, padx=50, pady=5)

            # All field labels
            Label(row, font=(self.__default_font_style, self.__default_font_size, self.__default_font_weight),
                  width=12, text=value, anchor='w').pack(side=LEFT)

            # STRATEGY OPTION
            if key == 'strategy':
                Label(row, font=(self.__default_font_style, self.__default_font_size, self.__default_font_weight),
                      text='  ').pack(side=LEFT)
                # Strategy option menu
                strategy_option_menu = OptionMenu(row, self.__current_strategy_stringvar,
                                                  *self.__strategies_dict.values(),
                                                  command=lambda x: self.__refresh_ui_strategy())
                strategy_option_menu.pack(anchor='w')
                strategy_option_menu.config(
                    font=(self.__default_font_style, 12, self.__default_font_weight))

            # CURRENCY OPTION
            elif key == 'currency':
                # Currency label
                Label(row, font=(self.__default_font_style, self.__default_font_size, self.__default_font_weight),
                      text='  ').pack(side=LEFT)
                # Currency option menu
                currency_option_menu = OptionMenu(row, self.__current_currency_stringvar,
                                                  *self.__currencies_dict,
                                                  command=lambda x: self.__refresh_ui_currency())
                currency_option_menu.pack(anchor='w')
                currency_option_menu.config(
                    font=(self.__default_font_style, 12, self.__default_font_weight))

            # RADIO BUTTONS
            elif key == 'stop_type':
                for stop_type_key, stop_type_value in self.__stop_types_dict.items():
                    Radiobutton(row, font=(self.__default_font_style, 12, self.__default_font_weight),
                                variable=self.__current_stop_type_stringvar,
                                text=stop_type_value, value=stop_type_value,
                                command=lambda: self.__refresh_ui_stop_type()).pack(anchor=W)

            # ENTRIES
            elif key == 'funds' or key == 'entry_price' or key == 'risk' or key == 'trailing_stop' or \
                    key == 'stop_price':

                # CURRENCY SYMBOL LABELS
                if key == 'funds' or key == 'entry_price' or key == 'stop_price':
                    Label(row, font=(self.__default_font_style, self.__default_font_size, self.__default_font_weight),
                          textvariable=self.__current_currency_symbol_stringvar).pack(side=LEFT)
                else:
                    Label(row, font=(self.__default_font_style, self.__default_font_size, self.__default_font_weight),
                          text='  ').pack(side=LEFT)

                entry = Entry(row,
                              font=(self.__default_font_style, self.__default_font_size, self.__default_font_weight))
                entry.bind("<FocusOut>", lambda x: self.__format_entry_currency_value())
                entry.pack(side=LEFT, expand=NO, fill=X)

                # PERCENTAGE LABELS
                if key == 'risk' or key == 'trailing_stop':
                    Label(row, font=(self.__default_font_style, self.__default_font_size, self.__default_font_weight),
                          width=12, text='%',
                          anchor='w').pack(side=LEFT)

                form_entries_dict.update({key: entry})

        return form_entries_dict

    def __format_entry_currency_value(self):
        """ Formats the entry values to a currency value when an entry loses focus """

        for key, value in self.__form_entries_dict.items():
            if key == 'funds' or key == 'entry_price' or key == 'stop_price':
                value_str = value.get()
                if self.__get_current_currency() == 'USD':
                    value_str = value_str.replace(',', '')
                elif self.__get_current_currency() == 'EUR':
                    value_str = value_str.replace(',', '.')
                if value_str == '':
                    continue
                try:
                    number = currency_formatter.float_to_currency(float(value_str), self.__get_current_currency())
                except ValueError:
                    pass
                else:
                    value.delete(0, END)
                    value.insert(0, str(number))

    def __create_buttons(self):
        """ Create the buttons """

        # CALCULATE BUTTON
        Button(self.__root, font=(self.__default_font_style, self.__default_font_size, self.__default_font_weight),
               width=self.__default_button_width,
               text='Calculate', command=lambda: self.__init_calculation()).pack(side=TOP, pady=15)

        # EXIT BUTTON
        Button(self.__root, font=(self.__default_font_style, self.__default_font_size, self.__default_font_weight),
               width=self.__default_button_width,
               text='Exit', command=lambda: self.__quit()).pack(side=TOP)

    def __create_results(self):
        """ Create the results UI """

        # SPACER
        Frame(self.__root).pack(pady=10)

        # RESULTS TOP LABEL
        row_results = Frame(self.__root)
        row_results.pack(side=TOP)
        Label(row_results, font=(self.__default_font_style, self.__default_font_size, 'bold'),
              text='Results').pack(side=LEFT, expand=NO, fill=X)

        # SPACER
        Frame(self.__root).pack(pady=5)

        results_stringvars_dict = {}

        results_fields_dict = {}
        results_fields_dict.update({'shares': 'Shares'})
        results_fields_dict.update({'position_value': 'Position Value'})
        results_fields_dict.update({'equity_at_risk': 'Equity at Risk'})
        results_fields_dict.update({'stop_price': 'Stop Price'})

        for key, value in results_fields_dict.items():
            row = Frame(self.__root)
            row.pack(side=TOP, fill=X, padx=50, pady=5)

            # FIELD LABELS
            Label(row, font=(self.__default_font_style, self.__default_font_size, self.__default_font_weight),
                  width=12, text=value, padx=2, anchor='w').pack(side=LEFT)

            # COLON LABELS
            Label(row, font=(self.__default_font_style, self.__default_font_size, self.__default_font_weight),
                  text=': ').pack(side=LEFT)

            # RESULT VALUE LABELS
            stringvar = StringVar()
            Label(row, font=(self.__default_font_style, self.__default_font_size, self.__default_font_weight),
                  textvariable=stringvar).pack(side=LEFT)
            results_stringvars_dict.update({key: stringvar})

        return results_stringvars_dict

    def __quit(self):
        """ Quit the app """

        self.__root.quit()
