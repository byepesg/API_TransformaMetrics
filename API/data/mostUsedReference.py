import pandas as pd
import numpy as np
from data.data import loadData
#Third and four card
#Revista más utilizada
def getMostUsedJournal(df: pd.DataFrame):
    df_filtered = df.dropna(subset=['journal'])
    df_filtered['journal'] = df_filtered['journal'].astype(str)
    common = df['journal'].value_counts().idxmax()
    frequency = df['journal'].value_counts().max()
    print("Papers",type(common),type(frequency))
    frequency = frequency.item()
    return {'common': common, 'frequency': frequency}

# Editorial más utilizada
def getMostUsedEditorial(df: pd.DataFrame):
    df_filtered = df.dropna(subset=['publisher'])
    df_filtered['publisher'] = df_filtered['publisher'].astype(str)
    common = df['publisher'].value_counts().idxmax()
    frequency = df['publisher'].value_counts().max()
    print("Books",type(common),type(frequency))
    frequency = frequency.item()
    return {'common': common, 'frequency': frequency}