from tickers import tickers
#libraries
import yfinance as yf

def data_downloader():
    # "Most interesting" shares in the sectors: Technology, Financials, Healthcare, Consumer Discretionary, Industrials, Energy, Utilities
    #tickers = ["AAPL"]
    data = yf.download(tickers, group_by = "ticker")
    return data

if __name__ == "__main__":
    data = data_downloader()
    print(data)