from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

import matplotlib.pyplot as plt

def plot_time_series(ax, df, col):
    ax.plot(df.index, df[col], color='#007acc', linewidth=2, marker='o', markersize=4, markerfacecolor='orange')
    ax.set_title(f"Serie de {col}", fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel("Fecha", fontsize=11, labelpad=10)
    ax.set_ylabel("Valor", fontsize=11, labelpad=10)
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_facecolor('#eaf2fa')

def plot_histogram(ax, df, col):
    ax.hist(df[col].dropna(), bins=30, color='#ff9800', edgecolor='black', alpha=0.85)
    ax.set_title(f"Histograma de {col}", fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel("Valor", fontsize=11, labelpad=10)
    ax.set_ylabel("Frecuencia", fontsize=11, labelpad=10)
    ax.grid(True, linestyle=':', alpha=0.5)
    ax.set_facecolor('#fff3e0')

def plot_acf_custom(ax, df, col):
    plot_acf(df[col].dropna(), ax=ax, lags=30)
    ax.set_title(f"ACF de {col}", fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel("Rezago", fontsize=11, labelpad=10)
    ax.set_ylabel("Autocorrelación", fontsize=11, labelpad=10)

def plot_pacf_custom(ax, df, col):
    plot_pacf(df[col].dropna(), ax=ax, lags=30, method='ywm')
    ax.set_title(f"PACF de {col}", fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel("Rezago", fontsize=11, labelpad=10)
    ax.set_ylabel("Autocorrelación parcial", fontsize=11, labelpad=10)

def plot_time_series_analysis(df):
    for col in df.columns:
        fig, axes = plt.subplots(2, 2, figsize=(14, 10), facecolor='#f5f5f5')

        plot_time_series(axes[0, 0], df, col)
        plot_histogram(axes[0, 1], df, col)
        plot_acf_custom(axes[1, 0], df, col)
        plot_pacf_custom(axes[1, 1], df, col)

        for ax in axes.flat[:2]:
            ax.set_aspect('auto')

        plt.tight_layout(rect=[0, 0, 1, 0.97], pad=2.0)
        plt.show()