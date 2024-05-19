from sklearn.preprocessing import StandardScaler
import pandas as pd

def cleaner(data):
    data = data.ffill()
    print(data["AAPL"])
    data_scaled = StandardScaler().fit_transform(data)
    df_scaled = pd.DataFrame(data_scaled, index = data.index, columns = data.columns)
    print(df_scaled["AAPL"])

    
if __name__ == "__main__":
    cleaner()
