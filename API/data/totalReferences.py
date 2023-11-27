import pandas as pd
import httpx
import numpy as np
from data.data import loadData
#First card 
#Bibliografía: Cantidad de literatura
def getTotalReferences(df: pd.DataFrame) -> int:
    return df.shape[0]