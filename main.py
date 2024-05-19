import downloader, data_cleaner, feature_engineer

def main():
    data = downloader.data_downloader()
    cleaned_data = data_cleaner.cleaner(data)
    final_data = feature_engineer.features(cleaned_data)


if __name__ == "__main__":
    main()
