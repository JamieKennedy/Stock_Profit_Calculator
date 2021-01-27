import pandas as pd
import sys


def main(csv_file):

    try:
        df = pd.read_csv(csv_file)
    except:
        print("Unable to open {}".format(csv_file))
        return

    sales = get_sales(df)
    dividends = get_dividends(df)

    sales_profit = 0
    dividends_profit = 0

    for index, row in sales.iterrows():
        sales_profit += row["Result (GBP)"]

    print("Sales Profit: £{:,.2f}".format(sales_profit))

    for index, row in dividends.iterrows():
        dividends_profit += row["Total (GBP)"]

    print("Dividends Profit: £{:,.2f}".format(dividends_profit))


def get_sales(df):
    return df.query('Action in ["Market sell", "Limit sell", "Stop sell"]')


def get_dividends(df):
    return df.query('Action in ["Dividend (Ordinary)"]')


if __name__ == '__main__':
    args = sys.argv

    if len(args) > 1:
        main(args[1])
    else:
        print("Please specify a location for the .csv")
