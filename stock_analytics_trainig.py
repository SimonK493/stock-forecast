
#libraries
import numpy as np
import pandas as pd


class ModelTrainer:

    def __init__(self, data):
        self.data = data

    def train_test_split(self):

        train_data = {}
        test_data = {}

        for ticker, df_list in self.data.items():

            if ticker not in train_data:
                train_data[ticker] = []
                test_data[ticker] = []

            for df in df_list:
                
                train_size = int(len(df) * 0.8)
                train_data[ticker].append(df[:train_size])
                test_data[ticker].append(df[train_size:])
        
        print(test_data)



