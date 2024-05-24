import downloader, data_cleaner, feature_engineer
from feature_engineer import FinancialIndicators

def main():
    data = downloader.data_downloader()
    cleaned_data = data_cleaner.cleaner(data)
    fi = FinancialIndicators(cleaned_data)
    final_data = fi.calculate_indicators()
    



if __name__ == "__main__":
    main()
