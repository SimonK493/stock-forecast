from sklearn.preprocessing import StandardScaler, QuantileTransformer
from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd
""" 
 TODO: 
    - Fehlende Daten ersetzen oder entfernen
    - Unregelmäßige Handelszeiten behandeln (--> evtl. wird nicht jeden Tag gehandelt)
    - Ausreiser identifizieren und handhaben
    - Datumsformat kontrollieren
    - Anpassen der Splits und Dividenden (?)
    - Skalieren der Daten, z.B. Min-Max-Skalierung
    - Feature Engineering, z.B. Gleitende Durschnitte über mehrere Tage
"""
def cleaner(data):
    data = data.ffill()
    print(data["AAPL"])
    data_scaled = StandardScaler().fit_transform(data)
    df_scaled = pd.DataFrame(data_scaled, index = data.index, columns = data.columns)
    print(df_scaled["AAPL"])

    
if __name__ == "__main__":
    cleaner()
