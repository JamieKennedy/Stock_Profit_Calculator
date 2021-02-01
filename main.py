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

    sales_gains = 0
    sales_losses = 0
    sales_profit = 0
    dividends_profit = 0

    for index, row in sales.iterrows():
        result = row["Result (GBP)"]

        if result >= 0:
            sales_gains += result
        if result <= 0:
            sales_losses += result

        sales_profit += result

    print("Sales Gains: £{:,.2f}".format(sales_gains))
    print("Sales Losses: £{:,.2f}".format(sales_losses))
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
