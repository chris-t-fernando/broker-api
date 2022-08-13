if __name__ == "__main__":
    starting_balance = 10000
    api = BackTestAPI(back_testing=True, back_testing_balance=starting_balance)

    import pandas as pd

    import utils

    f_file = "bots/tests/fixtures/order_buy_active.txt"
    f = open(f_file, "r")
    order_file = f.read()
    unpickled_order = utils.unpickle(order_file)

    data = pd.read_csv(
        f"bots/tests/fixtures/symbol_chris.csv",
        index_col=0,
        parse_dates=True,
        infer_datetime_format=True,
    )

    api._put_bars("CHRIS", data)
    back_testing_date = Timestamp("2022-05-09 14:50:00").tz_localize(pytz.utc)

    api.get_account()
    api.list_positions()

    api.buy_order_market(symbol="CHRIS", units=10, back_testing_date=back_testing_date)
    api.sell_order_market(symbol="CHRIS", units=4, back_testing_date=back_testing_date)
    api.sell_order_limit(
        symbol="CHRIS", units=3, unit_price=20, back_testing_date=back_testing_date
    )
    # api.buy_order_limit(
    #    symbol="CHRIS", units=3, unit_price=150, back_testing_date=back_testing_date
    # )
    # api.buy_order_limit(
    #    symbol="CHRIS", units=4, unit_price=150, back_testing_date=back_testing_date
    # )
    # api.buy_order_limit(
    #    symbol="CHRIS", units=3, unit_price=150, back_testing_date=back_testing_date
    # )
    # api.sell_order_limit(
    #    symbol="CHRIS", units=3.5, unit_price=151, back_testing_date=back_testing_date
    # )
    # api.sell_order_limit(
    #    symbol="CHRIS", units=6.5, unit_price=151, back_testing_date=back_testing_date
    # )

    print(f"Profit: {round(api._balance - starting_balance,2)}")
    api.list_orders()
    print("banana")
