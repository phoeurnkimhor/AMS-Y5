def normalize_column(df, column):
    if column not in df.columns:
        raise KeyError(f"Column '{column}' not found in DataFrame")

    col_min = df[column].min()
    col_max = df[column].max()

    # Avoid division by zero if all values are the same
    if col_min == col_max:
        df[column] = 0.0
    else:
        df[column] = (df[column] - col_min) / (col_max - col_min)

    return df



