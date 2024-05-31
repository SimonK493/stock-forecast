from tickers import tickers, features
#libraries
import numpy as np
import pandas as pd
from tensorflow.python.keras import models
from tensorflow.python.keras import layers


class ModelTrainer:

    def __init__(self, data):
        self.data = data
        self.features = features
        self.tickers = tickers

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
        
        return train_data, test_data
        
    def calculate_layers(self):
        inputs = []
        for _ in self.tickers:
            inputs.append(len(self.features))
        
        hidden_layers = [layers.Dense(64, activation = "relu")(inp) for inp in inputs]
        concat = layers.Concatenate()(hidden_layers)

        x = layers.Dense(128, activation = "relu")(concat)
        x = layers.Dense(64, activation = "relu")(x)
        output = layers.Dense(1, activation = "linear")(x)

        return inputs, output

        


