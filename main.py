import downloader, data_cleaner, feature_engineer
from feature_engineer import FinancialIndicators
from tickers import tickers
from results_collector import collect_result
#libraries
import multiprocessing as mp


def main():
    data = downloader.data_downloader()
    cleaned_data = data_cleaner.cleaner(data)
    fi = FinancialIndicators(cleaned_data)

    #Multiprocessing of the DF
    manager = mp.Manager()
    final_data = manager.dict()
    pool = mp.Pool(mp.cpu_count())
    for ticker in tickers:
        pool.apply_async(fi.calculate_indicators, args = (ticker,), callback = collect_result)
    
    pool.close()
    pool.join

    final_data = dict(final_data)
    
    print(final_data)
    




if __name__ == "__main__":
    main()
