def collect_result(result, final_data):
    ticker, data = result
    final_data[ticker] = data

    print(f"Calculations for {ticker} completed")
