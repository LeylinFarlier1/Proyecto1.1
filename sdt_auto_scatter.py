import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def sdt_auto_scatter(series, lags=9, ncols=3):
    """
    Genera una cuadrícula de scatterplots que muestran la relación entre una serie temporal y sus rezagos.

    Este gráfico es útil para analizar la autocorrelación visualmente y detectar patrones de dependencia temporal.

    Args:
        series (array-like o pandas.Series): Serie temporal de entrada. Puede ser una lista, array de NumPy o un objeto pandas.Series.
        lags (int, opcional): Número de rezagos (lags) a graficar. Cada subgráfico mostrará la relación entre la serie original y su versión desplazada por este número de pasos. Valor por defecto: 9.
        ncols (int, opcional): Número de columnas en la cuadrícula de subgráficos. El número de filas se calcula automáticamente según la cantidad de rezagos. Valor por defecto: 3.

    Notas:
        - Cada subgráfico muestra un scatterplot entre la serie original y su versión desplazada (rezagada) por un número específico de pasos.
        - El título de cada subgráfico incluye el número de rezago y el coeficiente de correlación entre la serie y su rezago.
        - Es necesario tener instaladas las librerías pandas, numpy, matplotlib y seaborn.

    Returns:
        None. Muestra la figura con los scatterplots.
    """
    # Convierte la entrada en una Serie de pandas (por si acaso).
    series = pd.Series(series)
    # Calcula el número de filas necesarias según la cantidad de rezagos y columnas.
    nrows = int(np.ceil(lags / ncols))
    # Crea una figura y una cuadrícula de subgráficos para los scatterplots.
    fig, axes = plt.subplots(ncols=ncols, nrows=nrows, figsize=(4 * ncols, 4 * nrows))
    # Obtiene el nombre de la serie para el título principal.
    serie_name = series.name if series.name is not None else "Serie"
    # Título principal de la figura.
    fig.suptitle(f"Scatterplots de rezagos para: {serie_name}", fontsize=16, fontweight='bold')
    # Itera sobre cada subgráfico y cada rezago.
    for ax, lag in zip(axes.flat, np.arange(1, lags + 1, 1)):
        lag_str = f't-{lag}'  # Etiqueta del rezago.
        # Crea un DataFrame con la serie original y su versión desplazada (rezagada).
        X = pd.concat([series, series.shift(-lag)], axis=1, keys=['y', lag_str]).dropna()
        # Grafica el scatterplot: valores originales vs. rezagados.
        X.plot(ax=ax, kind='scatter', y='y', x=lag_str)
        # Calcula la correlación entre la serie y su rezago.
        corr = X.corr().to_numpy()[0][1]
        # Etiqueta del eje y y título del subgráfico con el valor de correlación.
        ax.set_ylabel('Original')
        ax.set_title(f'Lag: {lag_str} (corr={corr:.2f})')
        # Ajusta la relación de aspecto del gráfico.
        ax.set_aspect('auto')
        # Elimina los bordes superiores y derechos del gráfico.
        sns.despine()
    # Ajusta el diseño para evitar superposiciones.
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    # Ajusta el espacio vertical entre subgráficos.
    fig.subplots_adjust(hspace=0.4)
    # Muestra la figura.
    plt.show()