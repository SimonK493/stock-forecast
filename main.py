import downloader, data_cleaner, feature_engineer
from feature_engineer import FinancialIndicators
from tickers import tickers
from results_collector import collect_result
#from stock_analytics_trainig import ModelTrainer
from join_dataframes import join_dataframes
#libraries
import multiprocessing as mp
import os


def main():
    data = downloader.data_downloader()
    cleaned_data = data_cleaner.cleaner(data)
    fi = FinancialIndicators(cleaned_data)

    os.system("cls")
    print("Starting calculations")

    #Multiprocessing of the DF
    manager = mp.Manager()
    final_data = manager.dict()
    pool = mp.Pool(mp.cpu_count())
    for ticker in tickers:
        pool.apply_async(fi.calculate_indicators, args = (ticker,), callback = lambda result: collect_result(result, final_data))

    pool.close()
    pool.join()

    os.system("cls")
    print("Joining Dataframes...")
    final_data = dict(final_data)
    
    final_df = join_dataframes(final_data)


    # trainer = ModelTrainer(final_data)
    # trainer.train_test_split()
    




if __name__ == "__main__":
    main()
