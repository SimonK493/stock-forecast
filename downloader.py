from tickers import tickers
#libraries
import yfinance as yf

def data_downloader():
    print("Download historical financial data:")
    # "Most interesting" shares in the sectors: Technology, Financials, Healthcare, Consumer Discretionary, Industrials, Energy, Utilities
    data = yf.download(tickers, group_by = "ticker")
    data.to_csv("my.csv")
    return data

if __name__ == "__main__":
    data = data_downloader()
    print(data)