# Tickers of the most important or largest companies in the areas of consumer goods, energy, finance, healthcare, industry, providers and technology
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "JPM", "GS", "BAC", "JNJ", "PFE", "MRK", "KO", "PEP", "PG", "GE", "BA", "CAT", "XOM", "CVX", "COP", "DUK", "NEE", "D"]
#tickers = ["AAPL", "MSFT", "GOOGL"]
# Computed features for training the prediction model
features = ["daily_return", "sma_20", "sma_50", "volatility_20", "volatility_50", "ema_50", "ema_200", "relative_strength_index","roc_20", "roc_50","obv","daily_range","intraday_change"]