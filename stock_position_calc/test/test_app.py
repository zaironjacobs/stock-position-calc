from .. import state as app_state


class TestApp:

    ###########
    # STATE A #
    ###########
    def test_state_a(self):
        funds = 30000
        entry_price = 122.57
        risk = None
        trailing_stop = 8
        stop_price = None

        state_a = app_state.StateA()
        state_a.set_values(funds, entry_price, risk, trailing_stop, stop_price)

        result = [state_a.calculate_shares(),
                  round(state_a.calculate_position_value(), 2),
                  state_a.calculate_equity_at_risk(),
                  round(state_a.calculate_stop_price(), 2)]

        expected = [244,
                    29907.08,
                    None,
                    112.76]

        assert result == expected

    ###########
    # STATE B #
    ###########
    def test_state_b(self):
        funds = 50000
        entry_price = 324.78
        risk = None
        trailing_stop = None
        stop_price = 311.11

        state_b = app_state.StateB()
        state_b.set_values(funds, entry_price, risk, trailing_stop, stop_price)

        result = [state_b.calculate_shares(),
                  round(state_b.calculate_position_value(), 2),
                  state_b.calculate_equity_at_risk(),
                  round(state_b.calculate_stop_price(), 2)]

        expected = [153,
                    49691.34,
                    None,
                    311.11]

        assert result == expected

    ###########
    # STATE C #
    ###########
    def test_state_c(self):
        funds = 120000
        entry_price = 179.77
        risk = 2
        trailing_stop = 10
        stop_price = None

        state_c = app_state.StateC()
        state_c.set_values(funds, entry_price, risk, trailing_stop, stop_price)

        result = [state_c.calculate_shares(),
                  round(state_c.calculate_position_value(), 2),
                  round(state_c.calculate_equity_at_risk(), 2),
                  round(state_c.calculate_stop_price(), 2)]

        expected = [133,
                    23909.41,
                    2400.0,
                    161.79]

        assert result == expected

    ###########
    # STATE D #
    ###########
    def test_state_d(self):
        funds = 80000
        entry_price = 224.99
        risk = 2
        trailing_stop = None
        stop_price = 150.68

        state_d = app_state.StateD()
        state_d.set_values(funds, entry_price, risk, trailing_stop, stop_price)

        result = [state_d.calculate_shares(),
                  round(state_d.calculate_position_value(), 2),
                  round(state_d.calculate_equity_at_risk(), 2),
                  round(state_d.calculate_stop_price(), 2)]

        expected = [21,
                    4724.79,
                    1600,
                    150.68]

        assert result == expected
