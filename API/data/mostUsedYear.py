import pandas as pd
import httpx
import numpy as np
from data.data import loadData
def getMostUsedYear(df: pd.DataFrame) -> int:
    
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    year = df['year'].mode().iloc[0]
    return int(year)