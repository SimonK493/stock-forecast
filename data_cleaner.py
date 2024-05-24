from sklearn.preprocessing import StandardScaler
import pandas as pd

def cleaner(data):
    data = data.ffill()
    print(data.loc["1999-01-04 00:00:00", "AMZN"]["Open"])
    data_scaled = StandardScaler().fit_transform(data)
    df_scaled = pd.DataFrame(data_scaled, index = data.index, columns = data.columns)
    return df_scaled

    
if __name__ == "__main__":
    cd = cleaner()
    
