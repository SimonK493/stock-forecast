
#libraries
import yfinance as yf

def data_downloader():
    # "Most interesting" shares in the sectors: Technology, Financials, Healthcare, Consumer Discretionary, Industrials, Energy, Utilities
    #tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "JPM", "GS", "BAC", "JNJ", "PFE", "MRK", "KO", "PEP", "PG", "GE", "BA", "CAT", "XOM", "CVX", "COP", "DUK", "NEE", "D"]
    tickers = ["AAPL"]
    data = yf.download(tickers,period = "1d")
    return data

if __name__ == "__main__":
    data = data_downloader()
    print(data)
