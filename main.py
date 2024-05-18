import downloader, data_cleaner, loader

def main():
    data = downloader.data_downloader()
    cleaned_data = data_cleaner.cleaner(data)


if __name__ == "__main__":
    main()
