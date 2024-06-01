from tickers import tickers, features
#libraries
import pandas as pd

def join_dataframes(data):
    final_data = {}
    for ticker, dfs in data.items():
        result = pd.concat(dfs, axis = 1)
        result.columns = features
        result.dropna(how = "any", inplace = True)
        final_data[ticker] = result

    final_data["AAPL"].to_csv("final_format.csv")
    
    return final_data
    
        