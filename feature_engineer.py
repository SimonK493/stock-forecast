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

        adj_close = self.data[ticker]["Adj Close"]

        sma_20 = adj_close.rolling(window = 20, min_periods = 1).mean()
        sma_50 = adj_close.rolling(window = 50, min_periods = 1).mean()

        sma_20_values.extend(sma_20)
        sma_50_values.extend(sma_50)
        
        df_sma20 = self.create_dataframe(ticker, sma_20_values)
        df_sma50 = self.create_dataframe(ticker, sma_50_values)
    
        return df_sma20, df_sma50
    
    
    def volatility(self, ticker: str):
        volatility_20_values = []
        volatility_50_values = []

        adj_close = self.data[ticker]["Adj Close"]

        sma_20 = adj_close.rolling(window = 20, min_periods = 1).mean().tolist()
        sma_50 = adj_close.rolling(window = 50, min_periods = 1).mean().tolist()

        for i in range(len(adj_close)):
            volatility_20 = 0.05 * np.power(adj_close.iloc[i] - sma_20[i], 2)
            volatility_50 = 0.05 * np.power(adj_close.iloc[i] - sma_50[i], 2)

            volatility_20_values.append(np.sqrt(volatility_20))
            volatility_50_values.append(np.sqrt(volatility_50))

        df_volatility_20 = self.create_dataframe(ticker, volatility_20_values)
        df_volatility_50 = self.create_dataframe(ticker, volatility_50_values)

        return df_volatility_20, df_volatility_50

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
        self.volatility("AAPL")
        

if __name__ == "__main__":
    ...
    
    