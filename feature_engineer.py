from tickers import tickers, features
#libraries
import pandas as pd
import numpy as np
from multiprocessing import Pool, cpu_count


class FinancialIndicators:
    def __init__(self, scaled_data):
        self.data = scaled_data
        self.dates = scaled_data.index.get_level_values("Date").unique().strftime("%Y-%m-%d")
    
    def daily_return(self, ticker, df):
        for date in self.dates:
            print(self.data.loc[date, ticker]["Open"])

    def simple_moving_average(self):
        #ta.sma(,length = 20)
        #ta.sma(,length = 50)
        ...
    
    def volatility(self):
        
        ...
    
    def exponential_moving_average(self):
        ...
    
    def relative_strength_index(self):
        ...
    
    def rate_of_change(self):
        ...
    
    def macd_line(self):
        ...
    
    def signal_line(self):
        ...
    
    def on_balance_volume(self):
        ...

    def daily_range(self):
        ...

    def intraday_change(self):
        ...

    def create_dataframe(self):
        dates = self.dates
        columns = pd.MultiIndex.from_product([tickers, features], names = ["Ticker", "Feature"])

        df = pd.DataFrame(index = dates, columns = columns)

        df[:] = 0
        print("OK")
        return df


    def calculate_indicators(self):
        df = self.create_dataframe()
        for ticker in tickers:
            self.daily_return(ticker, df)
        

if __name__ == "__main__":
    ...
    
    