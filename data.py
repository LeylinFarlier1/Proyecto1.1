from tswidgets import sdt_get

def load_series():
    series_ids = ["9.2_PP2_2004_T_16", "9.2_TU_2004_T_17", "160.2_CTA_CORIOS_0_T_39"]
    df = sdt_get(series_ids, start_date="2000-01")
    return df