""""
def merge_dataframes():
    dates = self.dates
    columns = pd.MultiIndex.from_product([tickers, features], names = ["Ticker", "Feature"])

    df = pd.DataFrame(index = dates, columns = columns)

    df[:] = "E"
    print("OK")
    df.to_csv("test.csv")
    return df
"""