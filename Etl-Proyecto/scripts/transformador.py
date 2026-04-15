import pandas as pd

def limpiar_datos(df):
    df['imdb_rating'] = pd.to_numeric(df['imdb_rating'], errors='coerce')

    df['duracion'] = pd.to_numeric(df['duracion'], errors='coerce')

    df['recaudacion'] = pd.to_numeric(df['recaudacion'], errors='coerce')

    df['anio'] = pd.to_numeric(df['anio'], errors='coerce')

    df = df.dropna()

    return df