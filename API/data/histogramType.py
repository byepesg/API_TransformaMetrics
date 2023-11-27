import pandas as pd
import numpy as np
from data.data import loadData


def getTypeFrequency(df: pd.DataFrame):
    total = df.shape[0]

    # Filtrar por tipo de "revista"
    df_journals = df[df['type'] == 'article']
    journal_frequency = df_journals['year'].value_counts().sort_index()

    # Filtrar por tipo de "editorial"
    df_editorials = df[df['type'] == 'book']
    editorial_frequency = df_editorials['year'].value_counts().sort_index()

    # Filtrar por tipo de "Conferencias"
    df_conferences = df[df['type'] == 'inproceedings']
    conferences_frequency = df_conferences['year'].value_counts().sort_index()

    # Crear un rango de años desde el mínimo al máximo en el DataFrame original
    all_years = pd.Series(range(df['year'].min(), df['year'].max() + 1))

    # Llenar con 0 aquellos años que no están presentes en las frecuencias
    journal_frequency = journal_frequency.reindex(all_years, fill_value=0)
    editorial_frequency = editorial_frequency.reindex(all_years, fill_value=0)
    conferences_frequency = conferences_frequency.reindex(all_years, fill_value=0)

    return {
        "total": total,
        "journal_frequency": journal_frequency.to_json(),
        "journal_count": df_journals.shape[0],
        "editorial_frequency": editorial_frequency.to_json(),
        "editorial_count": df_editorials.shape[0],
        "conferences_frequency": conferences_frequency.to_json(),
        "conferences_count": df_conferences.shape[0],
        "df_journals": df_journals.to_json(),
        "df_editorials": df_editorials.to_json(),
        "df_conferences": df_conferences.to_json()
    }
