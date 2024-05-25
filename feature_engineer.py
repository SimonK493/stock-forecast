from tickers import tickers, features
#libraries
import pandas as pd
import numpy as np
from multiprocessing import Pool, cpu_count


class FinancialIndicators:
    def __init__(self, scaled_data):
        self.data = scaled_data
        self.dates = scaled_data.index.get_level_values("Date").unique().strftime("%Y-%m-%d")
    

    def daily_return(self, ticker: str):
        adj_close_t1 = None
        daily_returns = []

        for date in self.dates:
            adj_close_t = self.data.loc[date, ticker]["Adj Close"]

            if not np.isnan(adj_close_t):

                if adj_close_t1 is not None:
                    daily_return = (adj_close_t - adj_close_t1) / adj_close_t1
                    daily_returns.append(daily_return)

                else:
                    daily_returns.append(adj_close_t)

                adj_close_t1 = adj_close_t

            else:
                daily_returns.append(np.nan)
                adj_close_t1 = None
        
        return self.create_dataframe(ticker, daily_returns)
    

    def simple_moving_average(self, ticker: str):
        sma_20_values = []
        sma_50_values = []

        for date in self.dates:
            adj_close = self.data.loc[date, ticker]["Adj Close"]

            adj_close_series = pd.Series(adj_close)

            sma_20 = adj_close_series.rolling(window = 20, min_periods = 1).mean().iloc[-1]
            sma_50 = adj_close_series.rolling(window = 50, min_periods = 1).mean().iloc[-1]

            sma_20_values.append(sma_20)
            sma_50_values.append(sma_50)
        
        df_sma20 = self.create_dataframe(ticker, sma_20_values)
        df_sma50 = self.create_dataframe(ticker, sma_50_values)

        df_sma20.to_csv("sma20.csv")
        df_sma50.to_csv("sma50.csv")
        
        return df_sma20, df_sma50
    
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


    def create_dataframe(self, ticker: str, data: list):
        df = pd.DataFrame(data, index = self.dates, columns = [ticker])
        return df
    

    def calculate_indicators(self):
        #for ticker in tickers:
            #self.daily_return(ticker)
        sma_20, sma_50 = self.simple_moving_average("AAPL")
        self.volatility()
        

if __name__ == "__main__":
    ...
    
    