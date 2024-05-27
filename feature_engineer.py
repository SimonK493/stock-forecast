from tickers import tickers, features
#libraries
import pandas as pd
import numpy as np

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

        df_daily_return = self.create_dataframe(ticker, daily_returns)

        return df_daily_return
        
    

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

    def exponential_moving_average(self, ticker: str):

        adj_close = self.data[ticker]["Adj Close"]

        smoothing_factor_50 = 2 / 51
        smoothing_factor_200 = 2 / 201

        ema_50_period = []
        ema_200_period = []

        for i in range(len(adj_close)):
            if not np.isnan(adj_close.iloc[i]): 
                first_value = i
                break

        ema_50 = adj_close.iloc[first_value:first_value + 49].mean() if first_value + 49 <= len(adj_close) else None
        ema_200 = adj_close.iloc[first_value:first_value + 199].mean() if first_value + 199 <= len(adj_close) else None


        for i in range(len(adj_close)):

            if i < first_value:
                ema_50_period.append(np.nan)

            elif i >= first_value + 50:
                ema_50_period.append(smoothing_factor_50 * adj_close.iloc[i] + (1 - smoothing_factor_50) * ema_50)
                ema_50 = ema_50_period[-1]

            else:
                ema_50_period.append(ema_50)

            if i < first_value:
                ema_200_period.append(np.nan)

            elif i >= first_value + 200:
                ema_200_period.append(smoothing_factor_200 * adj_close.iloc[i] + (1 - smoothing_factor_200) * ema_200)
                ema_200 = ema_200_period[-1]
        
            else:
                ema_200_period.append(ema_200)

        df_ema_50 = self.create_dataframe(ticker, ema_50_period)
        df_ema_200 = self.create_dataframe(ticker, ema_200_period)

        return df_ema_50, df_ema_200
    
    def relative_strength_index(self,ticker: str):

        adj_close = self.data[ticker]["Adj Close"]
        price_changes = adj_close.diff()

        avg_gain_list = []
        avg_loss_list = []

        relative_strength_index_list = []

        for k in range(len(adj_close)):

            if not np.isnan(price_changes.iloc[k]):
                first_value = k 
                break

            else:
                relative_strength_index_list.append(np.nan)
                continue

        for i in range(first_value, len(price_changes)):

            if price_changes.iloc[i] > 0:
                avg_gain_list.append(price_changes.iloc[i])
                avg_loss_list.append(0)

            else:
                avg_gain_list.append(0)
                avg_loss_list.append(abs(price_changes.iloc[i]))

            avg_gain = sum(avg_gain_list) / len(avg_gain_list)
            avg_loss = sum(avg_loss_list) / len(avg_loss_list)

            if avg_loss == 0:
                relative_strength = avg_gain

            else:
                relative_strength = avg_gain / avg_loss
            
            relative_strength_index_list.append(100 / (1 + relative_strength))

        df_relative_strength_index = self.create_dataframe(ticker, relative_strength_index_list)

        return df_relative_strength_index

    def rate_of_change(self, ticker: str):

        adj_close = self.data[ticker]["Adj Close"]

        for j in range(len(adj_close)):
            if not np.isnan(adj_close.iloc[j]):
                first_value = j
                break

        roc_10 = []
        roc_50 = []

        for i in range(len(adj_close)):
            if i >= 9 + first_value:
                roc_10.append((adj_close.iloc[i] - adj_close.iloc[i - 9]) / adj_close.iloc[i - 9])

                if i >= 49 + first_value:
                    roc_50.append((adj_close.iloc[i] - adj_close.iloc[i - 49]) / adj_close.iloc[i - 49])
                
                else:
                    roc_50.append(np.nan)
            else:
                roc_10.append(np.nan)
                roc_50.append(np.nan)

        df_roc_10 = self.create_dataframe(ticker, roc_10)
        df_roc_50 = self.create_dataframe(ticker, roc_50)

        return df_roc_10, df_roc_50
    
    def on_balance_volume(self, ticker: str):

        adj_close = self.data[ticker]["Adj Close"]
        volumes = self.data[ticker]["Volume"]

        on_balance_volume_list = []

        for j in range(len(adj_close)):

            if not np.isnan(adj_close.iloc[j]):
                first_value = j + 1
                on_balance_volume_list.append(0)
                break

            else:
                on_balance_volume_list.append(np.nan)


        for i in range(first_value, len(adj_close)):
            closing_price = adj_close.iloc[i]
            closing_price_yesterday = adj_close.iloc[i - 1]
            volume = volumes.iloc[i]

            if closing_price > closing_price_yesterday:
                on_balance_volume_list.append(volume + on_balance_volume_list[-1])

            elif closing_price < closing_price_yesterday:
                on_balance_volume_list.append(on_balance_volume_list[-1] - volume)

            else:
                on_balance_volume_list.append(on_balance_volume_list[-1])


        df_on_balance_volume = self.create_dataframe(ticker, on_balance_volume_list)
        
        return df_on_balance_volume


    def daily_range(self, ticker: str):

        high_values = self.data[ticker]["High"]
        low_values = self.data[ticker]["Low"]

        daily_range_list = []

        for i in range(len(high_values)):
            daily_range_list.append(high_values.iloc[i] - low_values.iloc[i])
        
        df_daily_range = self.create_dataframe(ticker, daily_range_list)
        
        return df_daily_range

    def intraday_change(self, ticker: str):
        adj_close = self.data[ticker]["Adj Close"]
        open_values = self.data[ticker]["Open"]

        intraday_change_list = []

        for i in range(len(adj_close)):
            intraday_change_list.append((adj_close.iloc[i] - open_values.iloc[i]) / open_values.iloc[i])

        df_intraday_change = self.create_dataframe(ticker, intraday_change_list)

        return df_intraday_change


    def create_dataframe(self, ticker: str, data: list):
        df = pd.DataFrame(data, index = self.dates, columns = [ticker])
        return df
    

    def calculate_indicators(self, ticker):
        daily_return = self.daily_return(ticker)
        sma_20, sma_50 = self.simple_moving_average(ticker)
        volatility_20, volatility_50 = self.volatility(ticker)
        ema_50, ema_200 = self.exponential_moving_average(ticker)
        relative_strength_index = self.relative_strength_index(ticker)
        roc_20, roc_50 = self.rate_of_change(ticker)
        obv = self.on_balance_volume(ticker)
        daily_range = self.daily_range(ticker)
        intraday_change = self.intraday_change(ticker)

        return [daily_return, 
                sma_20, sma_50, 
                volatility_20, 
                volatility_50, 
                ema_50, ema_200, 
                relative_strength_index,
                roc_20, roc_50,
                obv,
                daily_range,
                intraday_change]
        
        

if __name__ == "__main__":
    ...
    
    