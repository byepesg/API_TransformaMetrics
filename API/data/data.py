# app/data.py
import httpx
import pandas as pd
import numpy as np

async def loadData(url: str) -> pd.DataFrame:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code == 200:
        data = response.json()

        # Crear un DataFrame con los datos
        df = pd.DataFrame(data)

        # Reemplazar NaN con None y infinitos con valores finitos
        df.replace({np.nan: None, np.inf: np.finfo(np.float64).max, -np.inf: np.finfo(np.float64).min}, inplace=True)

        return df
    else:
        raise ValueError(f"Error al cargar datos desde la URL. Código de estado: {response.status_code}")

