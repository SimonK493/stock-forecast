def collect_result(result, final_data):
    ticker, data = result
    final_data[ticker] = data

    print(f"Calculations for {ticker} completed")

if __name__ == "__main__":
    collect_result()
