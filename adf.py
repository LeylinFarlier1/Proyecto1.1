import pandas as pd
from statsmodels.tsa.stattools import adfuller

def analizar_estacionariedad(df):
    """
    Aplica la prueba de Dickey-Fuller aumentada (ADF) a cada columna de un DataFrame.
    Devuelve un DataFrame con los resultados de la prueba y otro con las series diferenciadas si es necesario.
    """

    adf_results = []
    diff_df = pd.DataFrame(index=df.index)  # DataFrame para almacenar las diferencias o las series originales

    for col in df.columns:
        serie = df[col]
        serie_no_na = serie.dropna()
        result = adfuller(serie_no_na)
        estacionaria = "Sí" if result[1] < 0.05 else "No"
        adf_results.append({
            "Serie": col,
            "Estadístico": result[0],
            "p-valor": result[1],
            "¿Estacionaria?": estacionaria
        })
        # Si no es estacionaria, calcula la primera diferencia y la guarda en diff_df
        if estacionaria == "No":
            diff = serie.diff()
            diff_df[col + "_diff"] = diff
        else:
            diff_df[col + "_diff"] = serie  # Si ya es estacionaria, guarda la serie original

    # Convertir los resultados de la prueba ADF a un DataFrame
    adf_df = pd.DataFrame(adf_results)
    return adf_df, diff_df