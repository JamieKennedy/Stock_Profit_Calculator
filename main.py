import pandas as pd
import sys


def main(csv_file):

    try:
        df = pd.read_csv(csv_file)
    except:
        print("Unable to open {}".format(csv_file))
        return

    sales = get_sales(df)



    profit = 0

    for index, row in sales.iterrows():
        profit += row["Result (GBP)"]

    print("Profit: £{:,.2f}".format(profit))


def get_sales(df):
    return df.query('Action in ["Market sell", "Limit sell", "Stop sell"]')


if __name__ == '__main__':
    args = sys.argv

    if len(args) > 1:
        main(args[1])
    else:
        print("Please specify as location for the .csv")
