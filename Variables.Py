
from data import load_series
df = load_series()

from shap import plot_time_series_analysis
plot_time_series_analysis(df)

from sdt_auto_scatter import sdt_auto_scatter

for col in df.columns:
    sdt_auto_scatter(df[col], lags=9, ncols=3)
    
from adf import analizar_estacionariedad

adf_df, diff_df = analizar_estacionariedad(df) 

import dataframe_image as dfi

dfi.export(adf_df, 'adf_results.png')

plot_time_series_analysis(diff_df)
for col in diff_df.columns:
    sdt_auto_scatter(diff_df[col], lags=9, ncols=3)

adf_df1, _ = analizar_estacionariedad(diff_df)
dfi.export(adf_df1, 'adf_results_diff.png')