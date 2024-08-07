# data_handler.py

import pandas as pd

def load_excel(file_path):
    try:
        if file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        elif file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
            df = df.drop(df.index[-1])
            # df = df.dropna()
        else:
            raise ValueError("Unsupported file format")
            # df = df.astype(int)
        # df = pd.read_excel(file_path)

        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        # df = df.dropna()

        # Find datetime columns and retain only one for simplification
        # datetime_cols = [col for col in df.columns if pd.api.types.is_datetime64_any_dtype(df[col])]
        # if len(datetime_cols) > 1:
        #     df = df[[col for col in df.columns if col not in datetime_cols[1:]]]

        return df, None
    except Exception as e:
        return None, str(e)

def get_column_names(df):
    if df is not None:
        return df.columns.tolist()
    return []

def filter_dataframe(df, columns):
    if df is not None and columns:
        return df[columns]
    return pd.DataFrame()
